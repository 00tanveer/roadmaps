import asyncio
from datetime import date
import hashlib
import json
import requests
import time
from dotenv import load_dotenv
import os
import json
import functools
from datetime import datetime

# typing
from typing import Dict, Optional, List

# Async DB session 
from app.db.session import AsyncSessionLocal
from app.db.data_models.podcast import Podcast
from app.db.data_models.episode import Episode
from app.db.data_models.transcript import Transcript
from app.db.data_models.transcript_chapter import TranscriptChapter
from app.db.data_models.transcript_utterance import TranscriptUtterance
from app.db.data_models.transcript_word import TranscriptWord

# sqlalchemy 
from sqlalchemy import select, func, distinct


def get_version():
    with open("version.json") as f:
        return json.load(f)['version']

VERSION = get_version()

def api_handler(max_retries=3, backoff_factor=1.5):
    """
    Decorator to handle network calls, rate limits, retries, and consistent JSON responses.
    - Respects PodcastIndex 'Retry-After' header.
    - Implements exponential backoff for retries.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            retries = 0

            while retries <= max_retries:
                try:
                    req = func(self, *args, **kwargs)
                    res = requests.post(req["url"], headers=req["headers"])

                    # ✅ If successful, return parsed JSON
                    if res.status_code == 200:
                        try:
                            data = res.json()
                            return {
                                "success": True,
                                "status_code": 200,
                                "data": data
                            }
                        except json.JSONDecodeError:
                            return {
                                "success": False,
                                "status_code": 200,
                                "error": "Invalid JSON response",
                                "data": None
                            }

                    # ⚠️ Rate limit exceeded (HTTP 429)
                    elif res.status_code == 429:
                        retry_after = res.headers.get("Retry-After")

                        if retry_after:
                            wait_time = int(retry_after)
                            print(f"⏳ Rate limit hit. Retrying after {wait_time}s...")
                        else:
                            # fallback exponential backoff
                            wait_time = backoff_factor ** retries
                            print(f"⚠️ Rate limit (no Retry-After). Waiting {wait_time:.1f}s...")

                        time.sleep(wait_time)
                        retries += 1
                        continue  # retry

                    # ❌ Other errors
                    else:
                        return {
                            "success": False,
                            "status_code": res.status_code,
                            "error": f"API returned {res.status_code}: {res.text[:200]}",
                            "data": None
                        }

                except requests.exceptions.RequestException as e:
                    # network-level issue
                    wait_time = backoff_factor ** retries
                    print(f"⚠️ Network error: {str(e)}. Retrying in {wait_time:.1f}s...")
                    time.sleep(wait_time)
                    retries += 1
                    continue

            # after all retries failed
            return {
                "success": False,
                "status_code": None,
                "error": f"Max retries ({max_retries}) reached. Request failed.",
                "data": None
            }

        return wrapper
    return decorator

class PDI_API:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('PODCASTINDEX_APIKEY')
        self.api_secret = os.getenv('PODCASTINDEX_SECRET')
        self.base_url = "https://api.podcastindex.org/api/1.0/"
    def build_request(self, query):
        # we'll need the unix time
        epoch_time = int(time.time())
        # our hash here is the api key + secret + time 
        data_to_hash = self.api_key + self.api_secret + str(epoch_time)
        # which is then sha-1'd
        sha_1 = hashlib.sha1(data_to_hash.encode()).hexdigest()
        # now we build our request headers
        headers = {
            'X-Auth-Date': str(epoch_time),
            'X-Auth-Key': self.api_key,
            'Authorization': sha_1,
            'User-Agent': f'Stories Pod v{VERSION}'
        }
        url = self.base_url + query
        request = {
            'url': url,
            'headers': headers
        }
        return request

    @api_handler()
    def getPodcastByFeedURL(self, feed_url):
        query = f"/podcasts/byfeedurl?url={feed_url}"
        return self.build_request(query)

    @api_handler()
    def getEpisodesByFeedURL(self, feed_url):
        query = f"/episodes/byfeedurl?url={feed_url}"
        return self.build_request(query)
    
def __map_feed_to_podcast(feed_data: Dict) -> Podcast:
    """Map PodcastIndex feed data to Podcast ORM model."""
    podcast = Podcast(
        id=str(feed_data.get('id')),
        title=feed_data.get('title', ''),
        url=feed_data.get('url', ''),
        original_url=feed_data.get('originalUrl', ''),
        description=feed_data.get('description', ''),
        cover_image=feed_data.get('image', ''),
        author=feed_data.get('author', ''),
        website=feed_data.get('originalUrl', ''),
        language=feed_data.get('language', ''),
        episode_count=feed_data.get('episodeCount', 0)
    )
    return podcast

def __map_item_to_episode(item: Dict) -> Episode:
    """
    Map an episode item into Episode ORM. Placeholder mapping — adapt fields if needed.
    """
    # datePublished sometimes is unix timestamp or ISO
    pub_raw = item.get("datePublished")
    date_published = None
    pub_raw = item.get("datePublished")
    date_published = (
        datetime.fromtimestamp(pub_raw)
        if pub_raw is not None
        else None
    )

    return Episode(
        id=str(item.get("id")),
        podcast_id=str(item.get("feedId")),
        title=item.get("title") or "",
        podcast_url=item.get("link") or item.get("url") or "",
        podcast_image=item.get("feedImage") or None,
        episode_image=item.get("image") or None,
        enclosure_url=item.get("enclosureUrl") or (item.get("enclosure", {}).get("url") if isinstance(item.get("enclosure"), dict) else None),
        duration=int(item.get("duration") or 0),
        date_published=date_published,
        host_questions=json.dumps(item.get("hostQuestions") or []),  # placeholder: store list as JSON string
    )
def __map_item_to_transcript(item: Dict) -> Transcript:
    """
    Map a transcript item into Transcript ORM. Placeholder mapping — adapt fields if needed.
    """
    return Transcript(
        id=str(item.get("id")),
        episode_id=str(item.get("episodeId")),
        status=item.get("status"),
        audio_url=item.get("audio_url"),
        text=item.get("text"), 
    )

def __map_item_to_transcript_chapter(item: Dict) -> TranscriptChapter:
    """
    Map a transcript chapter into TranscriptChapter ORM
    """
    return TranscriptChapter(
        transcript_id=item.get("transcriptId"),
        summary=item.get("summary"),
        headline=item.get("headline"),
        gist=item.get("gist") or "",
        start=item.get('start'),
        end=item.get("end")
    )

def __map_item_to_transcript_utterance(item: Dict) -> TranscriptChapter:
    """
    Map a transcript utterance into TranscriptUtterance ORM
    """
    return TranscriptUtterance(
        transcript_id=item.get("transcriptId"),
        start=item.get("start"),
        end=item.get("end"),
        confidence=item.get("confidence"),
        speaker=item.get("speaker"),
        text=item.get("text"),
    )

def __map_item_to_transcript_word(item: Dict) -> TranscriptWord:
    """
    Map a transcript word into TranscriptWord ORM
    """
    return TranscriptWord(
        transcript_id=item.get("transcriptId"),
        start=item.get("start"),
        end=item.get("end"),
        confidence=item.get("confidence"),
        speaker=item.get("speaker"),
        text=item.get("text"),
    )
async def save_podcast(feed: Dict):
    """
    Upsert a Podcast row using AsyncSession.merge() — idempotent.
    """
    # Ensure DB tables exist (call init_db() earlier in app startup normally)
    async with AsyncSessionLocal() as session:  # type: AsyncSession
        async with session.begin():
            podcast_obj = __map_feed_to_podcast(feed)
            # session.merge returns a persistent instance; await it because AsyncSession.merge is async
            await session.merge(podcast_obj)
        # commit happens on context exit because begin() used
    return True


async def save_episodes(items: List[Dict]):
    """
    Upsert multiple Episode rows.
    - Tries to use feed_url to find podcast_id (if you prefer), otherwise maps episode's feedId/guid.
    - Uses merge() for idempotent behavior.
    """
    semaphore = asyncio.Semaphore(100) # max 10 concurrent inserts
    async def save_one_episode(item):
        async with semaphore:
            async with AsyncSessionLocal() as session:
                async with session.begin():
                    episode_obj = __map_item_to_episode(item)
                    await session.merge(episode_obj)
            return True
    await asyncio.gather(*(save_one_episode(item) for item in items))
    return True

semaphore = asyncio.Semaphore(5)
async def save_one_transcript(t_dict: Dict, episodes: list, audio_urls: list):
    """Save a single transcript and its child objects."""
    async with semaphore:
        try:
            # Match transcript → episode
            if t_dict['audio_url'] in audio_urls:
                idx = audio_urls.index(t_dict['audio_url'])
                t_dict['episodeId'] = episodes[idx]['id']
            else:
                print(f"⚠️ No matching episode for {t_dict['audio_url']}")
                return False

            # Map ORM objects
            transcript_obj = __map_item_to_transcript(t_dict)

            t_ch_obj_list = [
                __map_item_to_transcript_chapter({**ch, "transcriptId": t_dict["id"]})
                for ch in t_dict.get("chapters", [])
            ]
            t_utt_obj_list = [
                __map_item_to_transcript_utterance({**utt, "transcriptId": t_dict["id"]})
                for utt in t_dict.get("utterances", [])
            ]
            t_word_obj_list = [
                __map_item_to_transcript_word({**w, "transcriptId": t_dict["id"]})
                for w in t_dict.get("words", [])
            ]

            async with AsyncSessionLocal() as session:
                async with session.begin():
                    merged = await session.merge(transcript_obj)
                    session.add_all(t_ch_obj_list)
                    session.add_all(t_utt_obj_list)
                    session.add_all(t_word_obj_list)

                await session.commit()
                print(f"✅ Saved transcript {merged.id} with {len(t_word_obj_list)} words.")
                return True

        except Exception as e:
            print(f"❌ Failed transcript {t_dict.get('id')} — {e}")
            return False
async def save_transcripts(files: List[Dict]):
    """
        Upsert multiple transcript records
        and their child records: words, utterances and
        chapters
    """
    episodes = json.load(open('data/podcasts/pod_episodes_metadata.json', 'r'))
    audio_urls = [e['enclosureUrl'] for e in episodes]

    # create tasks
    tasks = [
        save_one_transcript(t, episodes, audio_urls)
        for t in files
    ]

    # run them concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)

    success = sum(1 for r in results if r is True)
    fail = sum(1 for r in results if r is False or isinstance(r, Exception))

    print(f"\nSummary: ✅ {success} saved, ❌ {fail} failed\n")
    return True

async def read_podcast_metadata(id: str):
    '''
        Read podcast metadata including episode information 
        - podcast title
        - no. of episodes (from podcast table, don't calculate)
        - no. of hours of audio (sql query)
        - author
        - category
        - avg episode duration
        - website
        - avg transcript length
        - avg no. of chapters per episode
        - average number of utterances per episode
        ---- NLP ----
        - most common topics
        - named entities
        -
    '''
    pass
async def get_word_count(session, episode_id: str):
    stmt = (
        select(func.count(TranscriptWord.id))
        .join(Transcript, TranscriptWord.transcript_id == Transcript.id)
        .where(Transcript.episode_id == episode_id)
    )
    result = await session.execute(stmt)
    return result.scalar_one_or_none() or 0

async def get_utterance_count(session, episode_id: str):
    stmt = (
        select(func.count(TranscriptUtterance.id))
        .join(Transcript, TranscriptUtterance.transcript_id == Transcript.id)
        .where(Transcript.episode_id == episode_id)
    )
    result = await session.execute(stmt)
    return result.scalar_one_or_none() or 0
async def get_avg_utterance_duration(session, episode_id: str):
    stmt = (
        select(func.avg(TranscriptUtterance.end - TranscriptUtterance.start))
        .join(Transcript, TranscriptUtterance.transcript_id == Transcript.id)
        .where(Transcript.episode_id == episode_id)
    )
    result = await session.execute(stmt)
    return round(result.scalar_one_or_none() or 0, 2)
async def get_chapter_count(session, episode_id: str):
    stmt = (
        select(func.count(TranscriptChapter.id))
        .join(Transcript, TranscriptChapter.transcript_id == Transcript.id)
        .where(Transcript.episode_id == episode_id)
    )
    result = await session.execute(stmt)
    return result.scalar_one_or_none() or 0
async def read_episode_metadata(episode_id: str) -> Dict:
    '''
        Read episode information including guest information
        - episode title
        - guest 
        - audio_duration
        - total utterances (sql query)
        - avg utterance duration (sql query)
        - questions
        - question answer pair
    '''
    async with AsyncSessionLocal() as session:
        async with session.begin():
            episode_stmt = select(
                Episode.title,
                Episode.duration,
                Podcast.title.label("podcast_title")
            ).join(Podcast, Podcast.id == Episode.podcast_id).where(Episode.id == episode_id)

            episode_row = (await session.execute(episode_stmt)).first()
            if not episode_row:
                return None

            # Run all metric queries concurrently
            word_count, utter_count, avg_dur, chapter_count = await asyncio.gather(
                get_word_count(session, episode_id),
                get_utterance_count(session, episode_id),
                get_avg_utterance_duration(session, episode_id),
                get_chapter_count(session, episode_id)
            )
            print(word_count, utter_count, avg_dur/60, chapter_count)

            return {
                "podcast_title": episode_row.podcast_title,
                "episode_title": episode_row.title,
                "duration_min": round(episode_row.duration / 60, 1),
                "word_count": word_count,
                "utterance_count": utter_count,
                "avg_utterance_duration_sec": avg_dur,
                "chapter_count": chapter_count,
            }

                

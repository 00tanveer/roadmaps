# Create a csv of all podcasts with Podcastindex feed url, title, category DONE
# Write a Python API wrapper for Podcastindex API DONE
# Populate podcasts_metadata.json

from app.services.podcasts import PDI_API
import csv 
import json
import os

def fetch_podcasts_metadata():
    podcast_feedurls_csv_path = "data/podcasts/podcast_feedurls.csv"
    pdi_api = PDI_API()
    pods_to_fetch = []
    try:
        with open(podcast_feedurls_csv_path, mode='r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)

            for row in csv_reader:
                pods_to_fetch.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{podcast_feedurls_csv_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    pods = []
    for pod in pods_to_fetch:
        print(pod)
        # sanitize the feed URL (CSV may include stray quotes or trailing commas)
        raw_feed = pod[2] if len(pod) > 2 else ''
        feed_url = raw_feed.strip().strip('"').strip("'").rstrip(',')
        res = pdi_api.getPodcastByFeedURL(feed_url)
        # PDI_API.api_handler returns a dict like {"success": bool, "status_code": int, "data": ..., "error": ...}
        if res.get('status_code') == 200 and res.get('success'):
            data = res.get('data') or {}
            feed = data.get('feed') if isinstance(data, dict) else None
            if feed:
                print(feed.get('title'))
                pods.append(feed)
            else:
                print(f"Warning: no feed data for {feed_url}: {res}")
        else:
            print(f"Error fetching {feed_url}: {res.get('error') or res}")

    # Write the collected feeds to JSON file
    try:
        with open('data/podcasts/podcasts_metadata.json', 'w') as out_f:
            json.dump(pods, out_f, indent=2)
        print(f"Wrote {len(pods)} podcast(s) to data/podcasts/podcasts_metadata.json")
    except Exception as e:
        print(f"Failed to write podcasts_metadata.json: {e}")

def fetch_episodes_metadata():
    # Placeholder for fetching episodes metadata
    podcast_feedurls_csv_path = "data/podcasts/podcast_feedurls.csv"
    pdi_api = PDI_API()
    pods_to_fetch_from = []
    try:
        with open(podcast_feedurls_csv_path, mode='r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)

            for row in csv_reader:
                pods_to_fetch_from.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{podcast_feedurls_csv_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    episodes = []
    for pod in pods_to_fetch_from:
        print(pod)
        # sanitize the feed URL (CSV may include stray quotes or trailing commas)
        raw_feed = pod[2] if len(pod) > 2 else ''
        feed_url = raw_feed.strip().strip('"').strip("'").rstrip(',')
        res = pdi_api.getEpisodesByFeedURL(feed_url)
        if res.get('status_code') == 200 and res.get('success'):
            data = res.get('data') or {}
            eps = data.get('items') if isinstance(data, dict) else None
            if eps:
                print(f"Fetched {len(eps)} episodes for {feed_url}")
                episodes.extend(eps)
            else:
                print(f"Warning: no episode data for {feed_url}: {res}")
        else:
            print(f"Error fetching episodes for {feed_url}: {res.get('error') or res}")

        # Write the collected feeds to JSON file
        try:
            with open('data/podcasts/pod_episodes_metadata.json', 'w') as out_f:
                json.dump(episodes, out_f, indent=2)
            print(f"Wrote {len(episodes)} episodes(s) to data/podcasts/pod_episodes_metadata.json")
        except Exception as e:
            print(f"Failed to write podcasts_metadata.json: {e}")
if not os.path.exists('data/podcasts/podcasts_metadata.json'):
    fetch_podcasts_metadata()

if not os.path.exists('data/podcasts/pod_episodes_metadata.json'):
    fetch_episodes_metadata()

episodes = json.load(open('data/podcasts/pod_episodes_metadata.json', 'r'))
pods = json.load(open('data/podcasts/podcasts_metadata.json', 'r'))
count = 0

# for e in episodes:
#     if e['feedId'] in [p['id'] for p in pods]:
#         #print podcast title
#         matching_pod = next((p for p in pods if p['id'] == e['feedId']), None)
#         if matching_pod:
#             print(f"Podcast Title: {matching_pod['title']}")
#     print(e['title'])
#     if e['transcriptUrl'] is not None:
#         count += 1
#         print(f"Transcript URL: {e['transcriptUrl']}")
# total episides 
print(len(episodes)) # 243
mp3Count = 0
# for e in episodes:
#     if e['enclosureUrl'] is not None and 'mp3' in e['enclosureUrl']:
#         mp3Count += 1
#         # print(e['transcriptUrl'])
#     else:
#         print(e['enclosureUrl'])

print(f"Total episodes with mp3: {mp3Count}") # 228
print(f"Total episodes with transcripts: {count}") # very few

# Create directories for all podcasts inside data/podcasts/ if not exist DONE 
if os.path.exists('data/podcasts/podcasts_metadata.json'):
    pods = json.load(open('data/podcasts/podcasts_metadata.json', 'r'))
    for pod in pods:
        pod_title = pod.get('title', 'unknown_podcast').replace('/', '_').replace('\\', '_')
        pod_dir = os.path.join('data/podcasts/', pod_title)
        if not os.path.exists(pod_dir):
            os.makedirs(pod_dir)
            print(f"Created directory: {pod_dir}")
        else:
            print(f"Directory already exists: {pod_dir}")





# Similarly fetch episodes for each podcast and write to pod_episodes_metadata.json


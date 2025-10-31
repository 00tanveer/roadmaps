import re
import yaml
path = 'content/1-ilya-grigorik--ryan-peterman.md'

# print(text[:5])
def parse_frontmatter(f):
    lines = f.readlines()
    idx = [i for i,l in enumerate(lines) if l == '---\n']
    frontmatter = lines[idx[0]+1:idx[1]]
    frontmatter = [l.strip() for l in frontmatter]
    frontmatter = '\n'.join(frontmatter)
    frontmatter = yaml.safe_load(frontmatter)
    return frontmatter

def parse_transcript(f):
    lines = f.readlines()
    idx = [i for i,l in enumerate(lines) if l == '---\n']
    transcript = lines[idx[1]+1:]
    transcript = [l.strip() for l in transcript]

    return transcript
def build_metadata(frontmatter):
    guest = {
        "name": frontmatter.get("guest_name"),
        "title": frontmatter.get("biggest_role"),
        "company": frontmatter.get("current_company"),
        "company_size": frontmatter.get("company_size"),
        "YOE_starting": frontmatter.get("YOE-starting"),
        "background": frontmatter.get("guest_background"),
    }

    episode = {
        "title": frontmatter.get("episode_title"),
        "description": frontmatter.get("episode_description"),
        "date": frontmatter.get("episode_date"),
        "duration_minutes": frontmatter.get("episode_duration"),
        "topics": frontmatter.get("topics"),
    }

    return {"guest": guest, "episode": episode}

def build_blocks(lines):
    blocks = []
    current_speaker = None
    current_topic = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Detect topic line (### Google acquisition story)
        topic_match = re.match(r'^#{3}\s*(.+)$', line)
        if topic_match:
            current_topic = topic_match.group(1).strip()
            continue
        # Speaker line like "Ryan:"
        if re.match(r'^[A-Z][A-Za-z0-9._\- ]+:$', line):
            current_speaker = line[:-1]
            continue

        # Timestamped line like "[00:01:10] Text..."
        m = re.match(r'^\[?(\d{2}:\d{2}(?::\d{2})?)\]?\s*(.*)', line)
        if m:
            timestamp = m.group(1)
            text_line = m.group(2)
            blocks.append({
                "topic": current_topic,
                "speaker": current_speaker,
                "timestamp": timestamp,
                "text": text_line
            })
    return blocks
with open(path, 'r') as f:
    frontmatter = parse_frontmatter(f)
    metadata = build_metadata(frontmatter)
    f.seek(0)
    transcript = parse_transcript(f)
    blocks = build_blocks(transcript)

## Goal - Extract clean blocks from transcript with context
# {
#   "episode_id": "facebook_dwayne",
#   "guest": {
#     "name": "Dwayne Johnson",
#     "title": "Software Engineer",
#     "company": "Facebook",
#     "interview_date": "2015-07-12",
#     "summary": "Dwayne discusses joining Facebook after MIT and choosing it over Google and Amazon."
#   },
#   "num_blocks": 2,
#   "blocks": [
#     {
#       "speaker": "Ryan",
#       "timestamp_start": "00:00:39",
#       "text": "Thank you Dwayne, for coming on...",
#       "word_count": 85,
#       "embedding": [0.123, 0.553, ...],
#       "keywords": ["Facebook", "MIT", "career story"],
#       "sentiment": 0.21,
#       "entities": ["Facebook", "MIT"],
#       "summary_sentence": "Thank you Dwayne, for coming on."
#     },
#     ...
#   ]
# }

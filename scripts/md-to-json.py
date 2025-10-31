import re
import yaml
path = '../content/1-ilya-grigorik--ryan-peterman.md'

# print(text[:5])
def parse_frontmatter(file):
    lines = f.readlines()
    idx = [i for i,l in enumerate(lines) if l == '---\n']
    frontmatter = lines[idx[0]+1:idx[1]]
    frontmatter = [l.strip() for l in frontmatter]
    frontmatter = '\n'.join(frontmatter)
    frontmatter = yaml.safe_load(frontmatter)
    return frontmatter
def build_metadata():
    return 0

with open(path, 'r') as f:
    lines = f.readlines()

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

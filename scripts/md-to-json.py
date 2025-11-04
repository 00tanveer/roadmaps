import re
import yaml
import os
import json

# print(text[:5])
def parse_frontmatter(f):
    lines = f.readlines()
    idx = [i for i,l in enumerate(lines) if l == '---\n']
    print(idx)
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
        "host": frontmatter.get("host_name"),
        "description": frontmatter.get("episode_description"),
        "date": frontmatter.get("episode_date"),
        "duration_minutes": frontmatter.get("episode_duration"),
        "topics": frontmatter.get("topics"),
    }

    return {"guest": guest, "episode": episode}

# def build_blocks(lines):
#     blocks = []
#     current_speaker = None
#     current_topic = None

#     for line in lines:
#         line = line.strip()
#         if not line:
#             continue

#         # Detect topic line (### Google acquisition story)
#         topic_match = re.match(r'^#{3}\s*(.+)$', line)
#         if topic_match:
#             current_topic = topic_match.group(1).strip()
#             continue
#         # Speaker line like "Ryan:"
#         if re.match(r'^[A-Z][A-Za-z0-9._\- ]+:$', line):
#             current_speaker = line[:-1]
#             continue

#         # Timestamped line like "[00:01:10] Text..."
#         m = re.match(r'^\[?(\d{2}:\d{2}(?::\d{2})?)\]?\s*(.*)', line)
#         if m:
#             timestamp = m.group(1)
#             text_line = m.group(2)
#             blocks.append({
#                 "topic": current_topic,
#                 "speaker": current_speaker,
#                 "timestamp": timestamp,
#                 "text": text_line
#             })

#         # --- Detect "Name 00:02:40:" pattern
#         inline_match = re.match(r'^([A-Z][A-Za-z0-9._\- ]+)\s+(\d{2}:\d{2}(?::\d{2})?):$', line)
#         if inline_match:
#             current_speaker = inline_match.group(1).strip()
#             timestamp = inline_match.group(2)
#             blocks.append({
#                 "topic": current_topic,
#                 "speaker": current_speaker,
#                 "timestamp": timestamp,
#                 "text": ""
#             })
#             continue
#         # --- Otherwise, treat as continuation text for previous speaker (no new timestamp)
#         if blocks and current_speaker:
#             # append to the most recent block
#             if blocks[-1]["text"]:
#                 blocks[-1]["text"] += " " + line
#             else:
#                 blocks[-1]["text"] = line
#     return blocks


def build_blocks(lines, host_name, guest_name):
    blocks = []
    current_topic = None
    current_speaker = None
    current_text = []
    current_timestamp = None

    def finalize_block():
        """Helper to save a block before switching speakers."""
        if current_speaker and current_text:
            blocks.append({
                "topic": current_topic,
                "speaker": current_speaker,
                "timestamp": current_timestamp,
                "text": " ".join(current_text).strip()
            })

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Detect topic lines (### ...)
        topic_match = re.match(r'^#{3}\s*(.+)$', line)
        if topic_match:
            current_topic = topic_match.group(1).strip()
            continue

        # Detect timestamped lines like "[00:01:10] Text..."
        m = re.match(r'^\[?(\d{2}:\d{2}(?::\d{2})?)\]?\s*(.*)', line)
        if m and not line.endswith(':'):
            timestamp = m.group(1)
            text_line = m.group(2).strip()
            if current_speaker:
                if not current_timestamp:
                    current_timestamp = timestamp
                current_text.append(text_line)
            continue

        # Detect lines like "Ryan 00:02:40:" or "Ryan:"
        inline_match = re.match(r'^([A-Z][A-Za-z0-9._\- ]+)\s*(\d{2}:\d{2}(?::\d{2})?)?:$', line)
        if inline_match:
            # Speaker change → finalize current block
            finalize_block()
            current_speaker = inline_match.group(1).strip()
            current_timestamp = inline_match.group(2) if inline_match.group(2) else None
            current_text = []
            continue

        # Otherwise it's continuation text
        if current_speaker:
            current_text.append(line)

    # Save last one
    finalize_block()

    # ---- Pair host and guest blocks ----
    qa_pairs = []
    for i in range(len(blocks) - 1):
        q = blocks[i]
        a = blocks[i + 1]
        if q["speaker"] == host_name and a["speaker"] == guest_name:
            qa_pairs.append({
                "topic": q["topic"],
                "question_speaker": q["speaker"],
                "answer_speaker": a["speaker"],
                "question_text": q["text"],
                "answer_text": a["text"],
                "start_time": q["timestamp"],
                "end_time": a["timestamp"]
            })

    return qa_pairs
# for all markdown files in /content extract metadata and transcript
# blocks for each document, and store them in json
folder_path = "content/"
filepaths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
documents = []
for filepath in filepaths:
    print(filepath)
    with open(filepath, 'r') as f:
        frontmatter = parse_frontmatter(f)
        if frontmatter is None: # Skip file if frontmatter is not found or has parsing errors
            print(f"Skipping file {filepath} due to missing or invalid frontmatter.")
            continue
        metadata = build_metadata(frontmatter)
        f.seek(0) # Reset file pointer after reading frontmatter
        transcript = parse_transcript(f)
        blocks = build_blocks(transcript, host_name=metadata['episode']['host'].split()[0], guest_name=metadata['guest']['name'].split()[0])
        document = {} # Create a new document dictionary for each file
        document['guest'] = metadata['guest']['name']
        print(document['guest'])
        document['blocks'] = blocks
        documents.append(document)
none_count = 0
total_count = 0

for doc in documents:
    for block in doc['blocks']:
        total_count += 1
        if block['topic'] is None or block['topic'] == 'None':
            none_count += 1

print(f"{none_count}/{total_count} topics are None ({none_count/total_count*100:.1f}%)")

# get file names without extensions from content/
filepaths = [os.path.basename(f) for f in filepaths]
for i,path in enumerate(filepaths):
    path = 'content-json/' + path[:-2] + 'json'
    with open(path, 'w') as f:
        json.dump(documents[i], f, indent=4)



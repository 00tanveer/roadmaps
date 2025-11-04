# use BERT to summarize each block
import os
import json
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


def extractive_insights(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return "\n".join(f"- Insight {i+1}: {str(s)}" for i, s in enumerate(summary))

# Load JSON files from content-json directory
folder_path = "content-json/"
filepaths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
for path in filepaths:
    with open(path, 'r') as f:
        data = json.load(f)
    
# Summarize blocks with the same topic
    current_topic = None
    topic_texts = []
    for block in data['blocks']:
        if block['topic'] != current_topic:
            # Summarize previous topic texts
            if current_topic and topic_texts:
                combined_text = " ".join(topic_texts)
                print(f"Guest: {data['guest'] } - Summarizing topic: {current_topic}")
                summary = extractive_insights(combined_text)
                print(summary)
                # Assign summary to all blocks of the previous topic
                for b in data['blocks']:
                    if b['topic'] == current_topic:
                        b['summary'] = summary
            # Reset for new topic
            current_topic = block['topic']
            topic_texts = [block['text']]
        else:
            topic_texts.append(block['text'])
    # Summarize the last topic
    if current_topic and topic_texts:
        combined_text = " ".join(topic_texts)
        print(f"Guest: {data['guest'] } - Summarizing topic: {current_topic}")
        summary = extractive_insights(combined_text)
        print(summary)
        for b in data['blocks']:
            if b['topic'] == current_topic:
                b['summary'] = summary
    
    
    # # Save the updated JSON back to file
    # with open(path, 'w') as f:
    #     json.dump(data, f, indent=4)
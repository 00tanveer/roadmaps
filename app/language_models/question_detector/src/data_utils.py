# src/dataset.py
from datasets import Dataset
from transformers import AutoTokenizer
from src.config import MODEL_NAME, MAX_LENGTH
import json

def load_dataset(data_path: str = "data/training.json", test_size: float = 0.2):
    with open(data_path, "r") as f:
        data = json.load(f)
    return Dataset.from_list(data).train_test_split(test_size=test_size)

def tokenize_dataset(dataset):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    def tokenize(batch):
        return tokenizer(batch["text"], padding="max_length", truncation=True, max_length=MAX_LENGTH)
    dataset = dataset.map(tokenize, batched=True)
    dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])
    return dataset, tokenizer

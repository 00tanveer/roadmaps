# src/train.py
from transformers import TrainingArguments, Trainer, AutoModelForSequenceClassification
from src.data_utils import load_dataset, tokenize_dataset
from src.config import MODEL_NAME, SAVE_DIR, EPOCHS, LR, BATCH_SIZE

def train():
    dataset = load_dataset()
    dataset, tokenizer = tokenize_dataset(dataset)

    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

    args = TrainingArguments(
        output_dir=SAVE_DIR,
        eval_strategy="epoch",
        save_strategy="epoch",
        num_train_epochs=EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        learning_rate=LR,
        logging_steps=50,
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        tokenizer=tokenizer,
    )

    trainer.train()
    model.save_pretrained(SAVE_DIR)
    tokenizer.save_pretrained(SAVE_DIR)

if __name__ == "__main__":
    train()

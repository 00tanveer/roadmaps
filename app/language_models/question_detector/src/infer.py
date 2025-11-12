from transformers import pipeline, AutoTokenizer
from pathlib import Path

class InferenceModel:
    def __init__(self):
        base_dir = Path(__file__).resolve().parents[1]
        print(base_dir)
        self.model_dir = base_dir / "models" / "distilbert_question_detector"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_dir)
        self.pipe = pipeline("text-classification", model=self.model_dir, tokenizer=self.tokenizer)

    def predict(self, text: str):
        return self.pipe(text)
# # Example usage
# infer_model = InferenceModel()
# print(infer_model.predict("What inspired you to start your company?"))
# print(infer_model.predict("Hogar baal"))


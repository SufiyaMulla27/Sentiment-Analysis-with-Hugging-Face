from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import pipeline

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

result = sentiment_pipeline("I love using Hugging Face!")
print(result)


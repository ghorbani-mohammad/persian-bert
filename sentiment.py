from transformers import pipeline
from transformers import AutoTokenizer

# sentiment
tokenizer = AutoTokenizer.from_pretrained('/app/model')
sentiment_model = pipeline('sentiment-analysis', model='/app/model')
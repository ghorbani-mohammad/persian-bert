from transformers import pipeline
from transformers import AutoTokenizer

# sentiment
sentiment_model = pipeline('sentiment-analysis', model='/app/model')
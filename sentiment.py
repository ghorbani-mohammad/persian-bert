from transformers import pipeline

# sentiment
sentiment_model = pipeline('sentiment-analysis', model='/app/model')
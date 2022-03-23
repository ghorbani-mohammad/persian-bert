from transformers import pipeline

# sentiment
text = "سیب‌زمینی بی‌کیفیت بود."
sentiment_model = pipeline('sentiment-analysis', model='/app/model', return_all_scores=True)
result = sentiment_model(text)
print(result)
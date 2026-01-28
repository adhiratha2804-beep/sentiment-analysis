from textblob import TextBlob

def sentiment_analysis(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive sentiment"
    elif polarity < 0:
        return "Negative sentiment"
    else:
        return "Neutral sentiment"

# Example inputs
texts = [
    "This product is amazing!",
    "I am very disappointed with the service.",
    "The phone is okay, nothing special."
]

for t in texts:
    print(f"Text: {t}")
    print("Sentiment:", sentiment_analysis(t))
    print()
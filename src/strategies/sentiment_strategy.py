
import pandas as pd
from textblob import TextBlob

def sentiment_strategy(text_data, method="basic", clustering=False):
    sentiment_scores = text_data.apply(lambda x: TextBlob(x).sentiment.polarity)
    if method == "basic":
        signals = sentiment_scores.apply(lambda x: "Buy" if x > 0.5 else ("Sell" if x < -0.5 else "Hold"))
        return pd.DataFrame({"Text": text_data, "Sentiment Score": sentiment_scores, "Signal": signals})
    elif method == "index":
        sentiment_index = sentiment_scores.mean()
        signal = "Buy" if sentiment_index > 0.5 else ("Sell" if sentiment_index < -0.5 else "Hold")
        return {"Sentiment Index": sentiment_index, "Signal": signal}
    elif clustering:
        sentiment_df = pd.DataFrame({"Text": text_data, "Sentiment": sentiment_scores})
        sentiment_df["Sentiment Cluster"] = pd.qcut(sentiment_df["Sentiment"], q=3, labels=["Negative", "Neutral", "Positive"])
        return sentiment_df
    else:
        raise ValueError("Invalid method or clustering option. Use 'basic', 'index', or clustering=True.")

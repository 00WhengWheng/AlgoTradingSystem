import requests

def event_driven_social_strategy(posts, price_data):
    """
    Event-Driven Social Strategy.
    
    :param posts: List of social media posts or comments.
    :param price_data: pd.Series of price data.
    :return: Sentiment-driven trading signals.
    """
    from textblob import TextBlob
    
    sentiment_scores = [TextBlob(post).sentiment.polarity for post in posts]
    price_reaction = price_data.pct_change()
    
    signals = ["Buy" if score > 0.5 and ret < 0 else "Sell" if score < -0.5 and ret > 0 else "Hold"
               for score, ret in zip(sentiment_scores, price_reaction)]
    
    return pd.DataFrame({
        "Post": posts,
        "Sentiment Score": sentiment_scores,
        "Price Reaction": price_reaction,
        "Signal": signals
    })

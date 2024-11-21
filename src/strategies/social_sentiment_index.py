def social_sentiment_index(posts):
    """
    Create a Social Sentiment Index.
    
    :param posts: List of social media posts or comments.
    :return: Sentiment index and trading signals.
    """
    from textblob import TextBlob
    import pandas as pd
    
    sentiment_scores = [TextBlob(post).sentiment.polarity for post in posts]
    sentiment_index = sum(sentiment_scores) / len(sentiment_scores)
    
    # Generate signal
    signal = "Buy" if sentiment_index > 0.5 else "Sell" if sentiment_index < -0.5 else "Hold"
    
    return {
        "Sentiment Index": sentiment_index,
        "Signal": signal
    }

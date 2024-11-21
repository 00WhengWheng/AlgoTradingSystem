from textblob import TextBlob

def sentiment_analysis_trading(text_data):
    """
    Sentiment Analysis for Trading.
    
    :param text_data: List or pd.Series of text data (e.g., tweets, articles).
    :return: Sentiment scores and trading signals.
    """
    sentiment_scores = text_data.apply(lambda x: TextBlob(x).sentiment.polarity)
    
    # Generate signals based on sentiment
    signals = sentiment_scores.apply(lambda x: 'Buy' if x > 0.5 else ('Sell' if x < -0.5 else 'Hold'))
    
    sentiment_df = pd.DataFrame({
        "Text": text_data,
        "Sentiment Score": sentiment_scores,
        "Signal": signals
    })
    
    print("Sentiment-Based Trading Signals:")
    print(sentiment_df.head())
    
    return sentiment_df

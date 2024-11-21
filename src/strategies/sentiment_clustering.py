from textblob import TextBlob
import pandas as pd

def sentiment_clustering_strategy(text_data):
    """
    Sentiment Clustering Strategy.
    
    :param text_data: List or pd.Series of text data (e.g., tweets, articles).
    :return: Sentiment scores and cluster labels.
    """
    # Calculate sentiment polarity
    sentiments = text_data.apply(lambda text: TextBlob(text).sentiment.polarity)
    
    # Create clusters
    sentiment_df = pd.DataFrame({'Text': text_data, 'Sentiment': sentiments})
    sentiment_df['Sentiment Cluster'] = pd.qcut(sentiment_df['Sentiment'], q=3, labels=['Negative', 'Neutral', 'Positive'])
    
    # Analyze sentiment clusters
    cluster_counts = sentiment_df['Sentiment Cluster'].value_counts()
    print("Sentiment Clusters:\n", cluster_counts)
    
    return sentiment_df

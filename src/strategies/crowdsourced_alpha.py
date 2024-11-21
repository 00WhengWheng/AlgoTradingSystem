import requests
from textblob import TextBlob
import pandas as pd

def crowdsourced_alpha(strategy_data):
    """
    Crowdsourced Alpha Strategy using sentiment and top performer signals.
    
    :param strategy_data: Dict with keys 'social_sentiment_api' and 'trading_leaderboard_api'.
    :return: Aggregated sentiment and top performers' trades.
    """
    # Fetch sentiment data from API
    sentiment_response = requests.get(strategy_data['social_sentiment_api']).json()
    sentiment_scores = [
        TextBlob(post['text']).sentiment.polarity for post in sentiment_response['posts']
    ]
    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    
    # Fetch top performers from trading leaderboard API
    leaderboard_response = requests.get(strategy_data['trading_leaderboard_api']).json()
    top_trades = pd.DataFrame(leaderboard_response['top_performers'])

    # Combine data
    result = {
        'Average Sentiment': avg_sentiment,
        'Top Performers Trades': top_trades
    }
    
    print(f"Average Sentiment: {avg_sentiment:.2f}")
    print("Top Performers' Trades:")
    print(top_trades)
    return result

import spacy
from transformers import pipeline

def nlp_news_analysis(news_data):
    """
    NLP for Financial News and Reports.
    
    :param news_data: List or pd.Series of news headlines or reports.
    :return: Extracted sentiments and key entities.
    """
    # Load spaCy model for named entity recognition
    nlp = spacy.load("en_core_web_sm")
    
    # Load HuggingFace pipeline for sentiment analysis
    sentiment_analyzer = pipeline("sentiment-analysis")
    
    analysis_results = []
    for text in news_data:
        # Sentiment Analysis
        sentiment = sentiment_analyzer(text)[0]
        
        # Named Entity Recognition
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        
        # Store results
        analysis_results.append({
            "Text": text,
            "Sentiment": sentiment['label'],
            "Sentiment Score": sentiment['score'],
            "Entities": entities
        })
    
    # Convert results to DataFrame
    results_df = pd.DataFrame(analysis_results)
    print("NLP Analysis Results:")
    print(results_df.head())
    return results_df

## advanced refinements

from sklearn.feature_extraction.text import TfidfVectorizer

def keyword_extraction(news_data, top_n=5):
    """
    Keyword Extraction from Financial News.
    
    :param news_data: List or pd.Series of news articles or reports.
    :param top_n: Number of top keywords to extract.
    :return: List of top keywords for each article.
    """
    vectorizer = TfidfVectorizer(stop_words="english", max_features=top_n)
    tfidf_matrix = vectorizer.fit_transform(news_data)
    keywords = vectorizer.get_feature_names_out()
    
    print("Top Keywords:")
    print(keywords)
    return keywords

## sentiment weghted signal

def sentiment_weighted_signals(sentiment_scores, impact_factors):
    """
    Sentiment-Weighted Signals.
    
    :param sentiment_scores: List of sentiment scores (e.g., from NLP analysis).
    :param impact_factors: Market impact factors (e.g., volatility, volume).
    :return: Weighted signals.
    """
    weighted_signals = [score * impact for score, impact in zip(sentiment_scores, impact_factors)]
    print("Sentiment-Weighted Signals:")
    print(weighted_signals)
    return weighted_signals


## with financial api integration

import requests

def fetch_financial_news(api_key, ticker, language="en"):
    """
    Fetch financial news from Alpha Vantage.
    
    :param api_key: Alpha Vantage API key.
    :param ticker: Stock ticker symbol.
    :param language: Language filter for news.
    :return: List of news articles.
    """
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "NEWS_SENTIMENT",
        "tickers": ticker,
        "apikey": api_key,
        "language": language
    }
    response = requests.get(url, params=params)
    news_data = response.json()
    
    if "feed" in news_data:
        news_articles = news_data["feed"]
        print(f"Fetched {len(news_articles)} articles for {ticker}.")
        return news_articles
    else:
        print("Error fetching news:", news_data.get("Note", "Unknown error"))
        return []

import yfinance as yf

def fetch_stock_prices(ticker, period="1mo", interval="1d"):
    """
    Fetch historical stock prices using yFinance.
    
    :param ticker: Stock ticker symbol.
    :param period: Period of data (e.g., "1mo", "6mo").
    :param interval: Data interval (e.g., "1d", "1h").
    :return: DataFrame of stock prices.
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    print(f"Fetched {len(hist)} rows of price data for {ticker}.")
    return hist



def analyze_news_sentiment(news_articles):
    """
    Analyze sentiment of financial news articles.
    
    :param news_articles: List of news articles (e.g., from Alpha Vantage).
    :return: DataFrame with sentiment scores and signals.
    """
    from textblob import TextBlob
    import pandas as pd

    sentiment_results = []
    for article in news_articles:
        sentiment = TextBlob(article["title"]).sentiment.polarity
        signal = "Buy" if sentiment > 0.5 else "Sell" if sentiment < -0.5 else "Hold"
        sentiment_results.append({
            "Title": article["title"],
            "Sentiment Score": sentiment,
            "Signal": signal,
            "Published Date": article["time_published"]
        })
    
    sentiment_df = pd.DataFrame(sentiment_results)
    print("Sentiment Analysis Results:")
    print(sentiment_df.head())
    return sentiment_df


def correlate_sentiment_with_prices(sentiment_df, stock_prices):
    """
    Correlate sentiment with stock price changes.
    
    :param sentiment_df: DataFrame with sentiment analysis results.
    :param stock_prices: DataFrame with stock price data.
    :return: Correlation statistics.
    """
    stock_prices['Daily Return'] = stock_prices['Close'].pct_change()
    sentiment_df['Date'] = pd.to_datetime(sentiment_df['Published Date']).dt.date
    stock_prices['Date'] = stock_prices.index.date
    
    # Merge sentiment and price data
    merged_data = pd.merge(sentiment_df, stock_prices, on="Date", how="inner")
    correlation = merged_data['Sentiment Score'].corr(merged_data['Daily Return'])
    
    print(f"Sentiment and Price Correlation: {correlation:.2f}")
    return merged_data, correlation


### usage
api_key = "your_alpha_vantage_api_key"
ticker = "AAPL"

news_articles = fetch_financial_news(api_key, ticker)
stock_prices = fetch_stock_prices(ticker, period="1mo")

sentiment_df = analyze_news_sentiment(news_articles)

merged_data, correlation = correlate_sentiment_with_prices(sentiment_df, stock_prices)


## advanced enhance

from transformers import pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="yiyanghkust/finbert-tone")

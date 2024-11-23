import sqlite3
import pandas as pd

DB_FILE = "trading_dashboard.db"

def create_database():
    """
    Create the SQLite database and tables if they don't exist.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Tabella per i dati finanziari
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS financial_data (
        id INTEGER PRIMARY KEY,
        ticker TEXT,
        date DATE,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume INTEGER
    )
    """)

    # Tabella per le strategie
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS strategies (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        ticker TEXT,
        parameters TEXT,
        interval TEXT,
        start_date DATE,
        end_date DATE,
        last_run DATE,
        optimized_parameters TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("Database created and initialized.")

def insert_financial_data(ticker, data):
    """
    Insert financial data into the database.
    :param ticker: Ticker symbol.
    :param data: DataFrame containing financial data.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for _, row in data.iterrows():
        cursor.execute("""
        INSERT INTO financial_data (ticker, date, open, high, low, close, volume)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (ticker, row["Date"], row["Open"], row["High"], row["Low"], row["Close"], row["Volume"]))

    conn.commit()
    conn.close()
    print(f"Inserted financial data for {ticker}.")

def fetch_financial_data(ticker):
    """
    Fetch financial data for a given ticker from the database.
    :param ticker: Ticker symbol.
    :return: DataFrame with financial data.
    """
    conn = sqlite3.connect(DB_FILE)
    query = "SELECT date, open, high, low, close, volume FROM financial_data WHERE ticker = ?"
    data = pd.read_sql_query(query, conn, params=(ticker,))
    conn.close()
    return data

def save_optimized_parameters(strategy_name, optimized_params):
    """
    Save the optimized parameters for a strategy.
    :param strategy_name: Name of the strategy.
    :param optimized_params: Dictionary of optimized parameters.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE strategies
    SET optimized_parameters = ?
    WHERE name = ?
    """, (str(optimized_params), strategy_name))

    conn.commit()
    conn.close()
    print(f"Optimized parameters for strategy '{strategy_name}' saved.")

def fetch_optimized_parameters(strategy_name):
    """
    Fetch the optimized parameters for a given strategy.
    :param strategy_name: Name of the strategy.
    :return: Dictionary of optimized parameters.
    """
    conn = sqlite3.connect(DB_FILE)
    query = "SELECT optimized_parameters FROM strategies WHERE name = ?"
    result = pd.read_sql_query(query, conn, params=(strategy_name,))
    conn.close()

    if result.empty or result["optimized_parameters"].iloc[0] is None:
        return {}
    return eval(result["optimized_parameters"].iloc[0])  # Convert string back to dictionary

# src/utils/db_connector.py

import sqlite3
import pandas as pd
from sqlalchemy import create_engine

def create_sqlite_connection(db_path='../data/database/trading.db'):
    """Creates a SQLite database connection."""
    conn = sqlite3.connect(db_path)
    return conn

def execute_query(query, db_path='../data/database/trading.db'):
    """Executes a query on the SQLite database."""
    conn = create_sqlite_connection(db_path)
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

def save_df_to_sql(df, table_name, db_path='../data/database/trading.db'):
    """Saves a DataFrame to a SQL table."""
    engine = create_engine(f'sqlite:///{db_path}')
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    engine.dispose()

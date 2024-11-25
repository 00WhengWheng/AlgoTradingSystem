import psycopg2
import logging

class DatabaseWriter:
    def __init__(self, db_config):
        self.db_config = db_config

    def write_to_db(self, data, table_name):
        """Write pandas DataFrame to PostgreSQL."""
        connection = psycopg2.connect(**self.db_config)
        cursor = connection.cursor()
        try:
            for _, row in data.iterrows():
                cursor.execute(
                    f"""
                    INSERT INTO {table_name} (date_time, open, high, low, close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (date_time) DO NOTHING
                    """,
                    (row['date_time'], row['Open'], row['High'], row['Low'], row['Close'], row['Volume'])
                )
            connection.commit()
            logging.info("Data successfully written to database.")
        except Exception as e:
            logging.error(f"Failed to write data to database: {str(e)}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def fetch_from_db(self, symbol, start_date, end_date, table_name):
        """Fetch historical data from PostgreSQL."""
        connection = psycopg2.connect(**self.db_config)
        query = f"""
            SELECT date_time, open, high, low, close, volume
            FROM {table_name}
            WHERE symbol = %s AND date_time BETWEEN %s AND %s
            ORDER BY date_time ASC
        """
        try:
            data = pd.read_sql(query, connection, params=(symbol, start_date, end_date))
            logging.info("Data successfully fetched from database.")
            return data
        except Exception as e:
            logging.error(f"Failed to fetch data from database: {str(e)}")
            raise
        finally:
            connection.close()

import sqlite3
from sqlite3 import Error
import pandas as pd

csv_data = pd.read_csv("data/country_capitals.csv")
csv_data.columns = csv_data.columns.str.strip()


def fetch_sql_db():
    connection = None
    try:
        connection = sqlite3.connect(
            "data/country_capitals.db")
        # print("Connection to DB Successful")
    except Error as e:
        print(f"Error: {e} has occured")

    csv_data.to_sql("game_data", connection, if_exists="replace")
    cursor = connection.cursor()
    cursor.execute("select country,capital from game_data")
    country_city_pair = cursor.fetchall()

    return country_city_pair


country_capital_data = fetch_sql_db()

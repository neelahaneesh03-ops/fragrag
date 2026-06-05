import pandas as pd
from app.db_connection import get_connection

def insert_data_from_csv():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('/Users/haneesh/Documents/fragrag/data/cleaned_fra_perfumes.csv')

    # Establish a connection to the database
    conn = get_connection()
    with conn.cursor() as cur:
        rows = [
            (
                row['Name'],
                row['Gender'],
                row['Rating Value'],
                row['Rating Count'],
                row['Main Accords'],
                row['Description'],
                row['url']
            )
            for _, row in df.iterrows()
        ]
        cur.executemany("""
            INSERT INTO fragrances (name, gender, rating_value, rating_count, main_accords, description, URL)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, rows)
    conn.commit()
    conn.close()
    print("Data inserted successfully!")

if __name__ == "__main__":
    insert_data_from_csv()
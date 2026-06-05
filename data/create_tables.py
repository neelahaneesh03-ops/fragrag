import os
import psycopg
from app.db_connection import get_connection

conn = get_connection()

cur = conn.execute("""CREATE TABLE IF NOT EXISTS fragrances(
            id SERIAL PRIMARY KEY,
            name TEXT,
            gender TEXT,
            rating_value FLOAT,
            rating_count INTEGER,
            main_accords TEXT,
            description TEXT,
            URL TEXT,
            embeddings vector(384)
            )""")
            
conn.commit()
conn.close()
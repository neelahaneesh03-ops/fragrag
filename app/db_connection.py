import os
from dotenv import load_dotenv
import psycopg

# Load environment variables from .env file
load_dotenv()
def get_connection():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg.connect(os.getenv("DATABASE_URL"))
        return conn

    except Exception as e:
        print(f"Database connection failed: {e}")
        raise

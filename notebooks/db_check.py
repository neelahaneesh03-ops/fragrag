import os
from dotenv import load_dotenv
import psycopg
from google import genai

# Load environment variables from .env file
load_dotenv()
def check_database_connection():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg.connect(os.getenv("DATABASE_URL"))
        print("Database connection successful!")
        conn.close()
    except Exception as e:
        print(f"Database connection failed: {e}")

check_database_connection()

def check_gemini_api():
    try:
        # Initialize the Gemini API client
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        print("Gemini API key is valid!")
    except Exception as e:
        print(f"Gemini API key validation failed: {e}") 


check_gemini_api()

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def fetch_data():
    # Use your actual table name here
    response = supabase.table("eagles_offense").select("*").execute()

    # Print raw response if needed
    print("Raw response:", response)

    # Get the data
    data = response.data

    if not data:
        print("⚠️ No data found or query returned empty.")
    else:
        print("✅ Data fetched:")
        for row in data:
            print(row)



if __name__ == "__main__":
    fetch_data()

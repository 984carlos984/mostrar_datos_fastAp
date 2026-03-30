import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

URL: str = os.getenv("SUPABASE_URL")
KEY: str = os.getenv("SUPABASE_KEY")

if URL and KEY and not URL.startswith("https://reemplazame"):
    try:
        supabase: Client = create_client(URL, KEY)
    except Exception as e:
        print(f"Error inicializando Supabase: {e}")
        supabase = None
else:
    supabase = None

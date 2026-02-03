
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = None

if url and key:
    supabase = create_client(url, key)

def save_analysis(vision_data, cost_estimates=None, business_classification=None):
    """
    Saves the analysis results to a Supabase table named 'analyses'.
    """
    if not supabase:
        print("Supabase client not initialized. Check URL and Key.")
        return None

    try:
        data = {
            "room_type": vision_data.get("room_type"),
            "style_guess": vision_data.get("style_guess"),
            "vision_data": vision_data,
            "cost_estimates": cost_estimates,
            "business_classification": business_classification
        }
        
        # Insert into 'analyses' table
        response = supabase.table("analyses").insert(data).execute()
        print(f"✅ SUCCESS: Analysis for {data.get('room_type')} synced to Supabase.")
        return response
    except Exception as e:
        print(f"❌ ERROR: Failed to sync to Supabase: {e}")
        return None

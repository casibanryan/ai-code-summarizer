import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"Checking API Key... {'Found (Starts with ' + api_key[:6] + ')' if api_key else 'NOT FOUND'}")

if not api_key:
  print("❌ Error: GEMINI_API_KEY is missing from your environment variables!")
  exit()

try:
  print("Connecting to Gemini Gateway...")
  client = genai.Client()
  response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say 'API connection verified!'"
)
  print(f"🎉 Success! Response: {response.text}")

except APIError as e:
  print(f"\n❌ Google API Error: Status {e.code}")
  print(f"Message: {e.message}")
except Exception as e:
  print(f"\n❌ System/Network Error: {e}")
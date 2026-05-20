import os
from google import genai
from google.genai.errors import APIError
from dotenv import load_dotenv

load_dotenv()

class CodeAnalyzer:
  def __init__(self):
    if not os.getenv("GEMINI_API_KEY") and not os.getenv("GOOGLE_API_KEY"):
      raise ValueError("Missing API Key! Please ensure GEMINI_API_KEY is configured inside your .env file.")
        
    self.client = genai.Client()
    self.model_name = "gemini-2.5-flash"  

  def generate_summary(self, filename: str, code: str) -> str:
    # Craft a highly strict prompt telling the model exactly what output layout we expect
    prompt = (
        f"You are a Senior Software Engineer. Provide a concise, professional markdown review "
        f"for the following Python file: '{filename}'.\n\n"
        f"Structure your response exactly with these headers:\n"
        f"### 📋 Overview\n(Briefly explain what this file does)\n"
        f"### ⚙️ Core Functions/Classes\n(Bulleted list of key classes and methods with single-sentence descriptions)\n"
        f"### 📦 Dependencies\n(List imported modules or external libraries used)\n"
    )

    try:
      # Execute the stateless content generation API call
      response = self.client.models.generate_content(
          model=self.model_name,
          contents=f"{prompt}\n\n```python\n{code}\n```"
      )
      return response.text if response.text else "Warning: Model returned an empty text payload."

    except APIError as e:
      # Catches explicit Google API failures (invalid credentials, quota limits, blocked requests)
      print(f"⚠️ API Error analyzing {filename}: Status {e.code} - {e.message}")
      return "Analysis failed: A Google API error occurred."
      
    except Exception as e:
      # Fallback for unexpected system/network connectivity interruptions
      print(f"⚠️ Unexpected network/system error analyzing {filename}: {e}")
      return "Analysis failed: System or connection failure."
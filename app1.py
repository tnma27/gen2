from google import genai
from config import API

client=genai.Client(api_key=API)

response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents="python vs java"
)
print(response.text)
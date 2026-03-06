from google import genai
from dotenv import load_dotenv

load_dotenv()   

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="what color is orange? answer in one word",
)

print(response.text)
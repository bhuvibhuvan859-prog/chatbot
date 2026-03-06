from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os
import json

# Load .env from the parent directory (c:\chatbot\chatbot\.env)
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def index(request):
    return render(request, "index.html")


@csrf_exempt
def generate(request):
    if request.method == "POST":
        data = json.loads(request.body)
        prompt = data.get("prompt")

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return JsonResponse({"response": response.text})
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable not set.")

client = Groq(api_key=api_key)

# Groq doesn't have a list_models endpoint like Gemini
# Instead, we'll show the available models from Groq's documentation
print("Available Groq models:")
print("- llama-3.3-70b-versatile")
print("- llama-3.1-70b-versatile")
print("- llama-3.1-8b-instant")
print("- mixtral-8x7b-32768")
print("- gemma2-9b-it")
print("\nCurrent model in use: llama-3.3-70b-versatile")

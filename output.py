from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import openai
import google.generativeai as genai
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

load_dotenv()

from main import *

result=input

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

system = """You are given a detailed n-day travel itinerary for Bangalore. Your task is to extract and list only the locations mentioned, categorized by the day. 
Make sure to omit any descriptions, reasons, prices, or other details. Focus strictly on the location names based on the day."""

def get_gemini_responses(input_text, system_prompt):
    # Combine the system prompt and input text
    combined_input = f"{system_prompt}\n\nInput: {input_text}"
    response = model.generate_content(combined_input)
    return response.text

result = get_gemini_responses(input, system)
print(result)



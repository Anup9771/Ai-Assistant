import google.generativeai as genai
import os

# API key set karo (agar env variable set nahi hai to direct bhi likh sakte ho)
genai.configure(api_key="AIzaSyA-1YNnCeVbzqZXC9si-m_zaxJAZ3B9rf0")

# Gemini model select karo
model = genai.GenerativeModel("gemini-1.5-flash")

# Prompt bhejo
response = model.generate_content("Hello Gemini, how are you?")

# Output print
print(response.text)
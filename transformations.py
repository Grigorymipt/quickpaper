import os
from send_to_ChatGPT import get_openai_response

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("API key not found. Please set the OPENAI_API_KEY environment variable.")
    exit(1)

def transformation(text):
    if len(text) < 20:
        return text
    else:
        prompts = open("prompts.txt", 'r').readlines()
        prompt = prompts[0]
        prompt += text
        response = get_openai_response(api_key, model="gpt-4o-mini", user_message=prompt+text)
        return response

def upper_transformation(text):
    text = text.upper()
    return text

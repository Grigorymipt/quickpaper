# openai_request.py
import requests
import os
import json

def get_openai_response(api_key, model="gpt-4o", user_message="Write a one-sentence bedtime story about a unicorn."):
    """
    Function to interact with the OpenAI API and get a response.

    :param api_key: OpenAI API key.
    :param model: The model to use for completion (default: gpt-4o).
    :param user_message: The message sent to the model (default: bedtime story prompt).
    :return: The generated response from OpenAI.
    """
    # Define the endpoint URL
    url = "https://api.openai.com/v1/chat/completions"

    # Prepare the request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare the payload
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON and return the content
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"


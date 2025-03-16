# openai_request.py
import requests
import os
import json
import aiohttp
import asyncio

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

async def get_openai_response_async(api_key, model="gpt-4o", user_message="Write a one-sentence bedtime story about a unicorn."):
    """
    Asynchronous function to interact with the OpenAI API and get a response.

    :param api_key: OpenAI API key.
    :param model: The model to use for completion (default: gpt-4o).
    :param user_message: The message sent to the model (default: bedtime story prompt).
    :return: The generated response from OpenAI.
    """
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    try:
        # Asynchronous POST request using aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                response.raise_for_status()  # Raise an exception for bad responses (4xx/5xx)

                # Parse the response JSON
                result = await response.json()
                return result['choices'][0]['message']['content']

    except aiohttp.ClientError as e:
        # Handle any errors during the request (e.g., network issues, invalid API key)
        return f"Request failed: {str(e)}"
    except KeyError:
        # Handle if the expected response structure is not present
        return "Error: Unexpected response structure from OpenAI API."

# Example of how to use the function with asyncio
async def main():
    api_key = "your-openai-api-key-here"  # Replace with your actual API key
    response = await get_openai_response(api_key, user_message="Tell me a joke about a robot.")
    print(response)

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())

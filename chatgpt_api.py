import requests

api_key = '# Replace with your actual API key'  
api_endpoint = 'https://api.openai.com/v1/engines/davinci/completions'

def generate_response(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'prompt': prompt,
        'max_tokens': 50  # Adjust as needed
    }

    response = requests.post(api_endpoint, json=data, headers=headers)
    response_data = response.json()

    return response_data['choices'][0]['text']

def main():
    prompt = input("Enter your prompt: ")
    response = generate_response(prompt)
    print("Response:", response)

if __name__ == "__main__":
    main()
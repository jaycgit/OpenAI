from flask import Flask, request, render_template, jsonify
import openai
from capture_speech import capture_speech  # Import capture_speech function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-to-chatgpt', methods=['POST'])
def send_to_chatgpt():
    try:
        # Define a list of prompts to test
        prompts_to_test = [
            "What is the weather today?",
            "Tell me a joke.",
            "Open the door.",
            "Set a timer for 5 minutes.",
            # Add more prompts to test as needed
        ]

        # Capture speech and convert it to text
        recognized_text = capture_speech()

        if recognized_text:
            # Initialize OpenAI API client (replace with your API key)
            openai.api_key = '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'

            # Choose a prompt from the list
            # You can also randomly select a prompt or choose based on user input
            prompt = prompts_to_test[0]  # Change the index to test different prompts

            # Send recognized text to ChatGPT API using the selected prompt
            response = openai.Completion.create(
                engine="davinci",
                prompt=f"{prompt} {recognized_text}",
                max_tokens=50,  # Adjust as needed
                n=1,  # Number of responses
                stop=None,  # Optional stop criteria
            )

            # Extract the generated response
            chatgpt_response = response.choices[0].text

            return jsonify({'chatgpt_response': chatgpt_response})
        else:
            return jsonify({'chatgpt_response': 'Speech recognition failed.'})

    except Exception as e:
        # Log any exceptions or errors
        print(f'Error occurred: {str(e)}')
        return jsonify({'error': 'An error occurred'})

if __name__ == '__main__':
    app.run()

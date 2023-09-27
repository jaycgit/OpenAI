# Author: Jay Crispo
# Description: Flask app for sending speech to ChatGPT using OpenAI's GPT-3.
#Generated with assistance from ChatGPT
# Date: 9/21/2023


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
        # Capture speech and convert it to text
        recognized_text = capture_speech()

        if recognized_text:
            # Initialize OpenAI API client (replace with your API key)
            openai.api_key = 'your OpenAI API key'

            # Send recognized text to ChatGPT API without a fixed prompt
            response = openai.Completion.create(
                engine="curie",  # Change the engine to "curie"
                prompt=recognized_text,  # Use recognized_text as the prompt
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

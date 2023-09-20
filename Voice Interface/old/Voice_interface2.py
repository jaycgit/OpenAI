from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-to-chatgpt', methods=['POST'])
def send_to_chatgpt():
    recognized_text = request.form['recognizedText']

    # Initialize OpenAI API client (replace with your API key)
    openai.api_key = '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'

    # Send recognized text to ChatGPT API
    response = openai.Completion.create(
        engine="davinci",
        prompt=recognized_text,
        max_tokens=50,  # Adjust as needed
        n=1,  # Number of responses
        stop=None,  # Optional stop criteria
    )

    # Extract the generated response
    chatgpt_response = response.choices[0].text

    return jsonify({'chatgpt_response': chatgpt_response})

if __name__ == '__main__':
    app.run()

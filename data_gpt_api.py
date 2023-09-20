from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.json.get('what is the capital of france', '')
    response = generate_response(user_query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

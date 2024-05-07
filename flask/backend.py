from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

# Function to get Gemini response
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return [chunk.text for chunk in response]

# Define endpoint for chat request
@app.route('/api/chat', methods=['POST', 'GET'])
def chat_endpoint():
    if request.method == 'POST':
        data = request.get_json(force=True)  # Ignore Content-Type header
        question = data.get('question')
    elif request.method == 'GET':
        question = request.args.get('question')
    else:
        return jsonify({'error': 'Method not allowed'}), 405

    if not question:
        return jsonify({'error': 'Question not provided'}), 400

    response = get_gemini_response(question)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

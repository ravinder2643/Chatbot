# Chatbot Backend

This is the backend for the chatbot application. It provides an API for interacting with the chatbot model and handling user requests.

## Setup

1. Clone this repository to your local machine:

git clone <repository-url>

2. Navigate to the `backend` directory:

cd backend

3. Install the required dependencies:

pip install -r requirements.txt

4. Set up your environment variables by creating a `.env` file in the `backend` directory and adding your Google API key:

GOOGLE_API_KEY=<your-api-key>

## Usage

1. Start the Flask server:

python backend.py

This will start the Flask server on `http://localhost:5000`.

2. Your backend is now ready to handle requests from the frontend.

## API Endpoints

- `/api/chat`:
- **Method**: POST
- **Description**: Send a question to the chatbot and receive a response.
- **Request Body**: JSON object with a `question` parameter.
- **Response**: JSON object with a `response` parameter containing the chatbot's response.

## Environment Variables

- `GOOGLE_API_KEY`: Your Google API key for accessing the chatbot model.

# Chatbot Frontend

This is the frontend for the chatbot application. It provides a user interface for interacting with the chatbot backend.

## Setup

1. Clone this repository to your local machine:

git clone <repository-url>

2. Navigate to the `frontend` directory:

cd frontend

3. Install the required dependencies:

npm install


## Usage

1. Start the React development server:

npm start

This will start the development server on `http://localhost:3000`.

2. Open your web browser and navigate to `http://localhost:3000` to access the chatbot interface.

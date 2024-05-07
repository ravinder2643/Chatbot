import { useState } from 'react';
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const sendQuestion = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: question })
      });
      const data = await response.json();
      setResponse(data.response);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="app-container">
      <div className="chatbot-container">
        <div className="chatbot-popup">
          <div className="chatbot-input">
            <textarea
              value={response}
              readOnly
              placeholder="Chatbot response..."
            ></textarea>
            <input
              type="text"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Ask a question..."
            />
            <button onClick={sendQuestion}>Ask</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

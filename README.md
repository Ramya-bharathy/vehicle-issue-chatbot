 Vehicle Issue Diagnosing Chatbot
A smart AI-powered chatbot that helps users identify root causes of vehicle issues using the 5 Why Analysis method. Built with Python, Flask, and integrated with Mistral AI, this chatbot offers insightful diagnostics and solutions in a conversational interface.

🔧 Features

Takes user input describing a car problem
Uses Mistral AI to perform 5 Why Analysis
Identifies the root cause and offers a solution
Web-based interface for easy interaction
Built with Flask and JavaScript for frontend/backend flow

🧠 How It Works

User enters a car-related issue (e.g., "My car won't start")
The chatbot sends this to a Flask backend
Flask calls Mistral AI with a diagnostic prompt
AI responds with a step-by-step 5 Why breakdown
Result is displayed on the web page

📁 Project Structure

Copy
Edit
vehicle-issue-chatbot/
│
├── chatbot.py          # Flask app with Mistral AI integration  
├── templates/
│   └── index.html      # Frontend interface for the chatbot

🚀 Getting Started
1. Clone the Repository
Copy
Edit
git clone https://github.com/your-username/vehicle-issue-chatbot.git
cd vehicle-issue-chatbot

2. Install Dependencies
Copy
Edit
pip install flask requests

3. Add Your Mistral API Key
In chatbot.py, replace the placeholder key:
python
Copy
Edit
MISTRAL_API_KEY = "your_api_key_here"

4. Run the App
bash
Copy
Edit
python chatbot.py
Then go to http://127.0.0.1:5000 in your browser to chat with your vehicle assistant 🚘

📌 Example Query
User: My engine is overheating
AI Response:
1️⃣ First Why: The engine temperature is rising abnormally.
2️⃣ Second Why: The coolant level is low.
...
✅ Solution: Refill coolant and check for radiator leaks.


🧑‍💻 Built With

Python 🐍
Flask 🔥
Mistral AI 🧠
HTML + JavaScript

🙌 Acknowledgments
This project was built as a beginner-level AI-integrated web application to explore Flask, APIs, and logical root cause analysis using 5 Whys.

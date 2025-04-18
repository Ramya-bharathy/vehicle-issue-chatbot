from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Mistral API Configuration
MISTRAL_API_KEY = "DYsiSG8EVkuNCOugxEHrjRwKEsB7ujMn"  # Replace with your Mistral API Key
MISTRAL_MODEL = "mistral-small"

# Function to get vehicle diagnostics from Mistral AI
def get_vehicle_solution(user_input):
    url = "https://api.mistral.ai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # AI-powered 5 Why Analysis Prompt
    prompt = f"""
    You are an expert vehicle diagnostics assistant.
    Use the **5 Why Analysis** method to find the root cause of the issue and provide a solution.
    
    Problem: {user_input}
    
    Step 1: Ask 'Why did this happen?' and answer.
    Step 2: Ask 'Why?' again to go deeper.
    Step 3: Continue asking 'Why?' until you reach the root cause.
    Step 4: Once the root cause is identified, provide a **detailed solution**.

    Your response should follow this structure:
    
    1️⃣ **First Why:** (Analysis)
    2️⃣ **Second Why:** (Deeper Analysis)
    3️⃣ **Third Why:** (Further Root Cause Exploration)
    4️⃣ **Fourth Why:** (Narrowing Down the Issue)
    5️⃣ **Final Why:** (Root Cause Identified)
    ✅ **Solution:** (Provide a fix for the issue)
    """

    payload = {
        "model": MISTRAL_MODEL,
        "messages": [
            {"role": "system", "content": "You are an AI car diagnostic expert that uses the 5 Why Analysis to detect and fix vehicle problems."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.json()}"

# Route for Chatbot UI
@app.route('/')
def home():
    return render_template("index.html")

# API Route for handling chatbot requests
@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Please provide a vehicle issue description."}), 400
    
    solution = get_vehicle_solution(user_query)
    return jsonify({"response": solution})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset
with open('faq.json', encoding='utf-8') as f:
    data = json.load(f)

questions = [item['question'] for item in data]
answers = [item['answer'] for item in data]

# NLP model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(user_input):
    user_input = user_input.lower()

    # Greeting responses
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    
    if any(word in user_input for word in greetings):
        return "Hello! How can I assist you today?"

    # NLP matching
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    max_score = similarity.max()

    if max_score < 0.3:
        return "Sorry, I didn't understand that. Please try another question."

    index = similarity.argmax()
    return answers[index]

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_input = data.get('message', '')
    print("User:", user_input)  # Debug

    response = get_response(user_input)
    print("Bot:", response)     # Debug

    return jsonify({"response": response})

# Run app
if __name__ == '__main__':
    app.run(debug=True)
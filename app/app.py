from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

# Load saved vectorizer and model
with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf_vectorizer = pickle.load(f)

with open("Sentiment_model.pkl", "rb") as f:
    sentiment_model = pickle.load(f)

def predict_sentiment(text):
    text_features = tfidf_vectorizer.transform([text])
    prediction = sentiment_model.predict(text_features)
    return "Positive" if prediction == 4 else "Negative"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_input = data.get('text', '')
    result = predict_sentiment(user_input)
    return jsonify({'sentiment': result})

if __name__ == "__main__":
    app.run(debug=True)

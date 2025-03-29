# Sentiment Analysis App
This project is a web-based sentiment analysis application that predicts the sentiment (Positive or Negative) of a given text input. Built using Flask for the backend and a Machine Learning model trained on sentiment data, it aims to classify user inputs as having a positive or negative sentiment.

The app leverages TF-IDF vectorization to convert text data into numerical features and uses a pre-trained Logistic Regression model to make predictions.

### 💻 Technologies Used
1)Python: Backend and ML model development

2)Flask: Web framework for building the application

3)Scikit-learn: Model training and evaluation

4)TF-IDF Vectorizer: Feature extraction from text data

5)HTML & CSS: Frontend interface

6)Bootstrap: Styling and responsive design

7)Pickle: Model and vectorizer persistence


### 🛠️ Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/yourusername/sentiment-analysis-app.git
cd sentiment-analysis-app
Create a Virtual Environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask App:

bash
Copy
Edit
python app.py
Access the Application:
Open your browser and navigate to http://127.0.0.1:5000/

### 🚀 Usage
Open the web app.
Enter a text input that you want to analyze.

Click on "Analyze Sentiment" to get the prediction.

The predicted sentiment (Positive or Negative) will be displayed on the screen.


📊 Example Outputs

✅ Positive Sentiment:

"I love this product!" → Positive

"Amazing experience and great quality!" → Positive


❌ Negative Sentiment:

"This is the worst experience ever." → Negative

"I hate this product!" → Negative



##   Known Limitations and Challenges
Despite achieving satisfactory performance on common sentiment phrases, the model has some limitations:

1) Inconsistent Predictions:
Some phrases that express negativity are incorrectly labeled as positive, such as:

i)"I hate this product!" → Positive

ii)"This is the worst experience ever." → Positive


Ambiguous Phrases:
Phrases that include negations or mixed sentiments may yield incorrect predictions, like:

i) "I do not like him." → Positive

ii) "Hate to prefer it." → Positive



#### 📝 Reasons for Inaccuracy:

Data Imbalance: The training data might be biased towards positive sentiment.

Feature Extraction Limitation: TF-IDF fails to capture contextual information and negation properly.

Model Complexity: Logistic Regression might not fully grasp complex sentiment patterns.



#### 💡 Suggestions for Improvement:

1)Use Advanced NLP Models like BERT or GPT-based models.

2)Implement Data Augmentation to balance positive and negative samples.

3)Explore Word Embeddings (Word2Vec or GloVe) for richer feature extraction.

4)Fine-tune the model on more diverse and balanced datasets.

##  Future Improvements

- Integrate more advanced models such as LSTM or Transformers for improved accuracy.
- 
-Add a feedback loop to allow users to mark incorrect predictions and help retrain the model.

-Incorporate topic modeling to identify contextual biases.

-Improve the user interface with interactive elements and sentiment trend visualization.



🤝 Contributing

Contributions are welcome! If you want to add features or improve the model, feel free to submit a pull request. Please ensure your code follows proper formatting and includes relevant documentation.



📄 License

This project is licensed under the MIT License.

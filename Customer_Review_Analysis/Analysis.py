from flask import Flask, request, jsonify, render_template 
import pandas as pd

app = Flask(__name__)

# Sample words for sentiment analysis (this can be expanded)
POSITIVE_WORDS = {'good', 'great', 'excellent', 'love', 'amazing', 'fantastic', 'happy', 'positive'}
NEGATIVE_WORDS = {'bad', 'terrible', 'hate', 'awful', 'sad', 'negative', 'worst', 'disappointing'}

def analyze_sentiment(review_text):
    words = review_text.lower().split()
    positive_count = sum(1 for word in words if word in POSITIVE_WORDS)
    negative_count = sum(1 for word in words if word in NEGATIVE_WORDS)
    neutral_count = len(words) - (positive_count + negative_count)
    return positive_count, negative_count, neutral_count

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.filename.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

        if 'review' not in df.columns:
            return jsonify({"error": "Missing 'review' column in file"}), 400

        positive_score, negative_score, neutral_score = 0, 0, 0

        for review in df['review']:
            pos, neg, neu = analyze_sentiment(review)
            positive_score += pos
            negative_score += neg
            neutral_score += neu

        total_reviews = len(df)
        response = {
            "positive": positive_score / total_reviews if total_reviews > 0 else 0,
            "negative": negative_score / total_reviews if total_reviews > 0 else 0,
            "neutral": neutral_score / total_reviews if total_reviews > 0 else 0
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

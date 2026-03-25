from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy AI prediction function
def predict(text):
    if "good" in text.lower() or "amazing" in text.lower():
        return "Positive"
    return "Negative"

@app.route("/")
def home():
    return "Backend running!"

@app.route("/predict", methods=["POST"])
def get_prediction():
    data = request.get_json()
    text = data.get("text", "")
    
    prediction = predict(text)
    
    return jsonify({
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)

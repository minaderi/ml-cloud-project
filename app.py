from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Örnek veri
data = {
    "temperature": [30, 22, 35, 28, 18, 40, 25, 33],
    "humidity": [70, 40, 80, 65, 30, 90, 50, 75],
    "traffic": ["high", "low", "high", "medium", "low", "high", "medium", "high"]
}

df = pd.DataFrame(data)

df["traffic"] = df["traffic"].map({
    "low": 0,
    "medium": 1,
    "high": 2
})

X = df[["temperature", "humidity"]]
y = df["traffic"]

model = RandomForestClassifier()
model.fit(X, y)

labels = {
    0: "low",
    1: "medium",
    2: "high"
}

@app.route("/")
def home():
    return "ML Traffic Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    temperature = data["temperature"]
    humidity = data["humidity"]

    prediction = model.predict([[temperature, humidity]])

    result = labels[prediction[0]]

    return jsonify({
        "prediction": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
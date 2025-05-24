from flask import Flask, request, render_template
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('models/XGBoost.pkl', 'rb'))

# Crop indices mapping
crop_indices = {
    "Soyabeans": 0,
    "Apple": 1,
    "Banana": 2,
    "Beans": 3,
    "Coffee": 4,
    "Cotton": 5,
    "Cowpeas": 6,
    "Grapes": 7,
    "Groundnuts": 8,
    "Maize": 9,
    "Mango": 10,
    "Orange": 11,
    "Peas": 12,
    "Rice": 13,
    "Watermelon": 14
}

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    # Get form inputs
    N = int(request.form.get('Nitrogen', 0))
    P = int(request.form.get('Phosphorus', 0))  # fixed typo
    K = int(request.form.get('Potassium', 0))
    ph = float(request.form.get('pH', 0.0))
    rainfall = float(request.form.get('Rainfall', 0.0))
    temperature = float(request.form.get('Temperature', 0.0))
    humidity = float(request.form.get('Humidity', 0.0))

    # Prepare features for prediction
    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # Predict
    prediction_index = model.predict(data)[0]

    # Reverse lookup the crop name
    predicted_crop = next((crop for crop, idx in crop_indices.items() if idx == prediction_index), "Unknown")

    return render_template('index.html', result=predicted_crop)

if __name__ == "__main__":
    app.run(debug=True)

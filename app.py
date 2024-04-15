from flask import Flask,request,render_template
import numpy as np
import pandas
import sklearn
import pickle

# importing model
model = pickle.load(open('models/RandomForest.pkl', 'rb'))
#sc = pickle.load(open('standscaler.pkl', 'rb'))
#ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# creating flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    # Collect input values from the form
    N = int(request.form.get('Nitrogen', 0))  # Default value if key is missing
    P = int(request.form.get('Phosporus', 0))
    K = int(request.form.get('Potassium', 0))
    ph = float(request.form.get('pH', 0.0))
    rainfall = float(request.form.get('Rainfall', 0.0))
    temperature = float(request.form.get('Temperature', 0.0))
    humidity = float(request.form.get('Humidity', 0.0))

    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    my_prediction = model.predict(data)
    final_prediction = my_prediction[0]

    # Create a feature vector with numeric values
    #feature_list = [N, P, K, temperature, humidity, ph, rainfall]
    #single_pred = np.array(feature_list).reshape(1, -1)

    # Make prediction using the model
    #prediction = model.predict(single_pred)

    # Map prediction to crop name
    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    # Display result
    """if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated right there".format(crop)
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
"""
    return render_template('index.html', result=final_prediction)



# python main
if __name__ == "__main__":
    app.run(debug=True)
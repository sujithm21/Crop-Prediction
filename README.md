# Crop Prediction Flask App

## Description
This project implements a Flask web application for predicting the best crop to be cultivated based on input parameters such as soil nutrient levels, environmental conditions (temperature, humidity, rainfall), and pH level. The prediction is made using a Random Forest classifier trained on agricultural data.

## Features
- User-friendly web interface for inputting crop parameters
- Prediction of the best crop to be cultivated based on input data
- Mapping of prediction results to crop names for easy interpretation

## Installation
1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Make sure you have Python and Flask installed on your system.

## Usage
1. Run the application using `python app.py`.
2. Open your web browser and navigate to `http://localhost:5000`.
3. Input the soil nutrient levels, environmental conditions, and pH level.
4. Click on the "Predict" button to see the predicted crop.

## Contributing
Contributions are welcome! Please follow the guidelines in CONTRIBUTING.md.

## Credits
- Flask
- scikit-learn
- pandas
- numpy

## License
This project is licensed under the [MIT License](LICENSE).

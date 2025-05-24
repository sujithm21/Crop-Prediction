# Crop Recommendation System

## Overview
This project is a Crop Recommendation System designed to help users determine the best crops to cultivate based on various environmental factors. The application utilizes user inputs such as nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall to provide crop recommendations.

## Project Structure
```
ds355-project
├── static
│   └── styles.css        # Contains CSS styles for the project, including 3D effects and animations.
├── templates
│   └── index.html        # Main HTML template for the application with 3D elements.
└── README.md             # Documentation for the project.
```

## Features
- User-friendly interface for inputting environmental data.
- Real-time crop recommendations based on user inputs.
- Enhanced UI with 3D effects and animations for a more engaging experience.
- Utilization of CSS 3D transforms and shadows to create depth in the UI.
- Potential integration of libraries like Three.js for advanced 3D graphics.

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ds355-project
   ```

2. **Install dependencies:**
   Ensure you have Python and Flask installed. You can install Flask using pip:
   ```
   pip install Flask
   ```

3. **Run the application:**
   Start the Flask server:
   ```
   python app.py
   ```
   Access the application in your web browser at `http://127.0.0.1:5000`.

## UI Enhancements
The user interface has been designed to be visually appealing with the following enhancements:
- **3D Effects:** CSS 3D transforms are applied to various elements to create a sense of depth.
- **Animations:** Smooth transitions and animations enhance user interaction.
- **Responsive Design:** The layout adapts to different screen sizes for optimal usability.

## Future Improvements
- Explore additional 3D libraries for more complex visualizations.
- Implement user authentication for personalized recommendations.
- Expand the dataset for more accurate crop predictions.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
# Image Classification Web App using Flask and TensorFlow

This project implements a web application that classifies images using a deep learning model trained on the **CIFAR-10 dataset**. The app allows users to upload an image, and it predicts the class of the image using a **TensorFlow** model served by a **Flask** web server

## Features
- **Image Upload**: Upload images to be classified
- **Prediction**: The model predicts the class of the uploaded image (e.g., Airplane, Dog, Horse, etc.)
- **Web Interface**: Simple and responsive Flask-based interface
- **Machine Learning Model**: Pre-trained CNN model using TensorFlow, based on the CIFAR-10 dataset

## Technologies Used
- **Python**: The main programming language.
- **TensorFlow**: For building and training the deep learning model
- **Flask**: For creating the web application and handling user interactions
- **Pillow (PIL)**: For image processing
- **HTML/CSS**: For the front-end design

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/image-classification-app.git
   cd image-classification-app

2. **Install required dependencies: Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
   Install the dependencies from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Train the model (if not already done): If you don’t have the pre-trained model (saved_model.h5), run the model.py script to train and save the model**:
   ```bash
   python model.py
   ```
   
5. **Run the Flask app: To start the Flask server and access the app, run**:
   ```bash
   python app.py
   ```
   The app will be available at http://127.0.0.1:5000 in your browser

## Usage
Open the app in your browser
Upload an image (JPEG, PNG, etc.)
The app will classify the image and display the predicted class (e.g., Horse, Airplane)

## Example Output
After uploading an image, the app will display:

```vbnet
Predicted class: Horse (Class 7)
```
## Model Details
-**Dataset**: The app uses the CIFAR-10 dataset, which contains 60,000 32x32 color images in 10 classes.
-**Model**: The model is a Convolutional Neural Network (CNN) trained on CIFAR-10.
-**Classes**:
-- Airplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship, Truck.

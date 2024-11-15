from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

app = Flask(__name__)
model = load_model('saved_model.h5')  # Load the trained model

# Class names for CIFAR-10
class_names = {
    0: "Airplane",
    1: "Automobile",
    2: "Bird",
    3: "Cat",
    4: "Deer",
    5: "Dog",
    6: "Frog",
    7: "Horse",
    8: "Ship",
    9: "Truck"
}

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Preprocess the uploaded image
            image = Image.open(file).resize((32, 32))  # Resize to match model input
            image = img_to_array(image) / 255.0
            image = np.expand_dims(image, axis=0)

            # Predict the class
            prediction = model.predict(image)
            predicted_class = np.argmax(prediction)  # Predicted class number
            predicted_class_name = class_names[predicted_class]  # Map to class name

            # Return result
            return f"Predicted class: {predicted_class_name} (Class {predicted_class})"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Load the trained model
model = load_model('saved_model.h5')

# Function to predict a single image
def predict_image(image_path):
    image = Image.open(image_path).resize((32, 32))
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)
    print(f"Predicted class: {predicted_class}")

# Test with an image
predict_image('path_to_your_image.jpg')


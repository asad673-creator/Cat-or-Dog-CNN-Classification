from PIL import Image
import numpy as np
import joblib

# Load CNN model
model =joblib.load('cnn_model.pkl')

# Ask user for image
image_path = input("Enter the path of the cat or dog image: ")

# Open and resize image
image = Image.open(image_path).convert("RGB")
image = image.resize((256, 256))

# Convert image to numpy array
image = np.array(image)

# Normalize pixels
image = image / 255.0

# Reshape for CNN
image = image.reshape(1, 256, 256, 3)

# Predict
prediction = model.predict(image)

# Display result
if prediction[0] > 0.5:
    print("Prediction: Dog 🐶")
else:
    print("Prediction: Cat 🐱")


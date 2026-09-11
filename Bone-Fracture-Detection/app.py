import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

st.title("Bone Fracture Detection")

@st.cache_resource
def load_my_model():
    return load_model("bone-fracture.keras")

model = load_my_model()

uploaded_file = st.file_uploader(
    "Upload X-Ray Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    img = Image.open(uploaded_file)

    st.image(img, caption="Uploaded X-Ray", width=400)

    img = img.resize((256, 256))
    img = img.convert("RGB")

    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    if st.button("Predict"):

        prediction = model.predict(img_array)

        if prediction[0][0] > 0.5:
            st.error("Fracture Detected")
        else:
            st.success("No Fracture Detected")

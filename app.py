import streamlit as st
import tempfile
import os  
from model_helper import predict

# Set page config
st.set_page_config(page_title="Car Damage Detector", page_icon="🚗", layout="centered")

# Styled header
st.markdown("""
    <div style="background-color:#e6f2ff; padding: 15px; border-radius: 12px;">
        <h1 style="
            color: #003366;
            text-align: center;
            margin: 0;
            font-size: 28px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        ">
            🚗 Car Damage Detector
        </h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("## 📸 Upload a vehicle image:")

# File uploader block
uploaded_file = st.file_uploader("Choose a vehicle image (JPG/PNG)", type=["jpg", "png"])

if uploaded_file:
    # Create a temporary file to save the image
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.getbuffer())
        temp_image_path = tmp.name

    # Display the uploaded image nicely
    st.image(uploaded_file, caption="Uploaded Vehicle Image", use_container_width=True)

    # Horizontal line separator
    st.markdown("---")

    if st.button("🔎 Predict Damage Class"):
        progress = st.progress(0, text="Analyzing image...")

        prediction = predict(temp_image_path)
        progress.progress(100, text="Prediction complete!")

        st.success(f"🚗 **Predicted Damage Class:** {prediction}")

        # Clean up temporary file after prediction
        try:
            os.remove(temp_image_path)
        except Exception as e:
            st.warning(f"Could not delete temporary file: {e}")

import streamlit as st
import joblib
import re

# Page configuration
st.set_page_config(
    page_title="Customer Support Intent Classifier",
    layout="centered"
)
st.markdown("""
<style>

/* Main background */
.stApp{
    background-color:#f5f7fe;
}

/* Title */
h1{
    color:#1f77b4;
    text-align:center;
}

/* Buttons */
.stButton > button{
    width:100%;
    background-color:#1f77b4;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton > button:hover{
    background-color:#0f5da6;
}

/* Text area */
textarea{
    border-radius:10px !important;
}

/* Success box */
.stAlert{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)
# Load model and vectorizer
model = joblib.load("models/best_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text


# Main Title
st.title("Customer Support Intent Classifier")

st.write(
    "Enter a customer support message and the model will predict its intent."
)

# Example queries
with st.expander("💡 Example Queries"):
    st.write("- My card has not arrived yet")
    st.write("- I forgot my PIN")
    st.write("- My refund has not been credited")
    st.write("- Cash withdrawal failed")
    st.write("- My account is locked")

# User Input
user_input = st.text_area(
    "Customer Message",
    placeholder="Example: My card has not arrived yet."
)

if st.button("Predict Intent"):

    if user_input.strip():

        cleaned = clean_text(user_input)

        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)[0]

        prediction = prediction.replace("_", " ").title()

        st.success(f"🎯 Predicted Intent: **{prediction}**")

    else:
        st.warning("Please enter a customer message.")
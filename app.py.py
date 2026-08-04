import streamlit as st
import pickle
import re

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load Model
model = load_model("models/lstm_model.keras")

# Load Tokenizer
with open("models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAX_LEN = 100

# Clean Text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

# Streamlit Page
st.set_page_config(
    page_title="Sentiment Analysis Using LSTM",
    page_icon="😊"
)

st.title("🎬 Sentiment Analysis Using LSTM")
st.write("Enter a movie review below and click Predict.")

review = st.text_area("Movie Review")

if st.button("Predict"):

    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        review = clean_text(review)

        sequence = tokenizer.texts_to_sequences([review])
        padded = pad_sequences(sequence, maxlen=MAX_LEN)

        prediction = model.predict(padded)[0][0]

        if prediction >= 0.5:
            st.success("😊 Positive Review")
            st.write(f"Confidence: {prediction*100:.2f}%")
        else:
            st.error("😞 Negative Review")
            st.write(f"Confidence: {(1-prediction)*100:.2f}%")
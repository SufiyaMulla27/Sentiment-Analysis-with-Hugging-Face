import streamlit as st
from transformers import pipeline

# Load model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)

# Streamlit App
st.title("Sentiment Analysis with Hugging Face")
user_input = st.text_area("Enter text")

if st.button("Analyze"):
    result = sentiment_pipeline(user_input)
    st.write(result)

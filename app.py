import streamlit as st
import joblib
model = joblib.load("sentiment-model.pkl")
sentiment_labels = {"1":"Positive", "0":"Negative"}
st.title("Sentiment Analysis")
user_input = st.text_area("Enter your text here:")

if st.button("Predict"):
    #print(user_input)
    predicted_sentiment = model.predict([user_input])[0]
    print("Predicted Label:" + str(predicted_sentiment))
    predicted_sentiment_label = sentiment_labels[str(predicted_sentiment)]
    #st.info(f"Predicted Sentiment:{predicted_sentiment_label}")
    st.info(predicted_sentiment_label)


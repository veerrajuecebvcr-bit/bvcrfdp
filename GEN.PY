import streamlit as st
import google.generativeai as genai

st.title("Google Generative AI with Streamlit")
st.write('My App')

user_input = st.text_input("Enter your prompt:")

genai.configure(api_key="AIzaSyDkCZwizw9I4npcyYQu_bkb0Di7dGrD-Rs")

model=genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response=model.generate_content(user_input)
    st.write(response.text)
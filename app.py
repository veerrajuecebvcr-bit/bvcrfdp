import streamlit as st

st.title("Addition Calculator")

st.write("Enter two numbers and press Add to see the result in green.")

num1 = st.number_input("Number 1", value=0.0, format="%f")
num2 = st.number_input("Number 2", value=0.0, format="%f")

if st.button("Add"):
	result = num1 + num2
	st.markdown(f'<p style="color:green; font-size:20px;">Result: {result}</p>', unsafe_allow_html=True)


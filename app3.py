from google import genai
from config import API
client=genai.Client(api_key=API)
import streamlit as st

st.set_page_config(
    page_title="GENAI APP",
    page_icon=":robot_face",
    layout="wide"
)

st.header("GEMINI POWERED AI CHATBOT")
st.write("THIS AI BOT IS BUILT FOR INTERACTION")
st.subheader("INPUT YOUR QUESTION")

input=st.text_area("ENTER YOUR QUESTION")

if st.button("ASK YOUR QUESTION"):
    response=client.models.generate_content(
        model="gemini-3.5-flash",
        contents=input
    )

    st.subheader("Answer:")
    st.write(response.text)
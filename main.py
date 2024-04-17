# Import necessary libraries
import openai
import streamlit as st
import time
import os
import pandas as pd
from io import StringIO
from dotenv import load_dotenv

# Initialize the OpenAI client
client = openai

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    openai.api_key = openai_api_key


# Set up the Streamlit page with a title and icon
st.set_page_config(
    page_title="Content Flagger Chatbot")


# Main chat interface setup
st.title("Content Flagger Chatbot")
st.write("Flag my content")


scan_file = st.file_uploader("Choose a to scan")

topics_file = st.file_uploader("Choose a file of topics")


if (scan_file is not None) and (topics_file is not None):

    response = ""

    with st.spinner("Wait... Generating response..."):
    
    # To read file as bytes:
        bytes_data_scan = scan_file.getvalue()
        bytes_data_topics = topics_file.getvalue()

        # To convert to a string based IO:
        stringio_scan = StringIO(scan_file.getvalue().decode("utf-8"))
        stringio_topics = StringIO(topics_file.getvalue().decode("utf-8"))


        # To read file as string:
        string_data_scan = stringio_scan.read()
        string_data_topics = stringio_topics.read()

        api_response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "user", "content": f"Generate a report on this text: {string_data_scan}. " + 
                    f"The report should look for any topics mentioned in this text: {string_data_topics} " +
                    f"that appear in the first text and generate a report identifying any risks." }])    
        

        response = api_response.choices[0].message.content
        
        st.markdown(response)



    






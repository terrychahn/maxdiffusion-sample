import streamlit as st
import requests
import os
from PIL import Image
import time
from io import BytesIO

# setup environment variable before running
# export MAXDIFFUSION_SERVER_URL="http://IP:PORT"
server_url = os.getenv("MAXDIFFUSION_SERVER_URL")
request_url = server_url+"/generate"

# streamlit config
st.set_page_config(page_title=f'SDXL Lightning + MaxDiffusion', 
                    page_icon=':cloud:', 
                    initial_sidebar_state="collapsed",
                    layout="wide",
                    menu_items=None)

st.subheader("MaxDiffusion on TPU v5e - SDXL Lightning Inferencing", divider="blue")

# prompt input
col1, col2 = st.columns([0.87,0.13])

prompt = col1.text_area("", "", label_visibility="collapsed")
col2.write(" ")
col2.write(" ")
if (col2.button("Generate", type="primary")):
    with st.spinner("Generating an image from the prompt......"):
        # Send requst to the server
        data = {'prompt': prompt}
        #start_time = time.perf_counter()
        output = requests.post(request_url, json = data)
        #end_time = time.perf_counter()

        # Get an image from the response.
        generated_image = Image.open(BytesIO(output.content))

        # Print out
        st.image(generated_image, caption=prompt)
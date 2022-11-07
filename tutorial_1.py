import pandas as pd
import streamlit as st
import time 


col1, col2, col3 = st.columns([1,2,1]) 
col1.markdown("# Welcome to my app")
col1.markdown(" # here is some info on the app. ")
st.markdown('Streamlit is **_really_ cool**.')

uploaded_photo =col2.file_uploader("upload your photo here")
camera_photo=col2.camera_input("Take a photo")

progress_bar=col2.progress(0)

for  perc_completed in range(100):
    time.sleep(0.05)
    progress_bar.progress(perc_completed+1)


col2.success("Photo uploaded successfully")
col3.metric(label="Temperture",value="60 °c", delta = 3)


# read a CSV file inside the 'data" folder next to 'app.py'
df = pd.read_csv("./data/titanic.csv")
# df = pd.read_excel(...)  # will work for Excel files

st.title("Hello world!")  # add a title
st.write(df)  # visualize my dataframe in the Streamlit app

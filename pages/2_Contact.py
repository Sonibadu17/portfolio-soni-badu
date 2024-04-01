import streamlit as st
import os
import path
import sys

st.set_page_config(page_title="Contact Page")
with st.sidebar:
    st.write("Data Engineer at Infosys Ltd.")
    st.write("**Upcoming** Senior Data Analyst at Accenture")

    dir = path.Path(__file__).abspath()
    sys.path.append(dir.parent.parent)

    file_path = './assets/Soni_Badu_Resume.pdf'
    file_pathm = os.path.join(f"{file_path}")
    with open(f"{file_pathm}", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Resume",
                    data=PDFbyte,
                    file_name="Soni_Badu_Resume.pdf",
                    mime='application/octet-stream')
    
st.title("**Get in touch :lower_left_fountain_pen:**")
st.write("**Email :e-mail:** : sonibadu153@gmail.com")
st.write("**LinkedIn Profile** : https://www.linkedin.com/in/soni-badu/")
st.write("**GitHub Profile** : https://github.com/Sonibadu17")

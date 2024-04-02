import streamlit as st
import os
import path
import sys
st.set_page_config(
    page_title="Soni's Portfolio",
    page_icon=":wave:",
)
with st.sidebar:
    st.write("Data Engineer at Infosys Ltd.")
    st.write("**Upcoming** Senior Data Analyst at Accenture")
    dir = path.Path(__file__).abspath()
    sys.path.append(dir.parent.parent)

    file_path = 'assets/Soni_Badu_Resume.pdf'
    file_pathm = os.path.join(f"{file_path}")
    with open(f"{file_pathm}", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Resume",
                    data=PDFbyte,
                    file_name="Soni_Badu_Resume.pdf",
                    mime='application/octet-stream')
    
st.write("# Welcome to Soni's Job Profile! :wave:")
st.markdown("""
     I'm **Soni Badu** having 3.6 years of experienced with a strong background in **Unix, API integration, data pipelines using Python, SQL**, and a passion for working with data. 

     Skilled in **designing, implementing, and maintaining large volumes of data.** Proficient in leveraging APIs to extract data from diverse sources and integrate it into efficient data pipelines. 

     Experienced in **SQL for querying and manipulating relational databases**. Adept at optimizing data workflows for speed, scalability, and reliability. 

     Committed to delivering high-quality data solutions that drive actionable insights and business value.

""")




import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="Soni's Portfolio",
    page_icon=":wave:",
)
with st.sidebar:
    st.write("Data Engineer at Infosys Ltd.")
    st.write("**Upcoming** Senior Data Analyst at Accenture")
    file_path = 'Soni_Badu_Resume.pdf'
    st.markdown(f'<a href="{file_path}">Resume</a>', unsafe_allow_html=True)
    
st.write("# Welcome to Soni's Job Profile! :wave:")
st.markdown("""
     I'm **Soni Badu** having 3.6 years of experienced with a strong background in **Unix, API integration, data pipelines using Python, SQL**, and a passion for working with data. 

     Skilled in **designing, implementing, and maintaining large volumes of data.** Proficient in leveraging APIs to extract data from diverse sources and integrate it into efficient data pipelines. 

     Experienced in **SQL for querying and manipulating relational databases**. Adept at optimizing data workflows for speed, scalability, and reliability. 

     Committed to delivering high-quality data solutions that drive actionable insights and business value.

""")
image = Image.open(os.path.join("/assets/ach1.png"))
st.image(image, caption='Business Ninja Award')


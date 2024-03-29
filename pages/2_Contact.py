import streamlit as st

st.set_page_config(page_title="Contact Page")
with st.sidebar:
    st.write("Data Engineer at Infosys Ltd.")
    st.write("**Upcoming** Senior Data Analyst at Accenture")
    file_path = 'Soni_Badu_Resume.pdf'
    st.markdown(f'<a href="{file_path}">Resume</a>', unsafe_allow_html=True)
    
st.title("**Get in touch :lower_left_fountain_pen:**")
st.write("**Email :e-mail:** : sonibadu153@gmail.com")
st.write("**LinkedIn Profile** : https://www.linkedin.com/in/soni-badu/")
st.write("**GitHub Profile** : https://github.com/Sonibadu17")

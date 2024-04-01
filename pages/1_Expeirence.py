import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image
with st.sidebar:
    st.write("Data Engineer at Infosys Ltd.")
    st.write("**Upcoming** Senior Data Analyst at Accenture")
    file_path = 'Soni_Badu_Resume.pdf'
    st.markdown(f'<a href="{file_path}">Resume</a>', unsafe_allow_html=True)

st.markdown("# **Projects**")
project_1 = st.container()
with project_1:
    st.header("**Streamlining Data Migration: Integrating Oracle with Hive via Kafka**")
    st.write('''The primary objective of the data migration project is to seamlessly transfer data from Oracle/MySQL databases to 
    Hive while ensuring data consistency, integrity, and minimal downtime. The project aims to establish a robust data pipeline using 
    Kafka for real-time data ingestion and processing.''')
    st.write("**Skills**: Spark, SQL, UNIX")

project_2 = st.container()
with project_2:
    st.header("**Efficient Integration: Extracting Nested JSON Data from APIs into Snowflake**")
    st.write('''The primary objective of the data transformation project is to establish a robust and scalable 
    data pipeline that extracts data from disparate sources, applies data transformations, and 
    loads it into Snowflake for analysis and reporting. The project emphasizes security and 
    compliance by implementing secure app-to-app authorization mechanisms for data transfer.''')
    st.write("**Skills**: REST APIs, Python, SQL, SnowFlake")

st.markdown("# **Languages**")

df = pd.DataFrame(dict(
    categories = ['Python', 'SQL', 'Spark', 'UNIX'],
    values = [40, 20, 15, 25]))

fig = px.bar(df, x = 'categories', y = 'values', color = 'categories',color_discrete_map = {'Python': '#7FD4C1', 'SQL': '#30BFDD', 'Scala': '#8690FF',
                                   'Shell/Terminal': '#ACD0F4'})
st.plotly_chart(fig)

st.markdown("# **Achievements**")

image = Image.open('ach1.png')
st.image(image, caption='Business Ninja Award')
image = Image.open('ach2.jpeg')
st.image(image, caption='Rising Star Award')

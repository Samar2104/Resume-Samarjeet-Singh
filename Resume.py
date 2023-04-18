# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:07:24 2023

@author: Asus
"""

from pathlib import Path

import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir  / "style.css"
resume_file = current_dir  / "Samarjeet Singh Resume.pdf"
# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Samarjeet Singh"
PAGE_ICON = ":wave:"
NAME = "Samarjeet Singh"
DESCRIPTION = """
My objective is to become a skilled machine learning engineer and data scientist with a deep 
understanding of algorithms, programming languages, statistical modeling, and data analysis 
techniques, in order to contribute to the development of innovative solutions in the field of data science 
and machine learning.
"""
EMAIL = "samarjeet21apr@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/samarjeet-singh-51b226192/",
    "GitHub": "https://github.com/Samar2104",
}
PROJECTS = {
    "Revenue Grid Prediction App": "https://samar2104-revenue-grid-predictor-app-final-deploy-nkdgbr.streamlit.app"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()



st.title(NAME)
st.write(DESCRIPTION)
st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
st.write("📫", EMAIL)
st.write("- ✔️ 8979328098")


st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education & Qulifications")
st.write(
    """
    - ✔️ Diploma in Data Science From Techstack Pvt. Ltd.
- ✔️ Btech.(CSE) pursuing From Guru Gobind Singh Indraprastha University (GGSIPU):- 8.62 CGPA 
- ✔️ Std. XII From Central Board For Secondary Education (CBSE) in 2019 :- 72.8%
- ✔️ Std. X From Indian Certificate of Secondary Education (ICSE) in 2017 :- 81.5 %
"""
)


st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: Tableu, MS Excel
- 📚 Modeling: Logistic regression, linear regression, Random Forest, SVM, PCA, K-means Clustering, Time Series
- 🗄️ Databases:MySQL
"""
)




st.write('\n')
st.subheader("Internships")
st.write("---")
 

st.write("🚧", "**Intern | Analyst**")
st.write("**Orangus Pvt. Ltd.**")
st.write("02/2023 - Till Now")
st.write(
    """
- ► Used Random Forest classifer to predict whether the customer will be churn or not 
- ► Used python(Sk-learn, pandas) and used spyder and developed the model for prediction
- ► Technology used is spyder, MS Excel, MS SQL Server Studio  
"""
)




st.write("🚧", "**Intern**")
st.write("**Allsoft Solutions Pvt. Ltd.**")
st.write("07/2021 - 08/2021")
st.write(
    """
- ► Developed a Graphical User Interface using Tkinter named as Train Yourself  
- ► This Gui was used to calculate BMI (Body Mass Index) and stores it into the database and according to the BMI it suggests the exersices for the customer
- ► Technology used is  MS SQL Server Studio,  Pycharm
"""
)


st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write(
    """
- ► The aim of this project is to develop a web-based application that predicts the revenue grid for a given customer based on various parameters.The predictive model is built using the Random Forest algorithm, which is known for its accuracy and ability to handle large datasets with multiple features.   
- ► The application is designed using Streamlit, which is an open-source Python library that allows for the creation of interactive web applications. Users can enter customer information into the app, and the machine learning model will make predictions on the revenue grid for that customer.
- ► The Revenue Grid Predictor using Random Forest and Streamlit will provide businesses with an efficient way to predict the revenue grid for their customers, allowing them to make data-driven decisions and improve their sales strategy. The application will be accessible on the cloud, making it easy for 
businesses to use the tool and leverage its benefits.
"""
)

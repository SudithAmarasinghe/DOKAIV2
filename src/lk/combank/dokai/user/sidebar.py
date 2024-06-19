import streamlit as st
from datetime import datetime

class Sidebar:
    def __init__(self):
        pass
    
    def run(self):
        st.sidebar.header("Select options")
        company_names = {
                "commercial bank",
                "company B",
                "company C",
                "company D",
                "company E"
            }
        year_list = {
                "2018", "2019", "2020", "2021", "2022", "2023"
        }
        selected_option = st.sidebar.radio("Select company type:", ("PLC", "PVT"))
        selected_company = st.sidebar.selectbox("Select company", list(company_names))
        selected_year = st.sidebar.selectbox("Select company", list(year_list))

        uploaded_file_placeholder = st.sidebar.empty()
        uploaded_image_placeholder = st.sidebar.empty()
        uploaded_file = uploaded_file_placeholder.file_uploader("Upload a PDF", type=["pdf"])
        uploaded_image = uploaded_image_placeholder.file_uploader("Upload an Image", type=["jpg","png","jpeg"])

        return(selected_company, selected_option, selected_year, uploaded_file, uploaded_image)
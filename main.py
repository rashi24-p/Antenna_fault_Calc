import streamlit as st

import first, second, third, forth, fifth

st.set_page_config(
    page_title="Antenna-Fault-Detector",
    page_icon="chart_with_upwards_trend",
    layout="centered"
)

class MultiApp:

    def __init__(self):
        self.apps = []
    
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        st.markdown(""" 
        <style>
        [data-testid="stAppViewContainer"]{
            background-color:#f0f8ff;
            background-image:linear-gradient(135deg,#F5F995,#ACF995,#F5F995);
            padding:0px;
            margin:0px;
            height:100vh;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <style>
        [data-testid="stSidebar"]{
            background: linear-gradient(135deg,#8DF9B7,#F9F18D,#B0FC7A );
            padding:0px;
            margin:0;
            border-radius:0px;
            border: 2px solid #FB8F77;
            box-shadow: 7px 6px 10px rgba(20, 26, 26, 7);
        }
                    
        [data-testid="stSidebar"] > div:first-child {
            padding:0px;
            border-radius:0px;
            border:2px solid #FB8F77;
        }
        </style>
        """, unsafe_allow_html=True)
        
        with st.sidebar:
            app = st.radio(
                "Antenna Analyzer",
                options=['Introduction', 
                         'Analysis of S11', 
                         'Analysis Of Mutual Coupling & Patch Distance', 
                         'Analysis of Impedance', 
                         'Analysis Of VSWR']
            )
        
        if app == "Introduction":
            first.app()
        elif app == "Analysis of S11":
            second.app()
        elif app == "Analysis Of Mutual Coupling & Patch Distance":
            third.app()
        elif app == "Analysis of Impedance":
            forth.app()
        elif app == "Analysis Of VSWR":
            fifth.app()

# Creating an instance and calling run()
app_instance = MultiApp()
app_instance.run()


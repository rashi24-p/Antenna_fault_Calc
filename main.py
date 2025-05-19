import streamlit as st

from streamlit_option_menu import option_menu


import first,second,third,forth,fiveth,sixth

st.set_page_config(
    page_title="Antenna-Fault-Detector",
    page_icon="chart_with_upwards_trend",
    layout="centered"
)

class MultiApp:

    def __init__(self):
        self.apps =[]
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })

    def run():

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
        # text-align: left;
        border: 2px solid #FB8F77;
        box-shadow: 7px 6px 10px rgba(20, 26, 26, 7);
    }
                    
    [data-testid="stSidebar"] > div:first-child {
        padding:0px;
        border-radius:0px;
        border:2px  solid #FB8F77;
        
    }
    </style>
    """, unsafe_allow_html=True)
        
        with st.sidebar:
            app = option_menu(
                menu_title= 'Antenna-Fault Detector',
                options = ['Introduction','Analysis of S11','Analysis Of Mutual Coupling & Patch Distance','Analysis of Impedance','Analysis Of VSWR',''],
                icons=['graph-up','graph-up','graph-up','graph-up','graph-up'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                "container":
                {
                "padding":"5!important",
                'border-radius':'0px',
                "background":'linear-gradient(135deg, #D3F8EE, #FDE8E5, #D3F8EE)',
                "border":"3px solid #FB8F77",
                
                },
                "icon":{"color":"grey",
                "font-size":"23px",
                "font-weight": "bold"},
                "nav-link":{
                "color":"black",
                "font-size":"20px",
                "text-align":"left", 
                "margin":"0px",
                "border-radius":"20px",
                },   
                "nav-link-selected":{
                "background-color":"#FF5A51"},
                "menu-title":{
                "color":"black",
                "font-size":"24px",
                "text-align":"center"
                },
                }
            )
        if app == "Introduction":
            first.app()
        if  app == "Analysis of S11":
            second.app()
        if  app == "Analysis Of Mutual Coupling & Patch Distance":
            third.app()
        if  app == "Analysis of Impedance":
            forth.app()
        if  app == "Analysis Of VSWR":
            fiveth.app()
        if  app == "":
            sixth.app()   




    run()
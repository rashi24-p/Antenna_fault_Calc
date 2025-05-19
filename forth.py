
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    
    st.title("Impedance Analysis")
    st.markdown("""
    <style>
    h1{
    text-align:center; 
    font-family:'Arial Black ,Gadget,
                sans-serif; 
    background-color:#FA9999; 
    box-shadow: 7px 6px 10px rgba(20, 26, 26, 7);
    border-radius: 10px;    
    }
    
    [data-testid="stVerticalBlock"] {
        background: linear-gradient(135deg, #BAFCE9, #FFF9B7, #BCFCE7);
        padding: 7px;
        margin: 5px;
        text-align: left;
        # border: 2px solid black;
        box-shadow: 5px 6px 6px rgba(20, 20, 20, 7);
        border-radius: 5px;
    }
                
    
                
    
                
    .stText{
    font-family:'Verdanan',sans-serif;
        font-size:20px;
        line-height:1.8;
        color:#59A4D2;            
    }
    
             
    </style>
    """,unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
       df = pd.read_csv(uploaded_file)
       
       df.rename(columns={"Freq [GHz]":"Frequency","re(Zo(2)) []":"Impedance"},inplace=True)

       mean_impedance = df["Impedance"].mean()
       min_impedance = df["Impedance"].min()
       max_impedance = df["Impedance"].max()
       std_dev_impedance = df["Impedance"].std()

       st.markdown('<p class="header">Impedance Analysis</p>', unsafe_allow_html=True)

       st.success(f"**Mean Impedance:** {mean_impedance:.2f} Ohms")
       st.markdown('<p class="caption-text">It    indicates Average impedance across frequency    range, indicating stability.</p>',    unsafe_allow_html=True)

       st.success(f"**Min Impedance:** {min_impedance:.2f} Ohms")
       st.markdown('<p class="caption-text">It   indicates Lowest impedance recorded,      potential mismatch indicator.</p>',      unsafe_allow_html=True)

       st.success(f"**Max Impedance:** {max_impedance:.2f} Ohms")
       st.markdown('<p class="caption-text">It   indicates Peak impedance detected,    variations may affect signal quality.</p>',    unsafe_allow_html=True)

       st.success(f"**Standard Deviation:** {std_dev_impedance:.4f} Ohms")
       st.markdown('<p class="caption-text">It    indicates Impedance fluctuation measure,    lower values indicate stable circuits.</p>',    unsafe_allow_html=True)

       fig, ax = plt.subplots()
       ax.plot(df["Frequency"], df["Impedance"],    marker="o", linestyle="-", color="red")
       ax.set_xlabel("Frequency (GHz)")
       ax.set_ylabel("Impedance (Ohms)")
       ax.set_title("Impedance vs Frequency")
       ax.grid()

       st.pyplot(fig)
       st.markdown('<p class="caption-text">Graph    represents impedance variations with    frequency. A stable curve suggests efficient    signal transmission.</p>',    unsafe_allow_html=True)

if __name__ == "__main__":
    app()


   


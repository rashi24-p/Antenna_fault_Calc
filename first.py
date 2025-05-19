import streamlit as st

def app():
    st.title("MIMO Microstrip Patch Antenna Fault Diagnosis Dashboard")

    # Styling the components of this page here with css , (# color is by default set in title )
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
        padding: 2px;
        margin: 1px;
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

    # Column Layout
    col1 , col2 = st.columns(2)
    with col1:
        st.image("Images/ant4.jpg",caption="",use_container_width=True )

    with col2:
        st.image("Images/ant7.jpg",caption="",use_container_width=True)

    # with col3:
    #     st.image("Images/ant3.jpg",caption="",use_container_width=True)

    with st.container(border=True):
        st.write('This Project consist  of developing a basic MIMO antenna, modeling and optimizing the developed model with the ML technique in fault detection in antenna design. ')
        st.write('''5G Mobile communication, Wifi, 
        Satellite Communication, Radar systems, Industrial,         scientific, and Medical (ISM) use MIMO antenna         technology providing benefits such as increased data         rates, improved reliability and enhanced overall         performance to detect a fault type including faults in         elements.''')
        st.write('''
        These Elements feed points faults, and feed network faults in MIMO type antennas can be addressed by using a ⁸Streamlit Dashboard to ML techniques in an easy way, to identify whether an antenna is healthy(0) and faulty(1) and show specific fault types
       (e.g . misalignment, material degradation) by providing in  features such as frequenci  peak, and average Voltage Stand  Wave Ratio, radiation patt  metrics and physical dimensions  get desired result.

        ''')

    with st.expander("Expand for more explanation!"):
        st.write('''
        The growing reliance on wireless communication for applications such as satellite communications, radar systems, and 5G networks demands robust and efficient antenna systems. Microstrip patch antennas are widely used for their low profile, ease of fabrication, and cost-effectiveness. However, traditional methods of optimizing antenna performance often fail to address the complex requirements of modern MIMO systems operating in dynamic environments.
        ''')
        st.write('''
        This project aims to bridge these gaps by incorporating machine learning techniques into the design and optimization of a two-patch MIMO-enabled microstrip antenna. The primary goal is to enhance antenna performance by detecting potential faults. The fault parameters under consideration include physical dimensions, radiation patterns, VSWR (Voltage Standing Wave Ratio), gain, and frequency range. A dashboard will serve as a health status indicator, classifying the antenna as "healthy" or "unhealthy" using a binary output of 1 or 0, respectively.
        ''')
        st.write('''
        Designed to operate in the 8 GHz frequency band, which lies within the X-band of the electromagnetic spectrum, this antenna is ideal for satellite communication and high-speed data transmission. By integrating simulation tools such as Ansys with machine learning models, this approach ensures a comprehensive and innovative solution for antenna optimization, paving the way for advancements in modern communication systems.
        ''')
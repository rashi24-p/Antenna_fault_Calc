import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.title("VSWR Analysis")
    st.markdown("""
       <style>
          .stApp{
                background-color:#f4f4f4;
            }
          .header{
                font-size:22px;
                font-weight:bold;
                color:#333333;
                text-align:center;
            }
          .highlight{
                font-size:18px;
                font-weight:bold;
                color:#008000;
            }
            .caption-text{
                font-size:14px;
                color:#0066cc;
                font-style:italic;    
            }
            .styled-table{
                border-collapse : collapse;
                width: 100%;
                font-size:16px;
            }
            .styled-table th, .styled-table td{
                border:1px solid #ddd;
                padding:10px;
                text-align:center;
            }
            .styled-table th{
                background-color:#0066cc;
                color:white;    
            }
            .styled-table td{
                background-color:#f9f9f9;    
            }
            
       <style>
      """,unsafe_allow_html=True)
      
    uploaded_file = st.file_uploader("Upload your Antenna VSWR CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        possible_vswr_cols = [col for col in df.columns if "VSWR" in col]
        possible_freq_cols = [col for col in df.columns if "Freq" in col]

        if not possible_vswr_cols or not possible_freq_cols:
            st.error("Error: Could not find VSWR or Frequency columns! Please check your CSV format.")

        else:
            vswr_col = possible_vswr_cols[0]
            freq_col = possible_freq_cols[0]

            df.rename(columns={freq_col: "Frequency", vswr_col: "VSWR"}, inplace=True)
            df["VSWR"] = pd.to_numeric(df["VSWR"], errors="coerce")

            df["Reflection Coefficient"] = (df["VSWR"] - 1) / (df["VSWR"] + 1)

            df["Return Loss (dB)"] = -20 * np.log10(abs(df["Reflection Coefficient"]))

            df["Power Loss (%)"] = (df["Reflection Coefficient"] ** 2) * 100

            df["Mismatch Loss (dB)"] = -10 * np.log10(1 - df["Reflection Coefficient"] ** 2)

            df["Transmission Coefficient"] = 1 - df["Reflection Coefficient"] ** 2

            df.dropna(inplace=True)

            mean_vswr = df["VSWR"].mean()
            min_vswr = df["VSWR"].min()
            max_vswr = df["VSWR"].max()

            st.markdown('<p class="header">VSWR Analysis</p>', unsafe_allow_html=True)
            st.write(f"<p class='highlight'>Average VSWR: {mean_vswr:.3f}</p>", unsafe_allow_html=True)
            st.markdown('<p class="caption-text">Represents overall impedance matching efficiency.</p>', unsafe_allow_html=True)


            st.write(f"<p class='highlight'>Minimum VSWR: {min_vswr:.3f}</p>", unsafe_allow_html=True)
            st.markdown('<p class="caption-text">Ideal at resonance points—minimal reflections.</p>', unsafe_allow_html=True)

            st.write(f"<p class='highlight'>Maximum VSWR: {max_vswr:.3f}</p>", unsafe_allow_html=True)
            st.markdown('<p class="caption-text">Indicates frequency bands with potential mismatch issues.</p>', unsafe_allow_html=True)

            fig, ax = plt.subplots()
            ax.plot(df["Frequency"], df["VSWR"], marker="o", linestyle="-", color="blue")
            ax.set_xlabel("Frequency (GHz)")
            ax.set_ylabel("VSWR")
            ax.set_title(f"VSWR vs Frequency     ({vswr_col})")
            ax.grid()
            st.pyplot(fig)
            st.markdown('<p     class="caption-text">Lower VSWR values  indicate better impedance matching for  efficient signal transmission.</p>',     unsafe_allow_html=True)


            st.markdown('<p class="header">Understanding RF Parameters</p>', unsafe_allow_html=True)

            
            with st.container(border=True):
                  
                  

                  st.write("            - **Reflection Coefficient (\(\Gamma\)) **: Measures how much of the signal is reflected due to impedance mismatch.")
                  st.write("            - **Return Loss (dB)**: Indicates the amount of signal loss due to reflection. Higher values signify better efficiency.")
                  st.write("- **Power Loss (%)**: Represents the  percentage of energy lost due to  reflection. Lower values mean better  signal transmission.")
                  st.write("- **Mismatch Loss (dB)**: Quantifies  power loss from impedance mismatches, helping determine circuit performance.")
                  st.write("- **Transmission Coefficient (\(T\))**: Shows how much power is successfully  transmitted. Closer to 1 means minimal signal loss.")
                  st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<p class="header">Additional RF Parameters</p>', unsafe_allow_html=True)
            styled_table_html = df[["Frequency", "Reflection Coefficient", "Return Loss (dB)", "Power Loss (%)", "Mismatch Loss (dB)", "Transmission Coefficient"]].head().to_html(classes="styled-table",     index=False)
            st.markdown(styled_table_html, unsafe_allow_html=True)


if __name__ == "__main__":
    app()

    
 



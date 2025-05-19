import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constants
SPEED_OF_LIGHT = 3e8  # Speed of light (m/s)

def calculate_patch_distance(frequency_ghz):
    """Calculate patch distance using wavelength."""
    frequency_hz = frequency_ghz * 1e9  # Convert GHz to Hz
    wavelength = SPEED_OF_LIGHT / frequency_hz  # Wavelength calculation
    patch_distance = wavelength / 2  # Half-wavelength spacing
    return patch_distance

def app():
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
    st.title("Mutual Coupling & Patch Distance Calculator")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file:
        try:
            # Read CSV File
            data = pd.read_csv(uploaded_file)

            # Check for required columns
            if not all(col in data.columns for col in ["Freq [GHz]", "dB(S(3,2)) []"]):
                st.error("⚠ CSV must contain 'Freq [GHz]' and 'dB(S(3,2)) []' columns.")
                return

            # Extract Data
            frequency = data["Freq [GHz]"].values
            mutual_coupling = data["dB(S(3,2)) []"].values

            # Calculate Patch Distance
            patch_distances = [calculate_patch_distance(f) for f in frequency]

            # Display Computed Results
            st.subheader("Calculated Antenna Metrics")
            df_display = pd.DataFrame({
                "Frequency (GHz)": frequency,
                "Mutual Coupling (dB)": mutual_coupling,
                "Patch Distance (cm)": [d * 100 for d in patch_distances]  # Convert to cm
            })
            # st.dataframe(df_display)

            # Find values at 8 GHz
            if 8.0 in frequency:
                index_8GHz = np.where(frequency == 8.0)[0][0]
                st.subheader("Key Results at 8 GHz:")
                st.write(f"📡 **Mutual Coupling (S21) at 8 GHz:** {mutual_coupling[index_8GHz]:.2f} dB")
                st.write(f"📏 **Estimated Patch Distance at 8 GHz:** {patch_distances[index_8GHz] * 100:.2f} cm")

            # Plot Mutual Coupling vs Frequency
            st.subheader("Mutual Coupling vs Frequency")
            fig, ax = plt.subplots()
            ax.plot(frequency, mutual_coupling, marker="o", linestyle="-", color="blue", label="S21 (Mutual Coupling)")
            ax.set_xlabel("Frequency (GHz)")
            ax.set_ylabel("Mutual Coupling (dB)")
            ax.set_title("Mutual Coupling vs Frequency")
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

            # Plot Patch Distance vs Frequency
            st.subheader("Patch Distance vs Frequency")
            fig2, ax2 = plt.subplots()
            ax2.plot(frequency, [d * 100 for d in patch_distances], marker="o", linestyle="-", color="red", label="Patch Distance")
            ax2.set_xlabel("Frequency (GHz)")
            ax2.set_ylabel("Patch Distance (cm)")
            ax2.set_title("Patch Distance vs Frequency")
            ax2.legend()
            ax2.grid(True)
            st.pyplot(fig2)

        except Exception as e:
            st.error(f"⚠ Error processing file: {e}")

# Run the app
if __name__ == "__main__":
    app()



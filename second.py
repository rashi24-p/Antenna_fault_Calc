import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def app():
    st.title("Enter the Parameters in the Fields Below:")

    st.markdown("""
    <style>
    h1 {
        text-align: center; 
        font-family: 'Arial Black', Gadget, sans-serif; 
        background-color: #FA9999; 
        box-shadow: 7px 6px 10px rgba(20, 26, 26, 7);
        border-radius: 10px;    
    }       
    .info-box {
        background-color: #e6f7ff;
        padding: 15px;
        margin: 20px;
        border-radius: 8px;
        border-left: 5px solid #1890ff;
        color: #00529b;
        font-family: Arial, sans-serif;
        font-size: 14px;
    }
    </style>
                
    <div class="info-box">
    The frequency range should be provided in Hz or GHz. VSWR (Voltage Standing Wave Ratio) is a unitless value. 
    The radiation parameter must be specified in dB. The physical dimensions, including the length of the patch, 
    width of the patch, and height of the substrate, should be measured in meters or centimeters. 
    The dielectric constant is a unitless quantity. The input impedance should be given in Ohms. 
    The dimensions of the ground plane, including the length of the ground, width of the ground, and height of the ground, 
    must also be measured in meters or centimeters. Lastly, the gain should be mentioned in dBi.
    </div>
    """, unsafe_allow_html=True)

    st.header("User Input")
    expected_freq = st.number_input("Enter expected resonance frequency (GHz):", value=1.0)
    tolerance = 0.05 * expected_freq
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file:
        try:
            data = pd.read_csv(uploaded_file)
            
            if data.shape[1] < 2:
                st.error("⚠ Uploaded CSV file must contain at least two columns (Frequency and S11).")
                return

            x_data = data.iloc[:, 0].values  # Frequency (GHz)
            y_data = data.iloc[:, 1].values  # S11 (dB)

            # Detect resonance frequency (deepest dip in S11)
            min_s11_index = np.argmin(y_data)
            resonant_freq = x_data[min_s11_index]

            # Find -10 dB bandwidth
            below_10dB_indices = np.where(y_data < -10)[0]
            if len(below_10dB_indices) > 0:
                lower_freq = x_data[below_10dB_indices[0]]
                upper_freq = x_data[below_10dB_indices[-1]]
                bandwidth = upper_freq - lower_freq
                st.write(f"📡 Bandwidth: {bandwidth:.2f} GHz (From {lower_freq:.2f} to {upper_freq:.2f} GHz)")
            else:
                st.warning("⚠ Could not determine bandwidth. S11 does not drop below -10 dB.")

            # Return Loss Calculation (Minimum S11 value)
            return_loss = min(y_data)
            st.write(f"📉 Return Loss: {return_loss:.2f} dB")

            # Fault Detection
            st.subheader("Fault Detection")
            faults_detected = False
            S11_THRESHOLD = -10  # Impedance mismatch threshold

            st.write(f"🔍 Expected Resonance: {expected_freq} GHz")
            st.write(f"📡 Detected Resonance: {resonant_freq:.2f} GHz")

            # Impedance mismatch
            if max(y_data) > S11_THRESHOLD:
                st.error("⚠ Impedance mismatch detected! (High S11)")
                faults_detected = True

            # Dielectric change (Shift in resonant frequency)
            if abs(resonant_freq - expected_freq) > tolerance:
                st.error("⚠ Dielectric change detected! (Resonance frequency shift)")
                faults_detected = True

            # Multiple resonances → Possible fabrication error
            if len([x for x in y_data if x < -10]) > 1:
                st.error("⚠ Possible fabrication error detected! (Multiple resonances)")
                faults_detected = True

            # Resonance shift → Possible material defect
            if resonant_freq > expected_freq + tolerance:
                st.error("⚠ Resonance shifted higher! Possible material defect or thickness variation.")
                faults_detected = True
            if resonant_freq < expected_freq - tolerance:
                st.error("⚠ Resonance shifted lower! Possible substrate issue or misalignment.")
                faults_detected = True

            # Weak reponse -> Potential antenna inefficiency
            if min(y_data) > -10:
                st.error("⚠ Weak antenna response! Poor return loss.")
                faults_detected = True

            # Bandwidth Fault Detection
            if bandwidth is not None:
                bandwidth_lower_bound = 0.05 * expected_freq
                bandwidth_upper_bound = 0.10 * expected_freq

                st.subheader("Expected Bandwidth Range")
                st.write(f"Lower Bound: {bandwidth_lower_bound: .2f}GHz")
                st.write(f"Upper Bound: {bandwidth_upper_bound: .2f}GHz")


                if bandwidth <= bandwidth_lower_bound:
                    st.error("⚠ Bandwidth too narrow! Possible inefficiency or high losses.")
                elif bandwidth >= bandwidth_upper_bound:
                    st.error("⚠ Bandwidth too wide! Possible unwanted radiation or design issue.")
                    faults_detected = True
                else:
                    st.success("✅ Bandwidth is within the expected range.")

            if not faults_detected:
                st.success("✅ No major fault detected.")

            # Plot the S11 graph
            st.subheader("S11 Parameter Graph")
            fig, ax = plt.subplots()
            ax.plot(x_data , y_data ,label = "S11 Curve")
            ax.scatter(resonant_freq , y_data[min_s11_index], color = "red",
                       label = "Resonant Frequency")
            ax.set_xlabel("Frequency (GHz)")
            ax.set_ylabel("S11 (dB)")
            ax.set_title("S11 vs Frequency")
            ax.legend()
            ax.grid()
            st.plotly_chart(fig)


        except Exception as e:
            st.error(f"⚠ An error occurred while processing the CSV file: {e}")

    else:
        st.info("Please upload a CSV file to proceed.")


if __name__ == "__main__":
    app()

            

             









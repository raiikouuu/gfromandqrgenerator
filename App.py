import streamlit as st
import pandas as pd
import qrcode 
from PIL import Image
import os
import time

# -----------------------------
# GOOGLE SHEETS CSV LINK
# Replace this with your own Google Sheet CSV link
# -----------------------------
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSe4Mlc7QAWT5-e9DRKdFI3ecQijiaYDnZMLT7a4wEX1dzvC5ftEHElX0g0jl0wHgcHdHs33jt56G5b/pub?output=csv"

st.title("Google Form QR Generator")

st.write("Click the button below to answer the Google Form.")

# -----------------------------
# GOOGLE FORM BUTTON
# -----------------------------
google_form_url = "https://forms.gle/jgouL8gwFgzwQzvY9"

if st.button("Open Google Form"):
    st.markdown(f"""
    <meta http-equiv="refresh" content="0; url={google_form_url}">
    """, unsafe_allow_html=True)

st.divider()

# -----------------------------
# CHECK FOR NEW FORM RESPONSES
# -----------------------------
if st.button("Generate QR from Latest Response"):

    try:
        # Read latest form responses
        df = pd.read_csv(SHEET_URL)

        # Get latest row
        latest = df.iloc[-1]

        # Convert row into text
        qr_data = "\n".join(
            [f"{col}: {latest[col]}" for col in df.columns]
        )

        # Generate QR
        qr = qrcode.make(qr_data)

        # Save QR
        qr_path = "latest_qr.png"
        qr.save(qr_path)

        st.success("QR Code Generated!")

        # Display QR
        img = Image.open(qr_path)
        st.image(img, caption="Generated QR Code")

        # Download button
        with open(qr_path, "rb") as file:
            st.download_button(
                label="Download QR",
                data=file,
                file_name="qr_code.png",
                mime="image/png"
            )

    except Exception as e:
        st.error(f"Error: {e}")

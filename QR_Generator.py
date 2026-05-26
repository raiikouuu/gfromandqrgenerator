import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="QR Generator",
    page_icon="🎟"
)

# -----------------------------------
# GOOGLE SHEET CSV
# -----------------------------------

GOOGLE_SHEET_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSe4Mlc7QAWT5-e9DRKdFI3ecQijiaYDnZMLT7a4wEX1dzvC5ftEHElX0g0jl0wHgcHdHs33jt56G5b/pub?output=csv_LINK"

# -----------------------------------
# UI
# -----------------------------------

st.title("🎟 QR Generator")

st.write("""
Latest Google Form submission will automatically generate a QR code.
""")

st.divider()

try:

    # Read latest response
    df = pd.read_csv(GOOGLE_SHEET_CSV)

    # Check empty
    if df.empty:
        st.warning("No responses submitted yet.")
        st.stop()

    # Get latest response
    latest = df.iloc[-1]

    # Convert to QR text
    qr_data = ""

    for column in df.columns:
        qr_data += f"{column}: {latest[column]}\n"

    # -----------------------------------
    # GENERATE QR
    # -----------------------------------

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Save image to memory
    buffer = BytesIO()
    img.save(buffer, format="PNG")

    # -----------------------------------
    # DISPLAY QR
    # -----------------------------------

    st.subheader("📱 Generated QR Code")

    st.image(
        buffer,
        width=300
    )

    st.success("QR Code Generated Successfully!")

    st.divider()

    # -----------------------------------
    # LATEST RESPONSE
    # -----------------------------------

    st.subheader("📄 Latest Submitted Response")

    st.dataframe(
        latest.to_frame(),
        use_container_width=True
    )

    # -----------------------------------
    # DOWNLOAD BUTTON
    # -----------------------------------

    st.download_button(
        label="⬇ Download QR Code",
        data=buffer.getvalue(),
        file_name="generated_qr.png",
        mime="image/png"
    )

except Exception as e:

    st.error("Something went wrong.")
    st.code(str(e))

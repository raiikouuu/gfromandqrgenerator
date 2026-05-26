import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO
import time

# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="Auto QR Generator",
    page_icon="📱",
    layout="centered"
)

# ------------------------------------
# CUSTOM STYLE
# ------------------------------------

st.markdown("""
<style>

.main {
    text-align: center;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

.qr-container {
    padding: 20px;
    border-radius: 15px;
    background-color: #f3f3f3;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------
# YOUR LINKS
# ------------------------------------

GOOGLE_FORM_LINK = "https://forms.gle/aEkPK2UH5cZTMA7j8K"

GOOGLE_SHEET_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSe4Mlc7QAWT5-e9DRKdFI3ecQijiaYDnZMLT7a4wEX1dzvC5ftEHElX0g0jl0wHgcHdHs33jt56G5b/pub?output=csv"

# ------------------------------------
# HEADER
# ------------------------------------

st.title("📱 Automatic QR Generator")

st.write("""
Submit the Google Form and instantly receive a QR Code.
""")

st.divider()

# ------------------------------------
# OPEN FORM BUTTON
# ------------------------------------

st.link_button(
    "📝 Open Google Form",
    GOOGLE_FORM_LINK
)

st.divider()

# ------------------------------------
# AUTO GENERATE QR
# ------------------------------------

st.subheader("🎟 Your Generated QR Code")

try:

    # Read latest response
    df = pd.read_csv(GOOGLE_SHEET_CSV)

    # Check empty
    if df.empty:
        st.warning("No responses found yet.")
        st.stop()

    # Latest response
    latest = df.iloc[-1]

    # Convert response to text
    qr_data = ""

    for column in df.columns:
        qr_data += f"{column}: {latest[column]}\n"

    # Generate QR
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

    # Save to memory
    buffer = BytesIO()
    img.save(buffer, format="PNG")

    # Display QR
    st.image(
        buffer,
        width=300
    )

    st.success("✅ QR Code Generated Successfully!")

    # Download button
    st.download_button(
        label="⬇ Download QR Code",
        data=buffer.getvalue(),
        file_name="generated_qr.png",
        mime="image/png"
    )

    st.divider()

    # Show latest response
    st.subheader("📄 Latest Submission")

    st.dataframe(
        latest.to_frame(),
        use_container_width=True
    )

except Exception as e:

    st.error(" Error")
    st.code(str(e))
       

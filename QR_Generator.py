import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO
import time

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="QR Generator",
    page_icon="🎟",
    layout="centered"
)

# -----------------------------------
# GOOGLE SHEET CSV LINK
# -----------------------------------

GOOGLE_SHEET_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSe4Mlc7QAWT5-e9DRKdFI3ecQijiaYDnZMLT7a4wEX1dzvC5ftEHElX0g0jl0wHgcHdHs33jt56G5b/pub?output=csv"

# -----------------------------------
# CUSTOM DESIGN
# -----------------------------------

st.markdown("""
<style>

.main {
    text-align: center;
}

.title {
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    font-size: 18px;
    color: gray;
    margin-bottom: 20px;
}

.qr-box {
    padding: 25px;
    border-radius: 20px;
    background-color: #f5f5f5;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------

st.markdown(
    '<div class="title">🎟 QR Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Latest Google Form submission</div>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------------
# AUTO REFRESH BUTTON
# -----------------------------------

refresh = st.button("🔄 Refresh Latest Submission")

# -----------------------------------
# GENERATE QR
# -----------------------------------

try:

    with st.spinner("Generating QR Code..."):

        time.sleep(1)

        # Read CSV
        df = pd.read_csv(GOOGLE_SHEET_CSV)

        # Empty check
        if df.empty:
            st.warning("No submissions found yet.")
            st.stop()

        # Latest response
        latest = df.iloc[-1]

        # Convert to QR text
        qr_text = ""

        for column in df.columns:
            qr_text += f"{column}: {latest[column]}\n"

        # -----------------------------------
        # CREATE QR
        # -----------------------------------

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr.add_data(qr_text)
        qr.make(fit=True)

        qr_image = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        # Save to memory
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")

        # -----------------------------------
        # DISPLAY QR
        # -----------------------------------

        st.markdown("## 📱 Generated QR Code")

        st.image(
            buffer,
            width=320
        )

        st.success("✅ QR Code Generated Successfully!")

        st.divider()

        # -----------------------------------
        # RESPONSE TABLE
        # -----------------------------------

        st.markdown("## 📄 Latest Submission")

        st.dataframe(
            latest.to_frame(),
            use_container_width=True
        )

        st.divider()

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

    st.error(" Failed to Generate QR Code")
    st.code(str(e))

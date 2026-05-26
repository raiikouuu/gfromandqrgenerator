import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="QR Form System",
    page_icon="📱",
    layout="centered"
)

# -----------------------------------
# GOOGLE FORM LINK
# -----------------------------------

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeTxLbmbDdiqdaoBFC43fBGQ-aE-f6kWpF0b3SgVZbkOVMoJg/viewform?usp=dialog"

# -----------------------------------
# CUSTOM DESIGN
# -----------------------------------

st.markdown("""
<style>

.main {
    text-align: center;
}

.title {
    font-size: 50px;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 20px;
    color: gray;
    margin-bottom: 30px;
}

.box {
    padding: 30px;
    border-radius: 20px;
    background-color: #f5f5f5;
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# UI
# -----------------------------------

st.markdown(
    '<div class="title">📱 QR Form System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Google Form to Automatic QR Generator</div>',
    unsafe_allow_html=True
)

st.divider()

st.markdown("""
### 🚀 How It Works

1. Open the Google Form  
2. Submit your response  
3. Open the QR Generator page  
4. Your QR code will automatically appear
""")

st.divider()

# -----------------------------------
# BUTTON
# -----------------------------------

st.link_button(
    "📝 Open Google Form",
    GOOGLE_FORM_URL
)

st.divider()

st.success("✅ After submitting, open the QR Generator page from the sidebar.")

import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="QR Form System",
)

# -----------------------------------
# GOOGLE FORM LINK
# -----------------------------------

GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSeTxLbmbDdiqdaoBFC43fBGQ-aE-f6kWpF0b3SgVZbkOVMoJg/viewform?usp=sharing&ouid=108970755142225471143"

# -----------------------------------
# UI
# -----------------------------------

st.title("QR Form System")

st.write("""
Welcome!

Click the button below to answer the Google Form.
After submitting, open the QR Generator page from the sidebar.
""")

st.divider()

st.link_button(
    "📝 Open Google Form",
    GOOGLE_FORM_LINK
)

st.info("""
After submitting the form:

1. Return to this app
2. Open 'QR Generator' from the sidebar
3. Your QR code will automatically appear
""")

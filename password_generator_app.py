# 🔐 Secure Password Generator using Streamlit
import streamlit as st
import random
import string

# Page configuration
st.set_page_config(page_title="Secure Password Generator", page_icon="🔐", layout="centered")

# Title
st.title("🔐 Secure Password Generator")
st.write("Generate strong and customizable passwords instantly!")

# Input controls
length = st.slider("Select password length", min_value=6, max_value=24, value=12)
use_digits = st.checkbox("Include numbers (0-9)", value=True)
use_symbols = st.checkbox("Include symbols (!@#$%)", value=True)

# Generate button
if st.button("Generate Password"):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    st.success("✅ Your Secure Password:")
    st.code(password, language='text')

st.markdown("---")
st.caption("Developed by **Rushda 💻** | Powered by Streamlit")

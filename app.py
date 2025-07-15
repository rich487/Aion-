import streamlit as st
from code_generator import generate_code
from code_modifier import modify_code
from utils import save_code, read_code

st.set_page_config(page_title="AION - Immortal AI Builder", layout="centered")
st.title("🤖 AION - Your Personal AI Overlord")

st.markdown("### 1. Describe your app idea")
prompt = st.text_area("App Idea", placeholder="e.g. Create a note-taking web app with user login")

if st.button("🚀 Generate App Code"):
    if prompt:
        with st.spinner("Generating full Python code..."):
            code = generate_code(prompt)
            save_code("generated_code/app.py", code)
        st.success("✅ Code generated and saved!")
        st.code(code, language='python')
    else:
        st.warning("⚠️ Please enter an idea.")

st.markdown("---")
st.markdown("### 2. Modify existing code")

modifications = st.text_area("🔧 What should be changed?", placeholder="e.g. Add dark mode or use Flask instead of Streamlit")

if st.button("✏️ Apply Modification"):
    if modifications:
        with st.spinner("Modifying code..."):
            updated_code = modify_code(modifications)
        st.success("✅ Code modified!")
        st.code(updated_code, language='python')
    else:
        st.warning("⚠️ Please describe the change.")

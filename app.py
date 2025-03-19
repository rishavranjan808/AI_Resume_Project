from dotenv import load_dotenv
load_dotenv()

import io
import base64
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key=os.getenv("API_KEY"))

# ---------- Function to Get Gemini Response ----------
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# ---------- Function to Process PDF ----------
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None: 
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# ---------- Streamlit UI ----------
st.set_page_config(
    page_title="ATS Resume Checker",
    page_icon="📄",
    layout="wide"
)


# ---------- Main Layout ----------
st.header("🚀 ATS Resume Tracker")
st.write("Use this tool to analyze your resume against job descriptions and identify improvement areas.")

# Styling the job description text area
input_texts = st.text_area(
    "📌 Paste the Job Description Here:", 
    key="input",
    height=200,
    placeholder="Paste job description..."
)

# Upload resume section
uploaded_file = st.file_uploader("📎 Upload your Resume (PDF)", type=["pdf"])

# Display success message if uploaded
if uploaded_file is not None:
    st.success("✅ PDF Uploaded Successfully")

# Add a visual separator
st.markdown("---")

# ---------- Buttons ----------
col1, col2 = st.columns(2)

with col1:
    submit1 = st.button("🧐 Review Resume", use_container_width=True)

with col2:
    submit3 = st.button("📊 Percentage Match", use_container_width=True)

# ---------- Input Prompts ----------
input_prompt1 = """ 
You are an experienced Human Resource with Tech experience in the field of any one job role from data science, data analyst, machine learning engineer, AI engineer. Your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidaye's profile aligns with the role. Highlight the strenghts and weaknesses of the applicant in relation to the specified job description requirements."""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with deep understanding of any one job role from data science, data analyst, machine learning engineer, AI engineer and deep ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage resumes matches the job description. First the output should come as percentage and then the list of keywords missing, Spell Check, Grammer Check, suggest improvements in phrasing and last final thoughts.
"""

# ---------- Output Display ----------
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_texts)
        
        # Display response in styled box
        st.subheader("💡 Review Summary:")
        st.success("✅ Resume analyzed successfully!")
        st.write(response)

    else:
        st.warning("⚠️ Please upload a resume first.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_texts)
        
        # Display response in styled box
        st.subheader("📊 Percentage Match Result:")
        st.success("✅ Matching analysis completed!")
        st.write(response)

    else:
        st.warning("⚠️ Please upload a resume first.")

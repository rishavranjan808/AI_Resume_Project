# ATS Resume Checker using Gemini AI

An AI-powered Resume Analysis and ATS Evaluation tool built with **Google Gemini 2.0 Flash**, **Python**, and **Streamlit**. The application analyses uploaded resumes against job descriptions, provides recruiter-style feedback, identifies missing keywords, and estimates ATS compatibility to help candidates optimise their job applications.

---

## Project Overview

Modern recruitment processes often involve Applicant Tracking Systems (ATS) that automatically screen resumes before they reach recruiters. Candidates frequently struggle to understand why their applications are rejected despite having relevant qualifications.

This project leverages Google's Gemini AI to simulate both:

- A Human Recruiter reviewing a resume
- An ATS system evaluating job-description alignment

The system provides actionable recommendations that help users improve resume quality, keyword relevance, and overall presentation.

---

## Features

### AI Resume Review

Receive recruiter-style feedback covering:

- Skills relevance
- Work experience
- Education
- Resume structure
- Strengths and weaknesses
- Overall role suitability

---

### ATS Match Analysis

Compare a resume against a target job description and receive:

- ATS Match Percentage
- Missing Keywords
- Grammar Check
- Spelling Check
- Resume Improvement Suggestions
- Final Recruitment Assessment

---

### Job Description Matching

Upload a resume and paste any job description to evaluate how well the candidate profile aligns with the role requirements.

---

### Gemini-Powered Analysis

Uses **Google Gemini 2.0 Flash** to perform contextual analysis rather than relying solely on keyword matching.

---

### Interactive UI

A simple Streamlit interface enables users to:

- Upload resumes
- Enter job descriptions
- Generate AI feedback instantly
- Review ATS compatibility results

---

## Application Workflow

```text
Upload Resume (PDF)
          │
          ▼
Convert First Page to Image
          │
          ▼
Enter Job Description
          │
          ▼
Gemini 2.0 Flash Analysis
          │
          ├──────────► Resume Review
          │
          └──────────► ATS Match Report
                          │
                          ▼
      Feedback + Recommendations
```

---

## Technology Stack

### Artificial Intelligence

- Google Gemini 2.0 Flash
- Prompt Engineering

### Backend

- Python

### Frontend

- Streamlit

### Document Processing

- pdf2image
- Pillow (PIL)

### Environment Management

- python-dotenv

---

## Repository Structure

```text
.
├── app.py
├── requirements.txt
├── .env
├── assets/
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/AI_Resume_Project.git

cd AI_Resume_Project
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Gemini API Key

Create a `.env` file in the project root:

```env
API_KEY=YOUR_GEMINI_API_KEY
```

---

### Run the Application

```bash
streamlit run app.py
```

---

## How to Use

### Option 1: Resume Review

1. Upload your resume in PDF format.
2. Paste the target job description.
3. Click **Review Resume**.
4. Receive professional feedback highlighting strengths and weaknesses.

---

### Option 2: ATS Match Analysis

1. Upload your resume.
2. Paste the job description.
3. Click **Percentage Match**.
4. Receive:

- ATS Match Score
- Missing Keywords
- Grammar Feedback
- Resume Optimisation Suggestions

---

## Example Output

```text
ATS Match Score: 85%

Missing Keywords:
- SQL
- Power BI
- Data Visualisation

Grammar Feedback:
- Improve sentence consistency in Experience section.

Suggestions:
- Add measurable achievements.
- Include project outcomes using metrics.
- Incorporate missing technical skills from the job description.

Final Assessment:
Strong candidate profile with room for ATS optimisation.
```

---

## Sample Use Cases

- Data Analyst Applications
- Data Science Roles
- Machine Learning Engineer Positions
- AI Engineer Applications
- Resume Optimisation
- ATS Preparation

---

## Limitations

- Currently analyses only PDF resumes.
- Analysis is based primarily on the first page of the uploaded resume.
- ATS scores are AI-generated estimates and may differ from commercial ATS platforms.
- Results depend on the quality of the resume and job description provided.

---

## Future Improvements

- Multi-page resume analysis
- DOCX support
- Downloadable feedback reports
- Resume scoring dashboard
- Cover letter analysis
- LinkedIn profile evaluation
- Industry-specific ATS scoring

---

## Disclaimer

This project is intended for educational and career-development purposes only. The AI-generated feedback and ATS scores are recommendations and should not be considered official recruitment decisions.

---

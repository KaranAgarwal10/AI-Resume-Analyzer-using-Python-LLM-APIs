# 🚀 AI Resume Analyzer (RAG-based)

This project is an AI-powered Resume Analyzer built using Python and LLM APIs. It reads a resume (PDF) and provides structured feedback including strengths, weaknesses, missing skills, and suggestions based on a specific job role.

---

## ✨ Features

- 📄 Reads resume from PDF
- 🤖 AI-powered analysis using LLM API
- 🎯 Job role-based evaluation
- 📊 Provides:
  - Strengths
  - Weaknesses
  - Missing Skills
  - Suggestions
  - Overall Score (out of 10)
- 💾 Saves analysis to a file (`analysis.txt`)

---

## 🛠️ Tech Stack

- Python
- pypdf (PDF reading)
- Requests (API calls)
- OpenRouter (LLM API)

---

## 📂 Project Structure
resume-analyzer/
│── app.py
│── resume.pdf
│── analysis.txt
│── requirements.txt
│── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository

### 2. Install dependencies
pip install -r requirements.txt

### 3. Add your API Key

Open `app.py` and replace:
API_KEY = "YOUR_OPENROUTER_API_KEY"


---

### 4. Add your resume
Place your resume file in the project folder as:

---

### 5. Run the project


---

## 🧠 How it works

User input (job role)  
→ Resume PDF is read  
→ Sent to LLM API  
→ AI analyzes content  
→ Output displayed + saved  

---

## 📌 Example Output

- Strengths
- Weaknesses
- Missing Skills
- Suggestions
- Score (out of 10)

---

## 🚀 Future Improvements

- Web interface using Streamlit
- Upload multiple resumes
- Resume comparison feature
- ATS score integration

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## ⭐ Show your support

If you found this helpful, give it a ⭐ on GitHub!

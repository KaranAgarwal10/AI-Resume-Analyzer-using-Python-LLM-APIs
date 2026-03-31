import requests
from pypdf import PdfReader

# ==============================
# STEP 1: READ PDF
# ==============================
reader = PdfReader("resume.pdf")
text = ""

for page in reader.pages:
    text += page.extract_text()

# ==============================
# STEP 2: USER INPUT (JOB ROLE)
# ==============================
job_role = input("Enter job role (e.g. Software Engineer): ")

# ==============================
# STEP 3: API KEY
# ==============================
API_KEY = "ADD your OpenRouter API key here."

# ==============================
# STEP 4: PROMPT
# ==============================
prompt = f"""
Analyze this resume for the role of {job_role}:

{text}

Give:
1. Strengths
2. Weaknesses
3. Missing skills for this role
4. Suggestions
5. Overall Score (out of 10)
"""

# ==============================
# STEP 5: API REQUEST
# ==============================
response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
)

data = response.json()

# ==============================
# STEP 6: HANDLE RESPONSE
# ==============================
if "choices" in data:
    result = data["choices"][0]["message"]["content"]

    print("\n===== AI ANALYSIS =====\n")
    print(result)

    # ==============================
    # STEP 7: SAVE TO FILE
    # ==============================
    with open("analysis.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("\n✅ Analysis saved to analysis.txt")

else:
    print("❌ Error:", data)

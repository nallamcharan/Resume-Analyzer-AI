# 🤖 AI Resume Analyzer
An intelligent **AI-powered Resume Analyzer** built using **Streamlit + LangChain + Hugging Face**.
This application helps users analyze their resumes against job descriptions and provides actionable insights like ATS score, missing skills, and improvement suggestions.

## 🚀 Features

* 📄 Upload Resume (PDF, DOCX, TXT)
* 🧠 AI-based Resume Analysis
* 📊 ATS Score (1–100)
* 🔍 Missing Keywords Detection
* 💡 Strong Suggestions for Improvement
* ✨ Clean and interactive UI using Streamlit
* 
## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **LLM Integration:** LangChain
* **Model Provider:** Hugging Face
* **Libraries:**

  * pypdf
  * python-docx
  * langchain-huggingface

## 🧠 How It Works

1. User uploads a resume
2. Text is extracted from the file
3. User provides a job description
4. AI model analyzes resume vs job description
5. Outputs:

   * ATS Score
   * Missing Keywords
   * Suggestions
   * Improvements

## 📸 Demo

<img src="Screenshot 2026-03-23 225545.png"  alt="Description of image" width="400" height="auto">
<img src="Screenshot 2026-03-23 230422.png"  alt="Description of image" width="400" height="auto">
<img src="Screenshot 2026-03-23 230400.png"  alt="Description of image" width="400" height="auto">

## 🚀 Future Improvements

* 🧾 Resume rewriting suggestions
* 🌐 Deployment with Streamlit Cloud

## ⚙️ Installation

## 1️⃣ Clone the Repository

git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

### 2️⃣ Install Dependencies

pip install -r requirements.txt

## 3️⃣ Set Environment Variable

⚠️ Do NOT hardcode your API key.

export HUGGINGFACEHUB_API_TOKEN="your_api_token"

## 4️⃣ Run the App

streamlit run app.py



# 🤖 Auto-Tailor: AI Cover Letter Generator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Gemini API](https://img.shields.io/badge/AI-Google%20Gemini-orange)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Stop writing generic cover letters.** Let Python and AI write tailored, professional applications for you in seconds.

## 🚀 What is Auto-Tailor?
Auto-Tailor is a CLI tool that completely automates the job application process. It reads your **Resume (PDF)** and a target **Job Description**, analyzes them using **Google's Gemini 1.5/Pro AI**, and generates a highly persuasive, professional cover letter.

It doesn't just fill in blanks—it studies your experience and explains *why* you are the perfect fit for the specific role.

## ✨ Key Features
- **📄 Smart PDF Parsing:** Extracts text directly from your `resume.pdf`.
- **🧠 Auto-Discovery Model:** Automatically finds and uses the best available Gemini model (Flash, Pro, or Ultra).
- **🔒 Privacy First:** Your personal data and API keys are stored locally in a `.env` file. Nothing is hardcoded or uploaded to the cloud.
- **🖨️ Professional PDF:** Outputs a clean, formatted `Cover_Letter.pdf` ready for submission.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **AI Engine:** Google Gemini (via REST API)
- **Libraries:** `pypdf`, `fpdf`, `requests`, `python-dotenv`, `rich`

---

## 📖 How to Use

### 1. Prerequisites
- Python installed on your system.
- A **Free API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 2. Installation
Clone the repository and install the required libraries:

```bash
git clone [https://github.com/500daysofansh/Auto-Tailor.git](https://github.com/500daysofansh/Auto-Tailor.git)
cd Auto-Tailor
pip install -r requirements.txt

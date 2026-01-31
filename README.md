# 🤖 Auto-Tailor: AI Cover Letter Generator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Gemini API](https://img.shields.io/badge/AI-Google%20Gemini-orange)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Stop writing generic cover letters.** Let Python and AI write tailored, professional applications for you in seconds.

## 🚀 What is Auto-Tailor?
Auto-Tailor is a CLI tool that automates the job application process. It reads your **Resume (PDF)** and a target **Job Description**, analyzes them using **Google's Gemini AI**, and generates a highly persuasive, professional cover letter.

It doesn't just fill in blanks—it studies your experience and explains *why* you are the perfect fit for the specific role based on the job requirements.

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
3. Setup Your Secrets (.env)
To keep your data safe, create a file named .env in the project folder and add your details. The script will pull your name and contact info from here to generate the PDF header.

Paste this into your .env file:

Ini, TOML
# 1. Your Google AI Key
GEMINI_API_KEY=Paste_Your_Key_Here

# 2. Your Header Details (Replace these with your own info)
MY_NAME=Your Full Name
MY_CONTACT_1=City, State | +91-0000000000
MY_CONTACT_2=email@example.com | [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
MY_GITHUB=[github.com/yourusername](https://github.com/yourusername)
4. Prepare Input Files
Resume: Place your resume.pdf in the main folder.

Job Description: Copy the job post text into a file named job.txt.

5. Run the Tool
Bash
python main.py
6. Result
The AI will analyze your files and print a preview in the terminal. ✅ A ready-to-send file named Cover_Letter.pdf will be generated in your folder.

⚠️ Troubleshooting
Error: 404 Model Not Found? The script is designed to handle this. It will auto-retry with different model names until one works.

Git Error? Ensure you have a .gitignore file so you don't upload your .env keys.

Created by Anshuman Singh

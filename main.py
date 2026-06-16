import os
import requests
import json
from datetime import date
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from fpdf import FPDF
from pypdf import PdfReader

# 1. Setup - Load Safe Environment Variables
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))
console = Console()
api_key = os.getenv("GEMINI_API_KEY")

# Load Personal Info safely from .env
# If .env is missing, these defaults will show (safe for GitHub)
MY_NAME = os.getenv("MY_NAME", "[Your Name]")
MY_CONTACT_1 = os.getenv("MY_CONTACT_1", "[City, State | Phone]")
MY_CONTACT_2 = os.getenv("MY_CONTACT_2", "[Email | LinkedIn]")
MY_GITHUB = os.getenv("MY_GITHUB", "[GitHub URL]")

if not api_key:
    console.print("[bold red]❌ Error: API Key not found. Check your .env file![/bold red]")
    exit()

# 2. PDF Generator
def create_pdf(body_text, filename="Cover_Letter.pdf"):
    save_path = os.path.join(SCRIPT_DIR, filename)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- HEADER SECTION (Dynamic & Safe) ---
    
    # 1. Name (BOLD)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, MY_NAME, ln=True, align='C')
    
    # 2. Contact Info (Regular)
    pdf.set_font("Helvetica", size=10)
    pdf.cell(0, 5, MY_CONTACT_1, ln=True, align='C')
    pdf.cell(0, 5, MY_CONTACT_2, ln=True, align='C')
    pdf.cell(0, 5, MY_GITHUB, ln=True, align='C')
    
    # 3. Date
    pdf.ln(10)
    pdf.set_font("Helvetica", size=11)
    today = date.today().strftime("%B %d, %Y")
    pdf.cell(0, 10, f"Date: {today}", ln=True)
    
    # 4. Subject Line
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 10, "Subject: Application for Software Developer Position", ln=True)
    pdf.ln(5)

    # --- BODY SECTION ---
    pdf.set_font("Helvetica", size=11)
    
    # Clean up AI formatting
    clean_text = body_text.replace("**", "").replace("##", "")
    clean_text = clean_text.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 6, clean_text)
    
    pdf.output(save_path)
    console.print(f"[bold green]✅ Professional PDF Saved as: {save_path}[/bold green]")

# 3. PDF Reader
def read_resume_file():
    pdf_path = os.path.join(SCRIPT_DIR, "resume.pdf")
    txt_path = os.path.join(SCRIPT_DIR, "resume.txt")

    if os.path.exists(pdf_path):
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            console.print(f"[red]⚠️ Error reading PDF: {e}[/red]")
    
    if os.path.exists(txt_path):
        with open(txt_path, "r", encoding="utf-8") as f:
            return f.read()
            
    return None

# 4. AI Brain (Auto-Discovery)
def find_and_use_model(prompt):
    base_url = "https://generativelanguage.googleapis.com/v1beta"
    models_url = f"{base_url}/models?key={api_key}"
    
    try:
        response = requests.get(models_url)
        data = response.json()
        
        valid_model = None
        for m in data.get('models', []):
            if "generateContent" in m['supportedGenerationMethods'] and "gemini" in m['name']:
                valid_model = m['name']
                break
        
        if not valid_model:
            return None

        generate_url = f"{base_url}/{valid_model}:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        payload = {"contents": [{"parts": [{"text": prompt}]}]}

        gen_response = requests.post(generate_url, headers=headers, json=payload)
        
        if gen_response.status_code == 200:
            return gen_response.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            console.print(f"[bold red]❌ Google AI Error:[/bold red] {gen_response.text}")
            return None

    except Exception as e:
        console.print(f"[bold red]❌ Network Error:[/bold red] {e}")
        return None

# 5. Main Logic
def generate_cover_letter():
    console.print(Panel("[bold green]🤖 Auto-Tailor v3.0 (Safe Mode)[/bold green]", title="System Ready"))

    resume_text = read_resume_file()
    if not resume_text:
        console.print(f"[bold red]❌ No resume found in: {SCRIPT_DIR}[/bold red]")
        return

    job_path = os.path.join(SCRIPT_DIR, "job.txt")
    if not os.path.exists(job_path):
        console.print(f"[bold red]❌ No job.txt found in: {SCRIPT_DIR}[/bold red]")
        return
        
    with open(job_path, "r", encoding="utf-8") as f:
        job_text = f.read()

    # The Prompt - Dynamic Signature
    prompt = f"""
    I am applying for a job.
    MY RESUME TEXT: {resume_text}
    JOB DESCRIPTION: {job_text}
    
    TASK:
    Write the BODY of a professional cover letter.
    
    RULES:
    1. Do NOT write the header (Name, Date, Address). Start directly with "Dear Hiring Team,".
    2. Do NOT use markdown bolding (like **text**). Use plain text only.
    3. Do NOT use placeholders like [Date] or [Your Name].
    4. Sign it as "Sincerely,\n{MY_NAME}".
    5. Keep it under 250 words.
    """

    console.print("[yellow]⏳ AI is analyzing your PDF...[/yellow]")
    
    text = find_and_use_model(prompt)
    if text:
        console.print(Panel(text, title="✨ Preview", border_style="cyan"))
        create_pdf(text)

if __name__ == "__main__":
    generate_cover_letter()
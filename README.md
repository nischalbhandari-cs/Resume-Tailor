# 📄 AI Resume Tailor (AI-Powered Resume Analyzer)

Welcome to my AI Resume Tailor project! This Python application compares a resume with a job description using the Google Gemini API and provides personalized feedback to improve job matching.

## 🎓 Learning Journey

As an aspiring AI Software Engineer, I built this project to gain hands-on experience with:

- API integration with Google Gemini
- Prompt engineering
- Environment variables and security
- File handling in Python
- AI-powered automation

## 🚀 Features

- Reads resume and job description from text files
- Uses Google Gemini AI for analysis
- Generates match score out of 100
- Shows missing keywords and skills
- Provides resume improvement suggestions
- Password protected access
- Secure API key storage using .env

## ⚙️ How to Setup & Run

### Step 1: Create .env file
```
GEMINI_API_KEY=your_actual_key_here
API_PASSWORD=your_password
```

### Step 2: Create required files
Add your resume inside resume.txt
Add job description inside job_description.txt

### Step 3: Install dependencies
```
pip install google-generativeai python-dotenv
```

### Step 4: Run the program
```
python main.py
```

## 🧠 Code Breakdown

**load_dotenv**
Loads environment variables securely from .env file.

**os.getenv**
Retrieves API key and password securely.

**genai.configure**
Authenticates the Gemini API connection.

**generate_content**
Sends resume and job description to Gemini AI for analysis.

**try...except**
Handles errors gracefully and prevents crashes.

**File Handling**
Reads resume and job description from text files.

## 🔮 Future Improvements

- Add GUI interface
- Export analysis results to PDF
- Support .docx and PDF resumes
- Build web version using Flask

## ⚠️ Note

This project was built for learning purposes.
Some parts of development were assisted using AI tools.

## 👨‍💻 Created By

Nischal Bhandari
GitHub: github.com/nischalbhandari-cs

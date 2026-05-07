AI Resume Tailor (AI-Powered Resume Analyzer)
Welcome to my AI-powered Resume Tailor project!
This Python application compares a resume with a job description using the Google Gemini API and provides personalized feedback to improve job matching.

The tool analyzes:

Resume-job match score
Missing skills/keywords
Resume improvement suggestions
🎓 Learning Journey
As a Computer Science student, I built this project to gain hands-on experience with:

API integration
Prompt engineering
Environment variables
File handling
AI-powered automation
This project helped me move beyond beginner Python programs into practical AI-based applications.

I also learned how to:

Handle API authentication
Process AI-generated responses
Work with structured prompts
Improve error handling in Python
🚀 Features
Reads resume and job description from text files
Uses Google Gemini AI for analysis
Generates:
Match score (0–100)
Missing keywords/skills
Resume improvement suggestions
Password-protected access using .env
Simple command-line interface
📂 Project Structure
ResumeTailor/
│
├── main.py
├── resume.txt
├── job_description.txt
├── .env
├── README.md
⚙️ How to Setup & Run
To protect private credentials, the .env file is not included in this repository.

Step 1: Create .env file
GEMINI_API_KEY=your_actual_key_here
API_PASSWORD=your_security_password
Step 2: Create required files
Create:

resume.txt
job_description.txt
Paste your resume and job description inside them.

Step 3: Install dependencies
pip install google-generativeai python-dotenv
Step 4: Run the program
python main.py
🧠 Code Breakdown
dotenv (load_dotenv)
Loads environment variables securely from the .env file.

os.getenv
Retrieves stored values like API keys and passwords.

genai.configure
Authenticates the Gemini API connection using the API key.

GenerativeModel
Represents the Gemini AI model used in the project.

generate_content
Sends the prompt to Gemini AI and receives analysis results.

try...except
Handles errors gracefully and prevents program crashes.

File Handling
Reads resume and job description from text files.

Prompt Engineering
Structures input prompts to get better AI responses.

🔮 Future Improvements
Add graphical user interface (GUI)
Export analysis results to PDF
Support .docx and PDF resumes
Build a web version using Flask
⚠️ Note
This project was built for learning purposes.

Some parts of development were assisted using AI tools (Google Gemini).

👨‍💻 Created By
Nischal Bhandari
GitHub: github.com/nischalbhandari-cs

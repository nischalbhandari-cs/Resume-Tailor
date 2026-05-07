import os 
from dotenv  import load_dotenv 
import google.generativeai as genai  

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#get api key from the env file 
load_dotenv() 

# function 

def resume_tailor(): 
    # read both files 
    with open("resume.txt", "r") as f1, open("job_description.txt", "r") as f2:
        my_resume=f1.read()
        job_descrip= f2.read() 

    
    # configure and connect with gemini 
    api_key= os.getenv("GEMINI_API_KEY") 
    api_password= os.getenv("API_PASSWORD") 

    #ask for password 
    user_input=input("Enter the password to access: ") 

    if user_input==api_password:
        print("Access Granted!!") 
    else:
        print("Incorrect password. Access is not granted.") 
        return

    #configure gemini ai 
    genai.configure(api_key=os.getenv("GEMINI_API_KEY")) 
    model= genai.GenerativeModel("gemini-2.0-flash") 

    #Construct the prompt now 
    prompt= f""" 
    Analyze the resume for the following job description 

    RESUME:
    {my_resume} 

    JOB DESCRIPTION: 
    {job_descrip} 

    Based on the following provide:
        1. A match score(0-100)
        2.A list of 3 missing keywords or skill i should add 
        3.One specific point from my resume to better match the job 

    """ 

    #send to api  
    print("Analyzing your resume please wait: ") 

    try:
        response=model.generate_content(prompt)
        print("\n" + "=" *30 ) 
        print("AI analysis is completed") 
        print("=" *30 + "\n") 
        print(response.text) 

    except Exception as e:
        print(f" AN error has occured: {e}")

if __name__=="__main__":
    resume_tailor() 

# AI Resume Analyzer

This project will help you build a simple AI-powered app that:
- uploads a resume
- reads the job description
- extracts skills and experience
- compares the resume to the role
- gives a match score and feedback

## Step-by-step plan
1. Set up the Python project and dependencies.
2. Build a resume text extractor.
3. Build a skills-matching engine.
4. Add an AI summary using an LLM.
5. Create a simple Streamlit interface.

## Run the app
Install the dependencies into the project virtual environment, then launch Streamlit with that same environment:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open http://localhost:8501 in your browser if it does not open automatically. Keep the terminal running while you use the app.

You can also double-click `run_app.bat` to start the app with the project environment.

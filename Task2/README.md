# Task 2: AI-Powered Customer Service Agent

This project demonstrates a simple automated customer service system using the Google Gemini 1.5 Flash API. It reads customer complaints from a JSON file and generates professional, empathetic responses.

## Project Structure
- `app.py`: The main Python script that connects to the Gemini API and processes complaints.
- `eval_set.json`: A test dataset containing 5 different customer complaint scenarios.
- `prompts.md`: Documentation of the prompt engineering process and iterations.
- `report.md`: A brief report covering the use case, model choice, and reflections.
- `test_results.txt`: (Generated after running) The final output containing AI replies.

## How to Run
1. **Clone the repository** (or download the files).
2. **Install dependencies**:
   ```bash
   pip install -U google-generativeai
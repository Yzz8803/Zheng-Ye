import os
import warnings
import google.generativeai as genai
import json

# 1. Silence all Python & gRPC warnings for a clean console
warnings.filterwarnings("ignore")
os.environ["GRPC_VERBOSITY"] = "ERROR"

# 2. Configure API Key
genai.configure(api_key="YOUR_API_KEY")

# 3. Initialize Model
model = genai.GenerativeModel('gemini-1.5-flash')
def get_ai_response(complaint_text):
    """
    Calls Gemini API to generate a professional customer service reply.
    """
    prompt = f"You are a professional customer service agent. Please reply to this complaint politely: {complaint_text}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as error:
        return f"AI Error: {error}"

def main():
    print(">>> Starting Task 2 Automation...")
    
    # --- Load Test Cases ---
    try:
        with open('eval_set.json', 'r', encoding='utf-8') as f:
            test_cases = json.load(f)
    except Exception as error:
        print(f"FAILED: Could not read JSON file. Error: {error}")
        return

    all_results = []

    # --- Processing Loop ---
    print(f">>> Found {len(test_cases)} cases. Processing now...")
    
    for case in test_cases:
        case_id = case.get('id')
        user_input = case.get('customer_input')
        
        print(f"--- Processing Case ID: {case_id} ---")
        ai_reply = get_ai_response(user_input)
        
        all_results.append({
            "id": case_id,
            "input": user_input,
            "output": ai_reply
        })

    # --- Write Results to File ---
    try:
        output_filename = "test_results.txt"
        with open(output_filename, 'w', encoding='utf-8') as f:
            for item in all_results:
                f.write(f"CASE ID: {item['id']}\n")
                f.write(f"CUSTOMER INPUT: {item['input']}\n")
                f.write(f"AI RESPONSE: {item['output']}\n")
                f.write("=" * 40 + "\n")
        
        print(">>> SUCCESS: All cases processed.")
        print(f">>> Output saved to: {output_filename}")
        
    except Exception as error:
        print(f"FAILED: Could not save output file. Error: {error}")

if __name__ == "__main__":
    main()
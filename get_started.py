# agent.py

import os
import google.generativeai as genai

# === Configuration ===
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# === Gemini Model Setup ===
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  
    generation_config={
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 1024,
    }
)

# === Create Chat Session with History ===
chat = model.start_chat(history=[])


# === Optional: Expression Evaluator Tool ===
import subprocess
import os

def run_evaluator(expression):
    evaluator_path = os.path.join("..", "tools", "evaluate.exe")  # For Windows

    try:
        result = subprocess.run(
            [evaluator_path, expression],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"⚠️ Evaluator error: {e.stderr}"
    except FileNotFoundError:
        return "❌ Evaluator binary not found. Make sure evaluate.exe is compiled."



def handle_user_input(user_input: str):
    prompt = f"""
You are a CERN AI assistant.
Your job is to convert the user's question into a symbolic math or physics expression.
Respond with:
- A natural explanation
- The expression in valid math form
- Then write: EVALUATE: <expression> if it's ready to be computed

Question: {user_input}
"""

    response = chat.send_message(prompt)
    print("\n🤖 Gemini Agent:\n", response.text)

    if "EVALUATE:" in response.text:
        try:
            expression = response.text.split("EVALUATE:")[1].strip().split('\n')[0]
            print("\n🔧 Calling evaluator with:", expression)

            eval_result = run_evaluator(expression)  
            print("\n✅ Evaluated Result:", eval_result)
        except Exception as e:
            print("⚠️ Error evaluating expression:", e)

    print("\n" + "=" * 50 + "\n")



def run_agent():
    print("🔬 CERN Agentic AI is running. Type 'exit' to quit.\n")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        handle_user_input(user_input)



if __name__ == "__main__":
    run_agent()

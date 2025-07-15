import openai
import os
from dotenv import load_dotenv
from utils import read_code, save_code

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def modify_code(modification_instruction):
    current_code = read_code("generated_code/app.py")

    system_message = "You're an expert Python code refiner. Apply the user's changes safely and correctly to the existing code."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"Original code:\n{current_code}\n\nModify it as per:\n{modification_instruction}"}
        ],
        temperature=0.3
    )

    updated_code = response['choices'][0]['message']['content']
    save_code("generated_code/app.py", updated_code)
    return updated_code

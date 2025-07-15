import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code(prompt):
    system_message = "You're a powerful Python application generator. Generate clear, complete code for the user's app idea. Add comments. Make it production-ready."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    code = response['choices'][0]['message']['content']
    return code

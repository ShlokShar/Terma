import openai
import platform
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("AI_API")


def return_command(user_input: str) -> str:
    os_info = platform.system()
    prompt = (
        f"Convert this natural language request into a safe, standard shell command "
        f"for {os_info}: \"{user_input}\".\n\nCommand:"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response["choices"][0]["message"]["content"].strip()

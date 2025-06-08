import subprocess
import platform
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("AI_API"))


def is_command_available(command: str) -> bool:
    try:
        subprocess.run([command, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False


def return_command(user_input: str) -> str:
    os_info = platform.system()

    package_managers = []
    if is_command_available("brew"):
        package_managers.append("Homebrew (brew)")
    if is_command_available("apt"):
        package_managers.append("APT (apt)")
    if is_command_available("dnf"):
        package_managers.append("DNF (dnf)")
    if is_command_available("yum"):
        package_managers.append("YUM (yum)")

    if not package_managers:
        package_managers.append("No package manager detected.")

    prompt = (
        f"Convert this natural language request into a safe, standard shell command(s). Make sure to fulfill all requirements listed. "
        f"for {os_info}. The following package managers are available: {', '.join(package_managers)}.\n"
        f"Request: \"{user_input}\"\n\n"
        f"Prefer built-in system tools or native commands (e.g., 'python --version' instead of relying on a package manager). "
        f"Only fall back to package managers like {', '.join(package_managers)} if there is no native way.\n"
        f"Output only the shell command(s). If multiple commands are needed (e.g., to check availability or install), separate them with '&&'."
        f"\n\nCommand(s):"
    )

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150,
        temperature=0
    )

    return response.choices[0].text.strip()

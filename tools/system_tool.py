import os
import platform
import subprocess
import sys


def get_system_info():
    return f"""
System : {platform.system()}
Release : {platform.release()}
Python : {sys.version.split()[0]}
Current Folder :
{os.getcwd()}
"""


def run_system_command(command):
    """
    Execute safe system commands.
    """

    allowed_commands = {
        "pwd": ["pwd"],
        "ls": ["ls"],
        "whoami": ["whoami"],
        "which python3": ["which", "python3"],
        "which pip": ["which", "pip"],
        "python3 --version": ["python3", "--version"],
        "pip --version": ["pip", "--version"],
    }

    command = command.strip().lower()

    if command not in allowed_commands:
        return None

    try:
        result = subprocess.run(
            allowed_commands[command],
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout.strip()

    except Exception as e:
        return str(e)
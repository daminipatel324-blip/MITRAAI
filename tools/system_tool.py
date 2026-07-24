import platform
import os
import sys


def get_system_info():
    return f"""
System : {platform.system()}
Release : {platform.release()}
Python : {sys.version.split()[0]}
Current Folder :
{os.getcwd()}
"""
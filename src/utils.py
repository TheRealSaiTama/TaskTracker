from datetime import datetime, UTC
import os

DATEFORMAT = "%Y-%m-%d %H:%M:%S"
CURRENTUSER = "TheRealSaiTama"

def getcurrenttime():
    return datetime.now(UTC).strftime(DATEFORMAT)

def validatedescription(description):
    if not description or len(description.strip()) == 0:
        raise ValueError("Task description cannot be empty")
    if len(description) > 200:
        raise ValueError("Task description too long (max 200 characters)")
    return description.strip()

def validatestatus(status):
    validstatuses = ["todo", "inprogress", "done"]
    if status not in validstatuses:
        raise ValueError(f"Invalid status. Must be one of: {', '.join(validstatuses)}")
    return status

def formatstatus(status):
    statuscolors = {
        "todo": "\033[91m",
        "inprogress": "\033[93m",
        "done": "\033[92m"
    }
    resetcolor = "\033[0m"
    return f"{statuscolors[status]}{status.upper()}{resetcolor}"

def printerror(message):
    print(f"\033[91mError: {message}\033[0m")

def printsuccess(message):
    print(f"\033[92mSuccess: {message}\033[0m")

def ensuredirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)
import os
from dotenv import load_dotenv

load_dotenv()

# -------------------------

# WEBSITES

# -------------------------

WEBSITES = {
"youtube": "https://www.youtube.com",
"google": "https://www.google.com",
"github": "https://www.github.com",
"chatgpt": "https://chatgpt.com",
"leetcode": "https://leetcode.com",
"facebook": "https://www.facebook.com",
"instagram": "https://www.instagram.com",
"wikipedia": "https://www.wikipedia.org",
"reddit": "https://www.reddit.com",
"linkedin": "https://www.linkedin.com",
"gmail": "https://mail.google.com",
"spotify": "https://open.spotify.com",
}

# -------------------------

# APPS

# Add your manual app paths here if needed

# -------------------------

APPS = {
"notepad": "notepad.exe",
"calculator": "calc.exe",
"calc": "calc.exe",
"paint": "mspaint.exe",
"cmd": "cmd.exe",
# Example:
# "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
# "vscode": r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",
}

home = os.path.expanduser("~")

# -------------------------

# FILE SEARCH FOLDERS

# -------------------------

SEARCH_FOLDERS = [
os.path.join(home, "Desktop"),
os.path.join(home, "Documents"),
os.path.join(home, "Downloads"),
os.path.join(home, "Pictures"),
os.path.join(home, "Videos"),


os.path.join(home, "OneDrive", "Desktop"),
os.path.join(home, "OneDrive", "Documents"),
os.path.join(home, "OneDrive", "Downloads"),
os.path.join(home, "OneDrive", "Pictures"),
os.path.join(home, "OneDrive", "Videos"),

os.path.join(home, "OneDrive", "ドキュメント"),


]

# -------------------------

# START MENU FOLDERS FOR APP SEARCH

# -------------------------

START_MENU_FOLDERS = [
r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
os.path.join(
os.environ.get("APPDATA", ""),
r"Microsoft\Windows\Start Menu\Programs"
),
]

# -------------------------

# COMMON APP INSTALL LOCATIONS

# -------------------------

APP_SEARCH_FOLDERS = [
r"C:\Program Files",
r"C:\Program Files (x86)",
os.path.join(home, "AppData", "Local"),
]

# -------------------------

# SPECIAL FOLDERS

# -------------------------

SPECIAL_FOLDERS = {
"desktop": os.path.join(home, "Desktop"),
"documents": os.path.join(home, "Documents"),
"downloads": os.path.join(home, "Downloads"),
"pictures": os.path.join(home, "Pictures"),
"videos": os.path.join(home, "Videos"),
}

PROJECT_ROOT = os.getcwd()
SCREENSHOTS_FOLDER = os.path.join(PROJECT_ROOT, "screenshots")

# -------------------------

# AI CONFIG

# -------------------------

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")

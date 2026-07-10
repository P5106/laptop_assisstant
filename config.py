import os

WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://www.github.com",
    "chatgpt": "https://chat.openai.com",
    "leetcode": "https://leetcode.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "wikipedia": "https://www.wikipedia.org",
    "reddit": "https://www.reddit.com",
    "linkedin": "https://www.linkedin.com",
    "gmail": "https://mail.google.com",
}

APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
}

home = os.path.expanduser("~")

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

START_MENU_FOLDERS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.join(
        os.environ.get("APPDATA", ""),
        r"Microsoft\Windows\Start Menu\Programs"
    ),
]

APP_SEARCH_FOLDERS = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    os.path.join(home, "AppData", "Local"),
]

SPECIAL_FOLDERS = {
    "desktop": os.path.join(home, "Desktop"),
    "documents": os.path.join(home, "Documents"),
    "downloads": os.path.join(home, "Downloads"),
    "pictures": os.path.join(home, "Pictures"),
    "videos": os.path.join(home, "Videos"),
}

# Screenshot folder inside your project
PROJECT_ROOT = os.getcwd()
SCREENSHOTS_FOLDER = os.path.join(PROJECT_ROOT, "screenshots")
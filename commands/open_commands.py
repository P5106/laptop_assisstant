import os
import webbrowser
import subprocess
from urllib.parse import quote

from config import (
    WEBSITES,
    APPS,
    SEARCH_FOLDERS,
    START_MENU_FOLDERS,
    APP_SEARCH_FOLDERS,
    SPECIAL_FOLDERS,
)
from voice import speak


# =========================================================
# SEARCH / FIND HELPERS
# =========================================================
def find_path_by_name(target_name):
    target_name = target_name.lower().strip()

    for base_folder in SEARCH_FOLDERS:
        if not os.path.exists(base_folder):
            continue

        for root, dirs, files in os.walk(base_folder):
            for folder in dirs:
                if target_name in folder.lower():
                    return os.path.join(root, folder)

            for file in files:
                if target_name in file.lower():
                    return os.path.join(root, file)

    return None


def find_app_in_start_menu(app_name):
    app_name = app_name.lower().strip()

    for base_folder in START_MENU_FOLDERS:
        if not base_folder or not os.path.exists(base_folder):
            continue

        for root, dirs, files in os.walk(base_folder):
            for file in files:
                file_lower = file.lower()
                if app_name in file_lower and (file_lower.endswith(".lnk") or file_lower.endswith(".exe")):
                    return os.path.join(root, file)

    return None


def find_exe_in_common_locations(app_name):
    app_name = app_name.lower().strip()

    for base_folder in APP_SEARCH_FOLDERS:
        if not base_folder or not os.path.exists(base_folder):
            continue

        for root, dirs, files in os.walk(base_folder):
            for file in files:
                file_lower = file.lower()

                if file_lower == f"{app_name}.exe":
                    return os.path.join(root, file)

                if app_name in file_lower and file_lower.endswith(".exe"):
                    return os.path.join(root, file)

    return None


def find_app_path(app_name):
    path = find_app_in_start_menu(app_name)
    if path:
        return path

    path = find_exe_in_common_locations(app_name)
    if path:
        return path

    return None


# =========================================================
# WEBSITE / SEARCH
# =========================================================
def open_website(name):
    name = name.lower().strip()

    if name in WEBSITES:
        webbrowser.open(WEBSITES[name])
        speak(f"Opening {name}")
        return True

    if "." in name:
        url = name
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)
        speak(f"Opening {name}")
        return True

    url = f"https://www.{name}.com"
    webbrowser.open(url)
    speak(f"Opening {name}")
    return True


def search_google(query):
    query = query.strip()
    if not query:
        speak("What should I search on Google?")
        return
    url = f"https://www.google.com/search?q={quote(query)}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")


def search_youtube(query):
    query = query.strip()
    if not query:
        speak("What should I search on YouTube?")
        return
    url = f"https://www.youtube.com/results?search_query={quote(query)}"
    webbrowser.open(url)
    speak(f"Searching YouTube for {query}")


# =========================================================
# OPEN APP / FILE / SMART OPEN
# =========================================================
def open_special_windows_app(name):
    name = name.lower().strip()

    special_apps = {
        "camera": "start microsoft.windows.camera:",
        "settings": "start ms-settings:",
        "photos": "start ms-photos:",
    }

    if name in special_apps:
        os.system(special_apps[name])
        speak(f"Opening {name}")
        return True

    return False


def open_app(name):
    name = name.lower().strip()

    try:
        if open_special_windows_app(name):
            return True
    except Exception as e:
        print("Special app error:", e)

    if name in APPS:
        try:
            app_path = APPS[name]

            if app_path.endswith(".exe") and "\\" not in app_path and "/" not in app_path:
                subprocess.Popen(app_path)
            else:
                os.startfile(app_path)

            speak(f"Opening {name}")
            return True
        except Exception as e:
            speak(f"Could not open {name}")
            print("Error:", e)
            return False

    found_app = find_app_path(name)
    if found_app:
        try:
            os.startfile(found_app)
            speak(f"Opening {name}")
            print("Opened app path:", found_app)
            return True
        except Exception as e:
            speak(f"Could not open {name}")
            print("Error:", e)
            return False

    speak(f"App {name} not found")
    return False


def open_file(name):
    name = name.lower().strip()

    if name in SPECIAL_FOLDERS:
        folder_path = SPECIAL_FOLDERS[name]
        if os.path.exists(folder_path):
            os.startfile(folder_path)
            speak(f"Opening {name}")
            return True

    found_path = find_path_by_name(name)
    if found_path:
        try:
            os.startfile(found_path)
            speak(f"Opening {name}")
            print("Opened path:", found_path)
            return True
        except Exception as e:
            speak(f"Could not open {name}")
            print("Error:", e)
            return False

    speak(f"File or folder {name} not found")
    return False


def smart_open(name):
    name = name.lower().strip()

    if name in WEBSITES:
        return open_website(name)

    if open_app(name):
        return True

    if open_file(name):
        return True

    if "." in name or " " not in name:
        try:
            open_website(name)
            return True
        except Exception:
            pass

    speak(f"I could not find {name}")
    return False
import webbrowser
import os
import subprocess
from urllib.parse import quote
from datetime import datetime

from config import WEBSITES, APPS, SPECIAL_FOLDERS
from search_utils import find_path_by_name, find_app_path, suggest_similar_name
from voice import speak


# ---------------------------
# OPEN WEBSITE
# ---------------------------
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


# ---------------------------
# OPEN SPECIAL WINDOWS APPS
# ---------------------------
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


# ---------------------------
# OPEN APP
# ---------------------------
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

    return False


# ---------------------------
# OPEN FILE / FOLDER
# ---------------------------
def open_file(name):
    name = name.lower().strip()

    from config import SCREENSHOTS_FOLDER

    # open screenshots folder
    if name == "screenshots":
        try:
            os.makedirs(SCREENSHOTS_FOLDER, exist_ok=True)
            os.startfile(SCREENSHOTS_FOLDER)
            speak("Opening screenshots folder")
            return True
        except Exception as e:
            speak("Could not open screenshots folder")
            print("Error:", e)
            return False

    # open special folders like desktop/downloads/documents
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

    return False

# ---------------------------
# SMART OPEN
# ---------------------------
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

    suggestions = suggest_similar_name(name)
    if suggestions:
        speak(f"I could not find {name}. Did you mean {', '.join(suggestions)}?")
    else:
        speak(f"I could not find {name}")

    return False


# ---------------------------
# GOOGLE / YOUTUBE SEARCH
# ---------------------------
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


# ---------------------------
# TIME / DATE
# ---------------------------
def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    message = f"The time is {current_time}"
    speak(message)


def tell_date():
    current_date = datetime.now().strftime("%d %B %Y")
    message = f"Today's date is {current_date}"
    speak(message)

# ---------------------------
# SCREENSHOT
# ---------------------------
def take_screenshot(location=None):
    try:
        import pyautogui
        from datetime import datetime
        import os
        from config import SCREENSHOTS_FOLDER, SPECIAL_FOLDERS

        # default save folder
        save_folder = SCREENSHOTS_FOLDER

        # if user said desktop/downloads/documents etc.
        if location:
            location = location.lower().strip()
            if location in SPECIAL_FOLDERS and os.path.exists(SPECIAL_FOLDERS[location]):
                save_folder = SPECIAL_FOLDERS[location]

        # create folder if it doesn't exist
        os.makedirs(save_folder, exist_ok=True)

        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{now}.png"
        save_path = os.path.join(save_folder, filename)

        screenshot = pyautogui.screenshot()
        screenshot.save(save_path)

        speak("Screenshot taken")
        print("Saved screenshot to:", save_path)
        return True

    except Exception as e:
        speak("Could not take screenshot")
        print("Screenshot error:", e)
        return False

# ---------------------------
# CLOSE APP
# ---------------------------
def close_app(app_name):
    app_name = app_name.lower().strip()

    taskkill_map = {
        "chrome": "chrome.exe",
        "notepad": "notepad.exe",
        "calculator": "CalculatorApp.exe",
        "calc": "CalculatorApp.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
        "vscode": "Code.exe",
        "telegram": "Telegram.exe",
        "spotify": "Spotify.exe",
    }

    process_name = taskkill_map.get(app_name, f"{app_name}.exe")

    try:
        subprocess.run(
            ["taskkill", "/f", "/im", process_name],
            capture_output=True,
            text=True
        )
        speak(f"Closing {app_name}")
    except Exception as e:
        speak(f"Could not close {app_name}")
        print("Close app error:", e)
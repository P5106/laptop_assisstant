import os
from datetime import datetime
from voice import speak
from config import SCREENSHOTS_FOLDER, SPECIAL_FOLDERS


def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    message = f"The time is {current_time}"
    speak(message)


def tell_date():
    current_date = datetime.now().strftime("%d %B %Y")
    message = f"Today's date is {current_date}"
    speak(message)


def take_screenshot(location=None):
    try:
        import pyautogui

        save_folder = SCREENSHOTS_FOLDER

        if location:
            location = location.lower().strip()
            if location in SPECIAL_FOLDERS and os.path.exists(SPECIAL_FOLDERS[location]):
                save_folder = SPECIAL_FOLDERS[location]

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
import os
import subprocess
from voice import speak


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


def volume_up():
    try:
        import pyautogui
        for _ in range(5):
            pyautogui.press("volumeup")
        speak("Volume increased")
    except Exception as e:
        speak("Could not increase volume")
        print("Volume up error:", e)


def volume_down():
    try:
        import pyautogui
        for _ in range(5):
            pyautogui.press("volumedown")
        speak("Volume decreased")
    except Exception as e:
        speak("Could not decrease volume")
        print("Volume down error:", e)


def mute_volume():
    try:
        import pyautogui
        pyautogui.press("volumemute")
        speak("Volume muted")
    except Exception as e:
        speak("Could not mute volume")
        print("Mute error:", e)


def lock_laptop():
    try:
        subprocess.run("rundll32.exe user32.dll,LockWorkStation", shell=True)
        speak("Locking laptop")
    except Exception as e:
        speak("Could not lock laptop")
        print("Lock error:", e)


def shutdown_laptop():
    try:
        speak("Shutting down laptop")
        subprocess.run("shutdown /s /t 1", shell=True)
    except Exception as e:
        speak("Could not shutdown laptop")
        print("Shutdown error:", e)


def restart_laptop():
    try:
        speak("Restarting laptop")
        subprocess.run("shutdown /r /t 1", shell=True)
    except Exception as e:
        speak("Could not restart laptop")
        print("Restart error:", e)


def sleep_laptop():
    try:
        speak("Putting laptop to sleep")
        subprocess.run(
            "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
            shell=True
        )
    except Exception as e:
        speak("Could not put laptop to sleep")
        print("Sleep error:", e)


def open_task_manager():
    try:
        subprocess.Popen("taskmgr")
        speak("Opening Task Manager")
    except Exception as e:
        speak("Could not open Task Manager")
        print("Task manager error:", e)


def open_settings():
    try:
        os.system("start ms-settings:")
        speak("Opening Settings")
    except Exception as e:
        speak("Could not open Settings")
        print("Settings error:", e)
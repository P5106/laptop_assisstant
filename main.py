from parser import parse_command
from voice import speak, take_voice_command

from commands.open_commands import (
    open_website,
    open_app,
    open_file,
    smart_open,
    search_google,
    search_youtube,
)
from commands.media_commands import play_on_youtube, play_on_spotify
from commands.utility_commands import tell_time, tell_date, take_screenshot
from commands.system_commands import (
    close_app,
    volume_up,
    volume_down,
    mute_volume,
    lock_laptop,
    shutdown_laptop,
    restart_laptop,
    sleep_laptop,
    open_task_manager,
    open_settings,
)
from commands.ai_commands import ask_ai


def process_command(command):
    action, value = parse_command(command)

    if action == "open_website":
        open_website(value)

    elif action == "open_app":
        open_app(value)

    elif action == "open_file":
        open_file(value)

    elif action == "smart_open":
        smart_open(value)

    elif action == "google_search":
        search_google(value)

    elif action == "youtube_search":
        search_youtube(value)

    elif action == "spotify_search":
        play_on_spotify(value)

    elif action == "play_youtube":
        play_on_youtube(value)

    elif action == "play_spotify":
        play_on_spotify(value)

    elif action == "tell_time":
        tell_time()

    elif action == "tell_date":
        tell_date()

    elif action == "screenshot":
        take_screenshot(value)

    elif action == "close_app":
        close_app(value)

    elif action == "volume_up":
        volume_up()

    elif action == "volume_down":
        volume_down()

    elif action == "mute_volume":
        mute_volume()

    elif action == "lock_laptop":
        lock_laptop()

    elif action == "shutdown_laptop":
        shutdown_laptop()

    elif action == "restart_laptop":
        restart_laptop()

    elif action == "sleep_laptop":
        sleep_laptop()

    elif action == "open_task_manager":
        open_task_manager()

    elif action == "open_settings":
        open_settings()

    elif action == "ask_ai":
        ask_ai(value)

    elif action == "exit":
        speak("Goodbye")
        return False

    else:
        speak("Invalid command. Try open, search, play, AI, time, date, screenshot, or system control.")

    return True


def main():
    speak("Laptop assistant started")

    while True:
        print("\nChoose input mode:")
        print("1. Text command")
        print("2. Voice command")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            command = input("Type your command: ").strip()
            if command:
                if not process_command(command):
                    break

        elif choice == "2":
            command = take_voice_command()
            if command:
                if not process_command(command):
                    break

        elif choice == "3":
            speak("Exiting assistant")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
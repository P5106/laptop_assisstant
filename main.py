from commands import (
    open_website,
    open_app,
    open_file,
    smart_open,
    search_google,
    search_youtube,
    tell_time,
    tell_date,
    take_screenshot,
    close_app,
)
from parser import parse_command
from voice import speak, take_voice_command


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

    elif action == "tell_time":
        print("DEBUG: tell_time block reached")
        tell_time()

    elif action == "tell_date":
        tell_date()

    elif action == "screenshot":
        take_screenshot(value)

    elif action == "close_app":
        close_app(value)

    elif action == "exit":
        speak("Goodbye")
        return False

    else:
        speak("Invalid command. Try open, search, close, time, date, or screenshot.")

    return True


def main():
    speak("Laptop assistant version 5.1 started")

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
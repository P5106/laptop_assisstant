def parse_command(command):
    command = command.lower().strip()

    # -------------------------
    # EXIT
    # -------------------------
    if command in ["exit", "quit", "stop"]:
        return ("exit", "")

    # -------------------------
    # TIME
    # -------------------------
    if command in [
        "what is the time",
        "tell me the time",
        "tell time",
        "time",
        "current time",
        "what's the time"
    ]:
        return ("tell_time", "")

    # -------------------------
    # DATE
    # -------------------------
    if command in [
        "what is the date",
        "tell me the date",
        "tell date",
        "date",
        "today's date",
        "today date",
        "what's the date",
        "current date"
    ]:
        return ("tell_date", "")

    # -------------------------
    # SCREENSHOT
    # -------------------------
    if command == "take screenshot":
        return ("screenshot", "")

    if command == "capture screen":
        return ("screenshot", "")

    if command.startswith("take screenshot in "):
        location = command[len("take screenshot in "):].strip()
        return ("screenshot", location)

    # -------------------------
    # CLOSE APP
    # -------------------------
    if command.startswith("close app "):
        return ("close_app", command[len("close app "):].strip())

    if command.startswith("close "):
        return ("close_app", command[len("close "):].strip())

    # -------------------------
    # GOOGLE SEARCH
    # -------------------------
    if command.startswith("search google for "):
        return ("google_search", command[len("search google for "):].strip())

    if command.startswith("search ") and command.endswith(" in google"):
        query = command[len("search "):-len(" in google")].strip()
        return ("google_search", query)

    if command.startswith("search ") and command.endswith(" on google"):
        query = command[len("search "):-len(" on google")].strip()
        return ("google_search", query)

    if command.startswith("open google for "):
        return ("google_search", command[len("open google for "):].strip())

    # -------------------------
    # YOUTUBE SEARCH / PLAY
    # -------------------------
    if command.startswith("search youtube for "):
        return ("youtube_search", command[len("search youtube for "):].strip())

    if command.startswith("search ") and command.endswith(" in youtube"):
        query = command[len("search "):-len(" in youtube")].strip()
        return ("youtube_search", query)

    if command.startswith("search ") and command.endswith(" on youtube"):
        query = command[len("search "):-len(" on youtube")].strip()
        return ("youtube_search", query)

    if command.startswith("open youtube for "):
        return ("youtube_search", command[len("open youtube for "):].strip())

    if command.startswith("open ") and command.endswith(" in youtube"):
        query = command[len("open "):-len(" in youtube")].strip()
        return ("youtube_search", query)

    if command.startswith("play ") and command.endswith(" on youtube"):
        query = command[len("play "):-len(" on youtube")].strip()
        return ("youtube_search", query)

    # -------------------------
    # SPOTIFY PLAY
    # -------------------------
    if command.startswith("play ") and command.endswith(" on spotify"):
        query = command[len("play "):-len(" on spotify")].strip()
        return ("spotify_search", query)

    if command.startswith("open ") and command.endswith(" in spotify"):
        query = command[len("open "):-len(" in spotify")].strip()
        return ("spotify_search", query)

    # -------------------------
    # EXPLICIT OPEN COMMANDS
    # -------------------------
    if command.startswith("open website "):
        return ("open_website", command[len("open website "):].strip())

    if command.startswith("open app "):
        return ("open_app", command[len("open app "):].strip())

    if command.startswith("open file "):
        return ("open_file", command[len("open file "):].strip())

    # -------------------------
    # SMART OPEN
    # -------------------------
    if command.startswith("open "):
        return ("smart_open", command[len("open "):].strip())

    return ("unknown", command)
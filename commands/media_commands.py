import webbrowser
from urllib.parse import quote
from voice import speak


def play_on_youtube(song_name):
    song_name = song_name.strip()
    if not song_name:
        speak("What should I play on YouTube?")
        return

    url = f"https://www.youtube.com/results?search_query={quote(song_name)}"
    webbrowser.open(url)
    speak(f"Playing {song_name} on YouTube")


def play_on_spotify(song_name):
    song_name = song_name.strip()
    if not song_name:
        speak("What should I play on Spotify?")
        return

    url = f"https://open.spotify.com/search/{quote(song_name)}"
    webbrowser.open(url)
    speak(f"Playing {song_name} on Spotify")
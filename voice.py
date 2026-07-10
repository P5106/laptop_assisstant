import pyttsx3
import speech_recognition as sr


def speak(text):
    print("Assistant:", text)

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("Speech error:", e)


def take_voice_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""
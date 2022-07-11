import os
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import smtplib
import pyaudio

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(Audio):
    engine.say(Audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Hi! I am your personal voice assistant")
    if 0 <= hour < 12:
        speak("Have a good morning and a fantastic day!")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening, nice to meet you again")

    speak("How i can help you")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")
    except Exception:
        print("Sorry Sir, Please try again")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to the wikipedia", )
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open('youtube.com')
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com") 
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif 'play music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "soundcloud" in query:
            webbrowser.open("soundcloud.com")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif "open Team Viewer" in query:
            code_path = "C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe"
            os.startfile(code_path)
        elif "exit" or "Shut up" or "keep quite" or "stop":
            exit()
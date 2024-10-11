import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import psutil
import pygetwindow as gw
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 155)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir")
        print("ISWIA: Good morning sir")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon sir")
        print("ISWIA: Good afternoon sir")
    else:
        speak("Good Evening sir")
        print("ISWIA: Good Evening sir")
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")
    print(f"The time is: {strTime}")
    speak("I am your Virtual Assistant named iswia.")
    print("ISWIA: I am your Virtual Assistant named Iswia.")

def open_application(application_name):
    try:
        if "discord" in application_name.lower():
            subprocess.Popen(["start", "msedge", "https://discord.com/channels/@me"])
            speak("Opening Discord")
            print("ISWIA: Opening Discord")
        elif "youtube" in application_name.lower():
            subprocess.Popen(["start", "chrome", "https://www.youtube.com/"])
            speak("Opening YouTube")
            print("ISWIA: Opening YouTube")
        else:
            subprocess.Popen(["start", application_name])
            speak(f"Opening {application_name}")
            print(f"ISWIA: Opening {application_name}")
    except Exception as e:
        speak(f"Sorry, I couldn't open {application_name}. Error: {e}")
        print(f"ISWIA: Sorry, I couldn't open {application_name}. Error: {e}")

def minimize_application(application_name):
    try:
        if application_name.lower() == "all":
            os.system(f"powershell -command \"(New-Object -ComObject Shell.Application).MinimizeAll()\"")
            speak("All windows minimized")
            print("ISWIA: All windows minimized")
        else:
            app = gw.getWindowsWithTitle(application_name)[0]
            app.minimize()
            speak(f"{application_name} minimized")
            print(f"ISWIA: {application_name} minimized")
    except IndexError:
        speak(f"Sorry, I couldn't find {application_name}.")
        print(f"ISWIA: Sorry, I couldn't find {application_name}.")

def maximize_application(application_name):
    try:
        if application_name.lower() == "all":
            for window in gw.getAllWindows():
                window.maximize()
            speak("All windows maximized")
            print("ISWIA: All windows maximized")
        else:
            app = gw.getWindowsWithTitle(application_name)[0]
            app.maximize()
            speak(f"{application_name} maximized")
            print(f"ISWIA: {application_name} maximized")
    except IndexError:
        speak(f"Sorry, I couldn't find {application_name}.")
        print(f"ISWIA: Sorry, I couldn't find {application_name}.")

def close_application(application_name):
    try:
        if application_name.lower() == "all":
            os.system(f"powershell -command \"(New-Object -ComObject Shell.Application).CloseAllWindows()\"")
            speak("All windows closed")
            print("ISWIA: All windows closed")
        else:
            app = gw.getWindowsWithTitle(application_name)[0]
            app.close()
            speak(f"{application_name} closed")
            print(f"ISWIA: {application_name} closed")
    except IndexError:
        speak(f"Sorry, I couldn't find {application_name}.")
        print(f"ISWIA: Sorry, I couldn't find {application_name}.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        commands = query.split(" and ")

        if 'wikipedia for' in query:
            speak("searching in wikipedia")
            print("ISWIA: searching in wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print("ISWIA: According to wikipedia")
            print(results)
            speak(results)

        elif "your name" in query:
            speak("my name is Iswia.")
            print("ISWIA: My name is Iswia.")

        elif "google for" in query:
            search_term = query.split("for")[-1]
            url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on google')
            print(f"ISWIA: Here is what I found for {search_term}")

        elif "github for" in query:
            search_term = query.split("for")[-1]
            url = f"https://github.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f"Here is what I found for {search_term} on Github")
            print(f"ISWIA: Here is what I found for {search_term} on Github")

        elif "youtube for" in query:
            search_term = query.split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on youtube')
            print(f"ISWIA: Here is what I found for {search_term}")

        elif 'open gmail' in query:
            url = f"https://www.gmail.com/"
            webbrowser.get().open(url)
            speak("Opening gmail")
            print("ISWIA: Opening gmail")

        elif 'my web' in query:
            url = f"https://technicalfacty.data.blog/"
            webbrowser.get().open(url)
            speak("Opening your website sir.")
            print("ISWIA: Opening your website sir.")

        elif 'open code' in query:
            path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio Code")
            print("ISWIA: Opening Visual Studio Code")
            os.startfile(path)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(f"ISWIA: The time is: {strTime}")

        elif 'open' in query:
            application_name = query.split('open')[-1].strip()
            open_application(application_name)

        elif 'minimise' in query:
            app_name = query.split("minimise", 1)[-1].strip()
            minimize_application(app_name)

        elif 'maximize' in query:
            app_name = query.split("maximize", 1)[-1].strip()
            maximize_application(app_name)

        elif 'close' in query:
            app_name = query.split("close", 1)[-1].strip()
            close_application(app_name)

        elif 'text to speech' in query:
            tts = query.split('text to speech')[-1]
            speak(f"{tts}")
            print(f"{tts}")

        elif 'offline' in query or 'exit' in query or 'bye' in query:
            speak("Turning off all my systems")
            print("ISWIA: Turning off all my systems")
            exit()

        else:
            speak("I am unable to assist you with this, can I help you with anything else?")
            print("ISWIA: I am unable to assist you with this, can I help you with anything else?")
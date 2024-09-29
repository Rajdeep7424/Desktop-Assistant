import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir")
    elif hour>=12 and hour<4:
        speak("Good afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am your Virtual Assistant JARVIS.")
    
def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry Sir, can you repeat that again?")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        speak("Please tell me how can i help you?")
        query = takeCommand().lower()
        if 'wikipedia' in query:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube Sir")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google Sir")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("Opening Gmail Sir")
        #elif 'open code' in query:
         #   open('path')
          #  path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
           # speak("Opening Visual Studio Code Sir")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'go offline' in query:
            speak("turning off my systems sir, see you soon!")
            exit()

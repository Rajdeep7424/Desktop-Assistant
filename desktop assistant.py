import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import psutil

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
        print("Computer: Good morning sir")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon sir")
        print("Computer: Good afternoon sir")
    else:
        speak("Good Evening sir")
        print("Computer: Good Evening sir")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        print(f"The time is: {strTime}")
    speak("I am your Virtual Assistant named iswia.")
    print("Computer: I am your Virtual Assistant named Iswia.")

def takeCommand():
    query = input("User: ")

    if 'wikipedia for' in query:
        speak("searching in wikipedia")
        print("Computer: searching in wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print("Computer: According to wikipedia")
        print(results)
        speak(results)
        return query

    elif "your name" in query:
        speak("my name is Iswia.")
        print("Computer: My name is Iswia.")
        return query

    elif "google for" in query:
        search_term = query.split("for")[-1]
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')
        print(f"Computer: Here is what I found for {search_term}")
        return query

    elif "github for" in query:
            search_term = query.split("for")[-1]
            url = f"https://github.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f"Here is what I found for {search_term} on Github")
            print(f"Computer: Here is what I found for {search_term} on Github")
            return query

    elif "`" in query:
        search_term = query.split("`")[-1]
        speak(f'{search_term}')
        print(f'Computer: {search_term}')
        return query

    elif "youtube for" in query:
        search_term = query.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')
        print(f"Computer: Here is what I found for {search_term}")
        return query

    elif 'open gmail' in query:
        url = f"https://www.gmail.com/"
        webbrowser.get().open(url)
        speak("Opening gmail")
        print("Computer: Opening gmail")
        return query

    elif 'my web' in query:
        url = f"https://technicalfacty.data.blog/"
        webbrowser.get().open(url)
        speak("Opening your website sir.")
        print("Computer: Opening your website sir.")
        return query

    elif 'open code' in query:
        open('path')
        path = "C:\Program Files\Microsoft VS Code\Code.exe"
        speak("Opening Visual Studio Code")
        print("Computer: Opening Visual Studio Code")
        os.startfile(path)
        return query

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
        print(f"Computer: The time is: {strTime}")
        return query

    elif "-" in query:
            search_term = query.split("-")[-1]
            url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on google')
            print(f"Computer: Here is what I found for {search_term}")
            return query

    elif 'minimize'in query:
        app = query.split("minimize")[-1]
        os.system(f"powershell -command \"(New-Object -ComObject Shell.Application).MinimizeAll()\"")
        speak(f"{app} minimized")
        print(f"Computer: {app} minimized")
        return query

    elif 'offline'in query:
        speak("Turning off all my systems")
        print("Computer: Turning off all my systems")
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
         speak("Bye! sir")
         print("Computer: Bye! sir")
        elif hour >= 12 and hour < 21:
         speak("See you soon sir")
         print("Computer: See you soon! sir")
        else:
         speak("Good night sir")
         print("Computer: Good night sir")
         (exit)

    else:
        speak("I am unable to assist you with this, can i help you with anything else?")
        print("Computer:  I am unable to assist you with this, can i help you with anything else?")
        return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

# python -u "f:\I.S.W.I.A\I.S.W.I.A.py"

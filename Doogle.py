import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am doogle. How may I help you")


def takeCommand():
    #It takes microphone inputs and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir="E:\\Music\\hindi\\kishore kumar"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        elif "google" and "search" in query:
            query = query.replace("google search", "")
            webbrowser.open("https://google.com/search?q=%s" % query)

        elif "quit" in query:
            speak("Thank you !")
            exit()




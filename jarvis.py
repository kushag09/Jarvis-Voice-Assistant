import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os.path
import random as r
import smtplib
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    '''with the help of this fuction our computer speak.'''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''this function simple wish me to and speak.'''
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12 : 
        speak("Good Morning sir")

    elif hour >=12 and hour < 18:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")
    
    speak("Hi i am Jarvis. Your assistant How may i help you sir?? ")

def takeCommand():
    ''' it takes our voices and convert into speech with the help of microphone.'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    
    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

with open("pswrd.txt", "r") as f:
    f.close()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abhaysananse@gmail.com', 'f')
    server.sendmail("abhaysananse@gmail.com", to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # execute the task which we want.
        if 'wikipedia' in query:
            speak("Searching Wkipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open vscode' in query:
            code_path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            
        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')
        
        elif 'thank you' in query or 'thanks' in query:
            speak('My pleasure sir')
        
        elif 'music' in query:
            music = "E:\\music"
            songs = os.listdir(music)
            songs = list(songs)
            # while 1:
                # choice = int(input("Press 1 for playing song: "))
            if 1:
                song = r.choice(songs)
                os.startfile(os.path.join(music, song))
            else: 
                speak("i am not able to play a music.")
        elif 'timer' in query or 'stopwatch' in query:

            speak("For how many minutes?")
            wait_time = takeCommand()
            wait_time = wait_time.replace('minutes', '')
            wait_time = wait_time.replace('minute', '')
            wait_time = wait_time.replace('for', '')
            wait_time = float(wait_time)
            wait_time = wait_time * 60
            speak(f'I will remind you in {wait_time} seconds')

            time.sleep(wait_time)
            speak('Your time has been finished sir')
            
        elif 'email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "abhaysananse@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this mail.")

        elif 'quit' in query:
            speak("Thanks for using me sir. Have a great day.")
            quit()
        

       

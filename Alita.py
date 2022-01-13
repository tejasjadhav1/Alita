import pyttsx3
import datetime
import wikipedia 
import webbrowser
import speech_recognition as sr
import os
import pyaudio
import smtplib

print("hello");

MASTER = "Tejas"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Pronouncing String
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This function will speak
def whishMe():

    
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER + ". I am Alita, How may I help you?")

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER +". I am Alita, How may I help you?")

    else:
        speak("Good Evening" + MASTER + ". I am Alita, How may I help you?")

#This function will take commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenging...")
        audio = r.listen(source)
    
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query

#Main Program starts here...   
whishMe()
query = takeCommand()

#executing task
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    webbrowser.open('https://www.youtube.com/')
    

elif 'on youtube' in query.lower():
    speak("playing youtube songs for you sir")
    webbrowser.open('https://www.youtube.com/watch?v=Gr82rgJKkPU&list=PLUt6EE2RAQR53GK216PgMeL7VFurCXfRm&ab_channel=LostStoriesMusic')
    

elif 'open reddit' in query.lower():
    webbrowser.open('https://www.reddit.com/') 
    

elif 'play music' in query.lower():
    songs_dir = "C:/Users/Lenovo/Downloads/Songs"
    songs = os.listdir(songs_dir)
    print(songs)
    speak("Playing music")
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'spotify' in query.lower():
    webbrowser.open('https://open.spotify.com/playlist/6ZlGMMdhQfhG58QP5Ps4Ul?si=e18d0545d5a549c8')

  


    


    

    



    
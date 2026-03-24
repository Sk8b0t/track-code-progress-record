import smtplib #for sending emails
import os
import webbrowser
import wikipedia
import datetime as d
import speech_recognition as sr
from win32com.client import Dispatch


def speak(chiz):
    spk = Dispatch("SAPI.SpVoice")
    voices = spk.GetVoices()
    spk.Voice = voices.Item(1) 
    spk.Speak(chiz)
    
def wishMe():
    hr=d.datetime.now().hour
    if hr>=0 and hr<12:
        speak("Good Morning Sir")
        print("Good Morning Sir")
    elif hr>=12 and hr<17:
        speak("Good Afternoon Sir")
        print("Good Afternoon Sir")
    elif hr>=17 and hr<=20:
        speak("Good Evening Sir")
        print("Good evening Sir")
    else:
        speak("Good night sir")
        print("Good night Sir")
    print(d.datetime.now())

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #  for audio listning
         print("Listning...")
         r.pause_threshold=1
         r.energy_threshold=330
         audio=r.listen(source)
         
        #  for recognizing the audio and converting it into a string
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        print("Failed to recognize voice")
        print("PLease say it again")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            try: 
                query=query.replace("wikipedia","").strip()
                res=wikipedia.summary(query,sentences=2)
                print(res)
                speak("According to Wikipedia , "+res)
            except Exception as e:
                print("Failed to fetch from wikipedia...")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open code forces' in query:
            webbrowser.open("https://codeforces.com/")
            speak("opening codeforces")

        elif 'attack on titan video' in query:
            musicDir="C:\\Users\\sayan\\Desktop\\बाकी"
            song=os.listdir(musicDir)
            speak("Opening Attack On Titan Video")
            print(f"playing {song[43]}")
            os.startfile(os.path.join(musicDir,song[43]))
             
        elif 'time' in query:
            speak(d.datetime.now().strftime("%H%M%S"))
            print(d.datetime.now().strftime("%H%M%S"))

        elif 'open code' in query:
            speak("Opening VS Code...")
            pth="C:\\Users\\sayan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(pth)
        elif query=="none":
            break

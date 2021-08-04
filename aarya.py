#python -m pip install pyttsx3
#pyttsx3 is a text-to-speech conversion library in Python
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')#sapi=microsoft speech api
voices=engine.getProperty("voices")
#error no module named pywintypes so copy files from C:\Users\Enchancia\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\pywin32_system32 to C:\Users\Enchancia\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\win32\lib
#print(voices)
engine.setProperty('voice',voices[1].id)#zero=david 1=zira

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good afternoon!")
    else:
        print("Good Evening!")
        speak("Good evening!")
    print("I am Aarya. How may i help you?")
    speak("I am Aarya. How may i help you?")

def takeCommand():
    r=sr.Recognizer()#recognizer is a class,if () are not added error is raised
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=0.8#non-speaking time before a phrase is termed as complete
        #energy_threshold we can say loudly if other disturbances are present
        #python -m pip install pywin also python -m pywin install pyaudio
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("User said:",query)
    except Exception as e:
        #print(e)#this prints the error
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)#587 is port no.
    server.ehlo()
    server.starttls()
    server.login("your-mail-address","your-password")
    server.sendmail('your-email-address',to,content)
    server.close()
       
    
if __name__=="__main__":
    wishMe()
    while(True):
        query=takeCommand().lower() #logic for executing tasks based on query
        if "wikipedia" in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia..")
            query=query.replace("wikipedia","")#replace the word wikipedia by a comma in query 
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir="G:\\Counter Strike\\Counter-Strike 1.6\\valve\\media"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Time is {strTime}")
        elif "open ms word" in query:
            path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010.lnk"
            os.startfile(path)
        elif 'send email' in query:
            #here you have to allow less secure apps to gmail
            try:
                speak("What should i say?")
                content=takeCommand()
                to=""
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry unable to send email.")
        elif "quit" in query:
            exit()
                
                
            

    

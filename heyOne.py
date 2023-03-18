import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#convert test to voice
def talk(text):
    engine.say(text)
    engine.runAndWait()

#assistant will great the user according to time
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        talk("Good Morning!")
    
    elif hour >=12 and hour <18:
        talk("good afternoon!")
    
    else:
        talk("good evening!")
    
    talk('I am one. How can i help you?')

#take voice command from user and return string output
def takeCommand():
    ...
    listner = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            listner.pause_threshold = 1
            listner.energy_threshold = 400
            voice=listner.listen(source)
            command=listner.recognize_google(voice, language='en-in')
            command=command.lower()
            if 'one' in command:
                command = command.replace('one','')
                
    except:
        pass
    return command
    ...


#logic for executing task based on user requests
def runOne():

    while True:
        command = takeCommand()
        if 'play' in command:
            song=command.replace('play','')
            talk('playing' + song)
            print(song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is'+time)

        elif 'tell me about' in command:
            talk("searching")
            about = command.replace('tell me about','')
            info = wikipedia.summary(about,1)
            talk("according to wikipedia")
            print(info)
            talk(info)

        elif 'open google' in command:
            talk("opening google")
            webbrowser.open('google.com')

        elif 'open youtube' in command:
            talk("opening youtube")
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in command:
            talk("opening stackoverflow")
            webbrowser.open('stackoverflow.com')
        
        elif 'open code' in command:
            talk("opening vs code")
            path = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        
        elif 'quit' in command:
            talk('quiting')
            break



   

if __name__ == "__main__":
    wishme()
    runOne()

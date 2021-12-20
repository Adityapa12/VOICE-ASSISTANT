import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning ')
    elif hour >=12 and hour<18:
        speak('good afternon ')
    else:
        speak('good evening ')
    speak('i am luffy sir . please tell me what is that you desire')
def takeCommand():


    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recogninzing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said :{query}\n')
    except Exception as e:
        # print(e)

        print('say that again please....')
        return 'None'
    return query
    
if __name__ == "__main__":
    wishMe()
    while True: 
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)
     



 

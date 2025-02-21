import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

id1= 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id2= 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'


# listen to microphone and returns audio text
def audio_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as origin:
        r.pause_threshold = 0.8
        print('Start talking')
        audio = r.listen(origin)

        try:
            #search on google
            request = r.recognize_google(audio, language='en-US')
            print(f"You Said: {request}")

            return request

        except sr.UnknownValueError:
            print("Error!")

            return "Waiting...."


def text_to_audio(text, id):
    engine = pyttsx3.init()
    engine.setProperty('voice', id)
    #for voice in engine.getProperty('voices'):
    #    print(voice)

    engine.say(text)
    engine.runAndWait()


#t = audio_to_text()
#text_to_audio(t)
text_to_audio("Hello", id1)
text_to_audio("Hello", id2)


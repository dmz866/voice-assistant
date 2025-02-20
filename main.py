import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

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


def text_to_audio(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


t = audio_to_text()
text_to_audio(t)


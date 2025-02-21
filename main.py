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

def what_time_is_it():
    now = datetime.datetime.now()
    text_to_audio(f"Its {now.hour} o'clock ", id1)

def main_app():
   is_running = True

   while is_running:
       request = audio_to_text().lower()
       print(request)

       if 'open youtube' in request:
           text_to_audio('With pleasure! Opening youtube', id1)
           webbrowser.open('www.youtube.com')
       elif 'what time is it' in request:
           what_time_is_it()
       elif 'search on wikipedia' in request:
           text_to_audio('Searching on wikipedia...', id1)
           request = request.replace('wikipedia', '')
           wikipedia.set_lang('en')
           result = wikipedia.summary(request, sentences=1)
           text_to_audio('Wikipedia says:', id1)
           text_to_audio(result, id1)
       elif 'search on the web' in request:
           text_to_audio('Searching on the web...', id1)
           request = request.replace('search on the web', '')
           pywhatkit.search(request)
       elif 'play on youtube' in request:
           text_to_audio('Playing on youtube...', id1)
           request = request.replace('play on youtube', '')
           pywhatkit.playonyt(request)
       elif 'tell me a joke' in request:
           request = request.replace('tell me a joke', '')
           text_to_audio(pyjokes.get_joke('en'), id1)
       elif 'exit' == request:
            text_to_audio('Closing app. Bye', id1)
            is_running = False


#t = audio_to_text()
#text_to_audio(t)
#text_to_audio("Hello", id1)
#text_to_audio("Hello", id2)

main_app()


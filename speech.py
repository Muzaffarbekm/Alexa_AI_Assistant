import speech_recognition as sr   # Also need to pyaudio.(microphone)
from time import ctime  # core-package
import time  # core-package
import webbrowser
from gtts import gTTS  # Google text to speech API
import playsound  # We install PyObjC
import os   # built-in remove method
import random  # to generate names for audio-files.

r = sr.Recognizer()

def audio_ai(ask =False):
    with sr.Microphone() as source:
        if ask:
            Alex_speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Alex_speak("sorry I didn't understand")
        except sr.RequestError:
            Alex_speak("Server isn't working")
        return voice_data

def Alex_speak(audio_str):
    tts = gTTS(text=audio_str, lang="en")
    random_number = random.randint(1,1000)
    audio_file = "audio-" + str(random_number) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_str)  # when she speaks it also prints what is being
    os.remove(audio_file)

def respond(voice_data):
    keys = ["how are you","how are you doing"]
    if voice_data in keys:
        Alex_speak("Fine thanks :)")

    if "what is your name" in voice_data:
        Alex_speak("my name is Alex")

    if "hi" in voice_data:
        Alex_speak("awesome!")

    if "what time is it" in voice_data:
        Alex_speak(ctime())

    if "search" in voice_data:
        #ask = input("what you wanna search for? \n")
        search = audio_ai("What you wanna search for?")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        Alex_speak("Here is what I found for" + search)

    if "find location" in voice_data:
        #ask = input("what you wanna search for? \n")
        location = audio_ai("What place you wanna search for?")
        url = "https://www.google.com/maps/place/" + location + "/&amp;"  # amp means (Accelerated Mobile Pages) that html works faster
        webbrowser.get().open(url)
        Alex_speak("Here is " + location)

    if "exit" in voice_data:
        Alex_speak("thanks for using Alex speech assistant!")
        exit()

time.sleep(1)
Alex_speak("how can I help you?")
while 1:
    voice_data = audio_ai()
    respond(voice_data)
#print(respond(voice_data))



# You can ask these things.

#["how are you","how are you doing"]
#"what is your name"
#"hi"
#"what time is it"
#"search"
#"find location"
#"exit"

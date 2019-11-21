#!/usr/bin/env python3
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import webbrowser
from pygame import mixer
from tempfile import TemporaryFile


name = "Django"; #enter your name here


def speak(audioString):
 print(audioString)
 mixer.init()
 tts = gTTS(text=audioString, lang='en')
 sf = TemporaryFile()
 tts.write_to_fp(sf)
 sf.seek(0)
 mixer.music.load(sf)
 mixer.music.play()


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("Say something!")
     audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        #use default google api key
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def iris(data):
  
 if "how are you" in data:
  speak("I am fine")

 if "what time is it" in data:
  speak(ctime())

#if you ask where something is, extract area and look it up in google chrome
 if "where is" in data:
  data = data.split(" ")
  location = data[2]
  speak("Hold on" + name + "I will show you where " + location + " is.")
  url ="https://www.google.nl/maps/place/" + location
  chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
  webbrowser.get(chrome_path).open(url)

 if "add" in data:
  data = data.split(" ")
  number = float(data[1])
  number2=float(data[3])
  answer = number + number2
  if(float(answer).is_integer()):
   speak("the answer is " + str(int(answer)))
  else:
    speak("the answer is " + str(round(answer,2)))

 if "multiply" in data:
  data = data.split(" ")
  number = float(data[1])
  number2=float(data[3])
  answer = number * number2
  if(float(answer).is_integer()):
   speak("the answer is " + str(int(answer)))
  else:
    speak("the answer is " + str(round(answer,2)))

 if "divide" in data:
  data = data.split(" ")
  number = float(data[1])
  number2=float(data[3])
  answer = number / number2
  if(float(answer).is_integer()):
   speak("the answer is " + str(int(answer)))
  else:
    speak("the answer is " + str(round(answer,2)))

 if "subtract" in data:
  data = data.split(" ")
  number = float(data[1])
  number2=float(data[3])
  answer = number2 - number
  if(float(answer).is_integer()):
   speak("the answer is " + str(int(answer)))
  else:
    speak("the answer is " + str(round(answer,2)))

# initialization
speak("Hi " + name + " what can I do for you?")
while 1:
    data = recordAudio()
    iris(data)
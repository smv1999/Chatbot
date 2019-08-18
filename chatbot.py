from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3
import speech_recognition as sr 
import os

bos=ChatBot('bot')
r = sr.Recognizer()
engine = pyttsx3.init()
bos.set_trainer(ListTrainer)
data=open('you dir','r').readlines()
bos.train(data)
while(True):
    with sr.Microphone() as source:
         print ('Say Something!')
         audio = r.listen(source)
         print ('Done!')  
    text = r.recognize_google(audio)
    print (text)
    if(text!='bye'):
        print(bos.get_response(text))
        engine.say(bos.get_response(text))
        engine.runAndWait() 
    else:
        print("bye")
        engine.say("bye")
        engine.runAndWait()
        break

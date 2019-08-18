from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import speech_recognition as sr 
import os


bos=ChatBot('bot')
r = sr.Recognizer()
bos.set_trainer(ListTrainer)
data=open('/Users/subramanianradhakrishnan/Desktop/Chatbot/dataset.yml','r').readlines()
bos.train(data)
while(True):
    with sr.Microphone() as source:
         print ('Say Something!')
         os.system('Say listeningS')
         audio = r.listen(source)
         print ('Done!')  
    text = r.recognize_google(audio)
    print (text)
    if(text!='bye'):
        print(bos.get_response(text))
        os.system('say '+str(bos.get_response(text)))
    else:
        print("bye")
        os.system('say bye')
        break
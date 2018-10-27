#!/usr/bin/python3

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
from shlex import quote
import re
import os

chatbot = ChatBot('Kina')
chatbot.set_trainer(ChatterBotCorpusTrainer)

r = sr.Recognizer()
mic = sr.Microphone()

voiceInput = ''

def speak(text):
    os.system('pico2wave -l de-DE -w buffer.wav "' + text + '" && aplay buffer.wav')

while True:

    confirmedInput = False
    while (confirmedInput == False):

        try:
            with mic as source:

                r.adjust_for_ambient_noise(source)
                print('Lausche')
                speak('Ich höre!')
                audio = r.listen(source)


            voiceInput = r.recognize_google(audio, language='de-DE')
            confirmedInput = True
        except sr.UnknownValueError:
            print('Error')
            speak('Das habe ich leider nicht verstanden.')

    if bool(re.match('^[ÖÄÜöäüßA-Za-z0-9.,?+=:* ]+$', string)) == True:

        print('Du: ' + voiceInput)

        answ = str(chatbot.get_response(voiceInput))

        print(str("Kina: ") + answ)

        if bool(re.match('^[ÖÄÜöäüßA-Za-z0-9.,?+=:* ]+$', answ)) == False:
            print('WARNUNG')
        else:
            speak(quote(answ))
    else:
        print('WARNUNG: ' + string)

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

string = ''

while True:

    ja = False
    while (ja == False):

        try:
            with mic as source:

                r.adjust_for_ambient_noise(source)
                print('Lausche')
                os.system('pico2wave -l de-DE -w buffer.wav "Ich höre!" && aplay buffer.wav')
                audio = r.listen(source)


            string = r.recognize_google(audio, language='de-DE')
            ja = True
        except sr.UnknownValueError:
            print('Error')
            os.system('pico2wave -l de-DE -w buffer.wav "Das habe ich leider nicht verstanden." && aplay buffer.wav')

    if bool(re.match('^[ÖÄÜöäüßA-Za-z0-9.,?+=:* ]+$', string)) == True:

        print('Du: ' + string)

        answ = str(chatbot.get_response(string))

        print(str("Kina: ") + answ)

        if bool(re.match('^[ÖÄÜöäüßA-Za-z0-9.,?+=:* ]+$', answ)) == False:
            print('WARNUNG')
        else:
            os.system('pico2wave -l de-DE -w buffer.wav "' +  quote(answ) + '" && aplay buffer.wav')
    else:
        print('WARNUNG: ' + string)


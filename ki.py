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
    os.system('pico2wave -l de-DE -w buffer.wav "' + text + '" && aplay buffer.wav -q')

while True:

    confirmedInput = False
    while (confirmedInput == False):

        try:
            with mic as source:

                r.adjust_for_ambient_noise(source)
                print(' #Lausche')
                audio = r.listen(source)

            voiceInput = r.recognize_google(audio, language='de-DE')
            confirmedInput = True
            print('Du: ' + voiceInput)

        except sr.UnknownValueError:
            print(' #Error')
            #speak('Das habe ich leider nicht verstanden.')

    if voiceInput == 'Computer':

        print(' #Unterhaltung begonnen')
        speak('Ich höre')
        print('Kina: Ich höre')

        isConversation = True

        while (isConversation == True):

            confirmedInput = False
            while (confirmedInput == False):

                try:
                    with mic as source:

                        r.adjust_for_ambient_noise(source)
                        print(' #Lausche')
                        #speak('Ich höre!')
                        audio = r.listen(source)
                        print(' #Verarbeite das Gehörte')


                    voiceInput = r.recognize_google(audio, language='de-DE')
                    confirmedInput = True
                except sr.UnknownValueError:
                    print(' #Error')
                    speak('Das habe ich leider nicht verstanden.')
                    print('Kina: Das habe ich leider nicht verstanden.')

            print('Du: ' + voiceInput)

            if voiceInput == 'Ruhe':
                isConversation = False
                speak('Ok. Ich warte auf das Stichwort.')
                print('Kina: Ok. Ich warte auf das Stichwort.')
                print(' #Unterhaltung beendet')

            else:
                answ = str(chatbot.get_response(voiceInput))

                print(str('Kina: ') + answ)
                speak(quote(answ))

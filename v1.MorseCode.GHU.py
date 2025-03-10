# python3 -i MorseCode.py

import numpy as np
import sounddevice as sd
import time

sample_rate = 44100
frequency = 800
unit = 0.25
dot_unit = np.linspace(0, unit, int(sample_rate * unit), endpoint=False)
dash_unit = np.linspace(0, unit * 3, int(sample_rate * unit * 3), endpoint=False)

dot_wave = np.sin(2 * np.pi * frequency * dot_unit)
dash_wave = np.sin(2 * np.pi * frequency * dash_unit)
space = """







"""

morse_dictionary = {
    "a" : ".-" ,
    "b" : "-..." ,
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    " " : " ",
    "." : ".-.-.-",
    "," : "--..--",
    "?" : "..--..",
    "!" : "-.-.--"
    }

def morse_code():
    # asks for message, verifies message is valid, returns dots_and_dashes()
    message = input("Type a brief message to convert to Morse Code! ")
    if len(message) == 0:
        print(space)
        print("ERROR: must type a message to translate!")
        return morse_code()
    if len(message) > 50:
        print(space)
        print("ERROR: messages may only be up to 50 characters long!")
        return morse_code()
    lower_case = message.lower()
    for character in lower_case:
        if character not in 'abcdefghijklmnopqrstuvwxyz0123456789 .,?!':
            print(space)
            print("ERROR: message may only consist of the alphabet, whole numbers, spaces, and .,?!")
            return morse_code()
    return dots_and_dashes(lower_case)

def dots_and_dashes(string):
    # translates string into morse code text, asks whether user wants text audio
    translated_text = ""
    audio_text = ""
    for character in string:
        if character == " ":
            translated_text += "   "
            audio_text += " "
        else:
            translated_text += morse_dictionary[character] + " "
            audio_text += morse_dictionary[character] + "/"
    print("Translated Text: " + translated_text)
    input("Press Enter to Send Transmission! ")
    sound_audio(audio_text)

def sound_audio(morse_text):
    # converts morse code to audio signals
    print("Transmitting...")
    for i in morse_text:
        if i == ".":
            sd.play(dot_wave, samplerate=44100, blocking=True)
            time.sleep(unit)
        elif i == "-":
            sd.play(dash_wave, samplerate=44100, blocking=True)
            time.sleep(unit)
        elif i == "/":
            time.sleep(2*unit) # would be 3*unit but there is already a 1 unit pause after .-
        elif i == " ":
            time.sleep(4*unit) # would be 7*unit but there is already a 1 unit pause after .-
            # AND 2 unit pause after each character
    print("Transmission Sent!")
    input("Press Enter to send another Morse Code transmission! ")
    print(space)
    morse_code()

morse_code()
        #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:16:18 2024

@author: bhanu
"""
import speech_recognition as sr
import pyttsx3
import sys
import random
import constant

randomYN = ['N']
r = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()
#print(engine.getProperty("rate"))
engine.setProperty("rate", 170)

def agentSay(command):
    # Randomly add Name or not
    if random.choice(randomYN) == "Y" and constant.currentUser != "":
        command = constant.currentUser + ", " + command
    
    engine.say(command) 
    engine.runAndWait()

def record_text():
    while (1):
        try:
            
            # use the microphone as source for input.
            with sr.Microphone() as source2:    
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                r.adjust_for_ambient_noise(source2, duration=0.0)
                #listens for the user's input 
                audio2 = r.listen(source2)
                command = r.recognize_google(audio2)
                print (command)
                return command.lower()
        except sr.RequestError as e:
            print("Could not request results; {0} ".format(e))
             
        except sr.UnknownValueError:
            print("unknown error occurred")



# Register your self
def register():
    agentSay("Whom I am speaking with?")
    yourname = record_text()
    
    if "my name is " in yourname or "i am ":
        yourname = yourname.replace("my name is ","").replace("i am ", "")
        agentSay(yourname+", Is that correct?, Say yes or no")
        
        if "yes" in record_text():
            me = yourname
            agentSay("Thanks "+me+", I will try to memorize it.")
        else:
            register()
    else:
        agentSay("""
                 I am unable to extract name, try something like "I am {constant.agentName}"
                 """)

def loadlib(module_name,command):
    __import__(module_name)
    mymodule = sys.modules[module_name]
    answer = mymodule.askMe(command)
    return answer

def process(command):
    answer = loadlib("plugin/chatgpt",command)
    agentSay(answer)
    #elif "ask wiki" in command:
    #    answer = loadlib("wiki",command.replace("ask wiki",""))
    #    sayAnswer(answer)
    #else:
    #    agentSay("Sorry!!! Could you try this different way!!")
            
while(1):
    if constant.currentUser == "":
        agentSay("Hi, I am "+constant.agentName)
        register()
    command = record_text()
    if "stop "+constant.agentName in command:
        break
    else:
        command = command
        process(command)


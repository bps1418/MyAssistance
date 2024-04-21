#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:22:21 2024

@author: bhanu
"""

import openai
import constant

openai.api_key = OPENAI_KEY
agentName = "Rachel"

def sendtochatGPT(messages, model="gpt-3.5-turbo"):
    
    response = openai.chat.completions.create (
        model=model,
        messages = messages,
        n=1,
        stop=None,
        temperature=0.5
        )
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

text = "I am your digital help! My name is "+agentName
messages=[{"role":"assistant","content":text}]
messages=[{"role":"user","content":"I am "+constant.currentUser}]

while(1):
    response = sendtochatGPT(messages)
    print(response)
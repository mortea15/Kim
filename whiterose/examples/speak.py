#!/usr/bin/env python2
# -*- coding: utf-8-*-
from whiterose import whiterose

spk = whiterose.Speak(device='plughw:0,0',
                resources='../resources/audio')

spk.beep()
spk.say("Hi, I'm whiterose. How are you today, Sir?")

#!/usr/bin/env python2
# -*- coding: utf-8-*-
from kim import kim

spk = kim.Speak(device='plughw:0,0',
                resources='../resources/audio')

spk.beep()
spk.say("Hi, I'm Kim. How are you today, Sir?")

#!/usr/bin/env python2
# -*- coding: utf-8-*-
from kim import kim

spk = kim.Speak(device='plughw:0,0',
                        resources='/home/pi/kim/kim/resources/audio')

spk.beep(1)
spk.beep(0)
spk.say("Hi, I'm Kim. How are you today, Sir?")

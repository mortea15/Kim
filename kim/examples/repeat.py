#!/usr/bin/env python2
# -*- coding: utf-8-*-
from kim import kim

lstn = kim.Listen(adcdev='plughw:1,0',
                lm='/home/pi/kim/kim/resources/dict/0014.lm',
                dict='/home/pi/kim/kim/resources/dict/0014.dic')

spk = kim.Speak(device='plughw:0,0',
		resources='/home/pi/kim/kim/resources/audio/')

def handle(phrase):
	print 'Heard: ', phrase
	spk.beep()
	spk.say(phrase)

kim.listener(lstn, spk, handle)

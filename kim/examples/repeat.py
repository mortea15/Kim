#!/usr/bin/env python2
# -*- coding: utf-8-*-
import kim

lstn = kim.Listen(adcdev='plughw:1,0',
                lm='/home/pi/kim/kim/resources/dict/0014.lm',
                dict='/home/pi/kim/kim/resources/dict/0014.dic')

spk = kim.Speak(device='plughw:0,0',
		resources='/home/pi/kim/kim/resources/audio/')

def handle(phrase):
	print 'Heard: ', phrase
	spk.beep(1)
	spk.say(phrase)
	spk.beep(0)

kim.listener(lstn, spk, handle)

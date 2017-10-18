#!/usr/bin/env python2
# -*- coding: utf-8-*-
from whiterose import whiterose

lstn = whiterose.Listen(adcdev='plughw:1,0',
                lm='/home/pi/whiterose/whiterose/resources/dict/6709.lm',
                dict='/home/pi/whiterose/whiterose/resources/dict/6709.dic')

spk = whiterose.Speak(device='plughw:0,0',
		resources='/home/pi/whiterose/whiterose/resources/audio/')

def handle(phrase):
	print 'Heard: ', phrase
	spk.beep()
	spk.say(phrase)

whiterose.listener(lstn, spk, handle)

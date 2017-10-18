#!/usr/bin/env python2
# -*- coding: utf-8-*-
import threading
import subprocess
import os
import re
import time
import tempfile
import Queue as queue


class Listen(threading.Thread):
    def __init__(self, **params):
        super(Listen, self).__init__()
        self._params = params
        self._listening = False
        self.phrase_queue = queue.Queue()

    def listen(self, y):
        self._listening = y

    def run(self):
        def execute(cmd):
            popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
            stdout_lines = iter(popen.stdout.readline, "")

            for stdout_line in stdout_lines:
                yield stdout_line

            popen.stdout.close()
            return_code = popen.wait()
            if return_code != 0:
                raise subprocess.CalledProcessError(return_code, cmd)

        pattern = re.compile('^[0-9]{9}: (.+)')

        cmd = ['pocketsphinx_continuous', '-inmic', 'yes']
        for k, v in self._params.items():
            cmd.extend(['-' + k, v])

        for out in execute(cmd):
            print out,
            if self._listening:
                m = pattern.match(out)
                if m:
                    phrase = m.group(1).strip()
                    if phrase:
                        self.phrase_queue.put(phrase)


class Speak(object):
    def __init__(self, device, resources):
        self._device = device

        if isinstance(resources, dict):
            self._resources = resources
        else:
            self._resources = {'beep': os.path.join(resources, 'beep.wav')}

    def play(self, path):
        cmd = ['aplay', '-D', self._device, path]
        subprocess.call(cmd)

    def beep(self):
        f = self._resources['beep']
        self.play(f)

    def say(self, phrase):
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f:
            fname = f.name

        cmd = ['pico2wave', '-w', fname, phrase.lower()]
        subprocess.call(cmd)

        self.play(fname)
        os.remove(fname)


def listener(lstn, spk, callback,
             callsign='WHITEROSE', attention_span=10, forever=True):
    lstn.daemon = True
    lstn.start()

    def loop():
        while 1:
            lstn.listen(True)
            ph = lstn.phrase_queue.get(block=True)

            if ph.split(' ')[-1] == callsign.upper():
                spk.beep(1)

                try:
                    ph = lstn.phrase_queue.get(block=True, timeout=attention_span)
                except queue.Empty:
                    spk.beep(0)
                else:
                    spk.beep(0)

                    lstn.listen(False)
                    while not lstn.phrase_queue.empty():
                        lstn.phrase_queue.get(block=False)

                    callback(ph)

    t = threading.Thread(target=loop)
    t.daemon = True
    t.start()

    if forever:
        if type(forever) is str:
            print forever

        while 1:
            time.sleep(10)

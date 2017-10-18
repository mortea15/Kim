import unittest
from whiterose import whiterose

spk = whiterose.Speak(device='plughw:0,0',
                resources='../resources/audio')


class Speech(unittest.TestCase):

    def setUp(self):
        print 'Setting up Speech Test'

    def test_beep(self):
        print 'Beep'
        spk.beep()

    def test_speak(self):
        print 'TTS Test'
        spk.say("This is not a drill. I repeat, this is NOT  a drill!")

    def tearDown(self):
        print 'Thanks for testing me. I feel better now.'

if __name__ == "__main__":
    unittest.main()

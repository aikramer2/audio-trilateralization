import pyaudio
import wave
import sys
from scipy.io import wavfile

data = wavfile.read("0_mid.wav")
print data
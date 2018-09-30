''' 
fmsynth

This program requires a working installation of:

On Mac:
    1. portaudio: brew install portaudio
    2. souddevice: pip install sounddevice

TODO:
    Implement Plotting

    Matlab example:

     subplot(2,1,1)
     plot(t(1:5000),x(1:5000))
     subplot(2,1,2)
     plot(fftshift(abs(fft(x))))
'''

import argparse
import numpy as np
import math
import sounddevice as sd

def play(vec, fs=44100):
    sd.play(vec, fs, blocking=True)
    
def main(args):
    fs = args.fs
    T = 1/fs
    dur = args.dur
    t = np.arange(0, dur-T, T)

    A = args.A
    C = args.C
    D = args.D
    M = args.M

    x = A*np.sin(2*np.pi*C*t + D*np.sin(2*np.pi*M*t))
    play(x, fs=fs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fs', 
                        help='choice of frequency', 
                        type=int, 
                        default=44100)
    parser.add_argument('--dur', 
                        help='duration', 
                        type=int, 
                        default=1)
    parser.add_argument('--A', 
                        help='A', 
                        type=int, 
                        default=2)
    parser.add_argument('--C', 
                        help='C', 
                        type=int, 
                        default=210)
    parser.add_argument('--D', 
                        help='D', 
                        type=int, 
                        default=10)
    parser.add_argument('--M', 
                        help='M', 
                        type=int, 
                        default=35)
    args = parser.parse_args()
    main(args)
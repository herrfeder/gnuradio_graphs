#!/usr/bin/python3
# -*- coding: utf-8 -*-


import zmq
import numpy as np
import time
from numpy_audio_helper import float_to_byte
import pyaudio


CHUNK = 1024  # number of audio samples per frame (1024 samples/ chunk)
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK)


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:9999") # connect, not bind, the PUB will bind, only 1 can bind
socket.setsockopt(zmq.SUBSCRIBE, b'') # subscribe to topic of all (needed or else it won't work)

while True:
    if socket.poll(10) != 0: # check if there is a message on the socket
        msg = socket.recv(4096) # grab the message
        dat = np.frombuffer(msg, dtype=np.float32, count=-1) # make sure to use correct data type (complex64 or float32); '-1' means read all data in the buffer
        data = float_to_byte(dat)
        stream.write(data)
    else:
        time.sleep(0.1) # wait 100ms and try again


stream.stop_stream()
stream.close()
p.terminate()

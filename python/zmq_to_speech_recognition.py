#!/usr/bin/python3
# -*- coding: utf-8 -*-


import zmq
import numpy as np
import time
from numpy_audio_helper import float_to_byte
import re
import sys
import speech_recognition_local as sr


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:9999") # connect, not bind, the PUB will bind, only 1 can bind
socket.setsockopt(zmq.SUBSCRIBE, b'') # subscribe to topic of all (needed or else it won't work)


def gen_audio_stream():
    while True:
        msg = socket.recv(4096) # grab the message
        dat = np.frombuffer(msg, dtype=np.float32, count=-1)
        data = float_to_byte(dat)
        yield data



class ZMQStreamWrapper():
    def __init__( self, it ):
        self.it = it
        self.next_chunk = b''
  
    def growChunk( self ):
        self.next_chunk = self.next_chunk + self.it.__next__()
 

    def read( self, n ):
        if self.next_chunk == None:
            return None
        try:
            while len(self.next_chunk)<n:
                self.growChunk()
                rv = self.next_chunk[:n]
                self.next_chunk = self.next_chunk[n:]
                return rv
        except StopIteration:
            rv = self.next_chunk
            self.next_chunk = None
            return rv


if __name__ == "__main__":
    
    # Audio recording parameters
    RATE = 48000
    CHUNK = int(RATE / 10)  # 100ms


    zmq_wrap = ZMQStreamWrapper(gen_audio_stream())
    
    r = sr.Recognizer()
    with sr.AudioFile(zmq_wrap) as source:
        audio = r.record(source)

'''
Traceback (most recent call last):
  File "wrapper_io_stream.py", line 64, in <module>
    audio = r.record(source)
  File "/usr/local/lib/python3.8/dist-packages/speech_recognition/__init__.py", line 449, in record
    buffer = source.stream.read(source.CHUNK)
  File "/usr/local/lib/python3.8/dist-packages/speech_recognition/__init__.py", line 221, in read
    buffer = self.audio_reader.readframes(self.audio_reader.getnframes() if size == -1 else size)
AttributeError: 'ZMQStreamWrapper' object has no attribute 'readframes'
'''


import socket
import pdb; debughere = pdb.set_trace

# from https://github.com/keithdoggett/gr-pocsag-decoder

PAYLOAD_SIZE = 1472  # default GNURadio payload size (in bytes)
UDP_IP_ADDR = "127.0.0.1"
UDP_PORT = 15000

def pop_all(l):
    r, l[:] = l[:], []
    return r


class UdpInterface(object):
    def __init__(self, addr, port, payload_size):
        self.addr = addr
        self.port = port
        self.payload_size = payload_size
        self.sock = self._make_conn()
        self.buffer = []

    def _make_conn(self):
        """
            make connection to the address and port specified
            set self.sock to bound socket
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.addr, self.port))
        print("connected to socket")
        return sock

    def read_socket(self):
        """
            read in data from socket to buffer
            will perform necessary bit flips here and make it
            a string instead of bytes
        """
        data, _ = self.sock.recvfrom(self.payload_size)
        data = bytearray(data)

        for i in data:
            bit = i ^ 1
            self.buffer.append(str(bit))
        return pop_all(self.buffer)


def get_bit_stream(udp_object):
    while True:
        msg = udp_object.read_socket() # grab the message
        yield msg

    

class UDPStreamWrapper():
    def __init__( self, it ): 
        self.it = it
        self.next_chunk = []

    def grow_chunk( self ):
        self.next_chunk.extend(self.it.__next__())

    def read( self, n ):
        if self.next_chunk == None:
            return None
        while len(self.next_chunk)<n:
            self.grow_chunk()
        try:
            rv = self.next_chunk[:n]
            self.next_chunk = self.next_chunk[n:]
            return rv
        except StopIteration:
            rv = self.next_chunk
            self.next_chunk = None
            return rv 


conn = UdpInterface(UDP_IP_ADDR, UDP_PORT, PAYLOAD_SIZE)
udpstream = UDPStreamWrapper(get_bit_stream(conn))

while True:
    print(udpstream.read(4096))

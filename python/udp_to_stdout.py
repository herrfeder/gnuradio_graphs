import socket


# from https://github.com/keithdoggett/gr-pocsag-decoder

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

    def clean_buffer(self, last_idx):
        """
            remove data that is no longer useful in the buffer
            will create a new buffer from curr_buffer[last_idx:]

            may perform other actions eventually
        """
        self.buffer = self.buffer[last_idx:]



PAYLOAD_SIZE = 1472  # default GNURadio payload size (in bytes)
UDP_IP_ADDR = "127.0.0.1"
UDP_PORT = 15000

conn = UdpInterface(UDP_IP_ADDR, UDP_PORT, PAYLOAD_SIZE)
while True:
        conn.read_socket()
        print(conn.buffer)

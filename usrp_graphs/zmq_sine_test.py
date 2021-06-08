#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Zmq Sine Test
# Generated: Wed Jan 20 02:38:12 2016
##################################################

from baz import introspective_xmlrpc_server
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import threading


class zmq_sine_test(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Zmq Sine Test")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.offset = offset = 0
        self.frequency = frequency = 1000
        self.amplitude = amplitude = 50

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, "tcp://*:9231", 100, False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.baz_xmlrpc_server_0 = introspective_xmlrpc_server.IntrospectiveXMLRPCServer(("192.168.10.2", 30000), allow_none=True, signatures={})
        self.baz_xmlrpc_server_0.register_instance(self)
        self.baz_xmlrpc_server_0.register_introspection_functions()
        threading.Thread(target=self.baz_xmlrpc_server_0.serve_forever).start()
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, frequency, amplitude, offset)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.zeromq_push_sink_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.analog_sig_source_x_0.set_offset(self.offset)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.analog_sig_source_x_0.set_frequency(self.frequency)

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.analog_sig_source_x_0.set_amplitude(self.amplitude)


def main(top_block_cls=zmq_sine_test, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()

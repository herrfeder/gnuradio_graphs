#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: e312_wbfm_receiver_filter_no_lowpass
# Generated: Wed Jan 20 09:12:00 2016
##################################################

from baz import introspective_xmlrpc_server
from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import threading
import time


class e312_wbfm_receiver_filter_no_lowpass(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "e312_wbfm_receiver_filter_no_lowpass")

        ##################################################
        # Variables
        ##################################################
        self.server_port = server_port = 30000
        self.server_address = server_address = "192.168.10.2"
        self.samp_rate = samp_rate = 1e6
        self.rf_gain = rf_gain = 50
        self.lowpass_transition = lowpass_transition = 1e4
        self.lowpass_cutoff = lowpass_cutoff = 1e5
        self.center_freq = center_freq = 98.5e6

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_1 = zeromq.push_sink(gr.sizeof_float, 1, "tcp://*:9999", 100, False)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(rf_gain, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=1000,
                taps=None,
                fractional_bw=None,
        )
        self.baz_xmlrpc_server_0 = introspective_xmlrpc_server.IntrospectiveXMLRPCServer((server_address, server_port), allow_none=True, signatures={})
        self.baz_xmlrpc_server_0.register_instance(self)
        self.baz_xmlrpc_server_0.register_introspection_functions()
        threading.Thread(target=self.baz_xmlrpc_server_0.serve_forever).start()
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=1e6,
        	audio_decimation=1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.zeromq_push_sink_1, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.analog_wfm_rcv_0, 0))    

    def get_server_port(self):
        return self.server_port

    def set_server_port(self, server_port):
        self.server_port = server_port

    def get_server_address(self):
        return self.server_address

    def set_server_address(self, server_address):
        self.server_address = server_address

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.uhd_usrp_source_0.set_gain(self.rf_gain, 0)
        	

    def get_lowpass_transition(self):
        return self.lowpass_transition

    def set_lowpass_transition(self, lowpass_transition):
        self.lowpass_transition = lowpass_transition

    def get_lowpass_cutoff(self):
        return self.lowpass_cutoff

    def set_lowpass_cutoff(self, lowpass_cutoff):
        self.lowpass_cutoff = lowpass_cutoff

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 0)


def main(top_block_cls=e312_wbfm_receiver_filter_no_lowpass, options=None):

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

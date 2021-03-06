#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.8.3.1-rc1

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import audio
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import zeromq
from gnuradio.qtgui import Range, RangeWidget
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy

from gnuradio import qtgui

class e312_wbfm_receiver(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "e312_wbfm_receiver")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.set_rf_gain = set_rf_gain = "set_rf_gain"
        self.set_lowpass_transition = set_lowpass_transition = "set_lowpass_transition"
        self.set_lowpass_cutoff = set_lowpass_cutoff = "set_lowpass_cutoff"
        self.set_center_freq = set_center_freq = "set_center_freq"
        self.samp_rate = samp_rate = 48000
        self.rf_gain = rf_gain = 50
        self.lowpass_transition = lowpass_transition = 1e4
        self.lowpass_cutoff = lowpass_cutoff = 1e5
        self.e312sdr = e312sdr = "192.168.10.2"
        self.center_freq = center_freq = 98.5e6

        ##################################################
        # Blocks
        ##################################################
        self._center_freq_range = Range(90e6, 110e6, 1e5, 98.5e6, 200)
        self._center_freq_win = RangeWidget(self._center_freq_range, self.set_center_freq, 'center_freq', "counter_slider", float)
        self.top_layout.addWidget(self._center_freq_win)
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_float, 1, 'tcp://192.168.10.2:9999', 100, False, -1)
        self.xmlrpc_client_0_0_0_0 = ServerProxy('http://e312sdr:30000')
        self.xmlrpc_client_0_0_0 = ServerProxy('http://e312sdr:30000')
        self.xmlrpc_client_0_0 = ServerProxy('http://e312sdr:30000')
        self.xmlrpc_client_0 = ServerProxy('http://e312sdr:30000')
        self._rf_gain_range = Range(0, 100, 5, 50, 200)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, 'rf_gain', "counter_slider", float)
        self.top_layout.addWidget(self._rf_gain_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            center_freq, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self._lowpass_transition_range = Range(0.5e4, 1.5e4, 0.1e4, 1e4, 200)
        self._lowpass_transition_win = RangeWidget(self._lowpass_transition_range, self.set_lowpass_transition, 'lowpass_transition', "counter_slider", float)
        self.top_layout.addWidget(self._lowpass_transition_win)
        self._lowpass_cutoff_range = Range(0.5e5, 1.5e5, 0.1e5, 1e5, 200)
        self._lowpass_cutoff_win = RangeWidget(self._lowpass_cutoff_range, self.set_lowpass_cutoff, 'lowpass_cutoff', "counter_slider", float)
        self.top_layout.addWidget(self._lowpass_cutoff_win)
        self.audio_sink_0 = audio.sink(48000, "plughw:0,0", True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.zeromq_pull_source_0, 0), (self.audio_sink_0, 0))
        self.connect((self.zeromq_pull_source_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "e312_wbfm_receiver")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_set_rf_gain(self):
        return self.set_rf_gain

    def set_set_rf_gain(self, set_rf_gain):
        self.set_rf_gain = set_rf_gain
        self.set_rf_gain(50)

    def get_set_lowpass_transition(self):
        return self.set_lowpass_transition

    def set_set_lowpass_transition(self, set_lowpass_transition):
        self.set_lowpass_transition = set_lowpass_transition
        self.set_lowpass_transition(1e4)

    def get_set_lowpass_cutoff(self):
        return self.set_lowpass_cutoff

    def set_set_lowpass_cutoff(self, set_lowpass_cutoff):
        self.set_lowpass_cutoff = set_lowpass_cutoff
        self.set_lowpass_cutoff(1e5)

    def get_set_center_freq(self):
        return self.set_center_freq

    def set_set_center_freq(self, set_center_freq):
        self.set_center_freq = set_center_freq
        self.set_center_freq(98.5e6)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.xmlrpc_client_0_0.set_rf_gain(self.rf_gain)

    def get_lowpass_transition(self):
        return self.lowpass_transition

    def set_lowpass_transition(self, lowpass_transition):
        self.lowpass_transition = lowpass_transition
        self.xmlrpc_client_0_0_0.set_lowpass_transition(self.lowpass_transition)

    def get_lowpass_cutoff(self):
        return self.lowpass_cutoff

    def set_lowpass_cutoff(self, lowpass_cutoff):
        self.lowpass_cutoff = lowpass_cutoff
        self.xmlrpc_client_0_0_0_0.set_lowpass_cutoff(self.lowpass_cutoff)

    def get_e312sdr(self):
        return self.e312sdr

    def set_e312sdr(self, e312sdr):
        self.e312sdr = e312sdr

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.xmlrpc_client_0.set_center_freq(self.center_freq)





def main(top_block_cls=e312_wbfm_receiver, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()

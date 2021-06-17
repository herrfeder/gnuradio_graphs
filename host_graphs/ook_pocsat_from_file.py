#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ook_pocsat_from_file
# GNU Radio version: v3.8.3.1-2-g18f86220

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
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class ook_pocsat_from_file(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ook_pocsat_from_file")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ook_pocsat_from_file")
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

        self.settings = Qt.QSettings("GNU Radio", "ook_pocsat_from_file")

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
        self.transition_bw = transition_bw = 20000
        self.symbol_rate = symbol_rate = 1200
        self.sqelch = sqelch = -63
        self.samp_rate = samp_rate = 2e6
        self.lowpass_transition = lowpass_transition = 1e3
        self.lowpass_cutoff = lowpass_cutoff = 10e3
        self.fsk_deviation_hz = fsk_deviation_hz = 4.5e3
        self.freq_adjust = freq_adjust = -160e3
        self.decimation = decimation = 10

        ##################################################
        # Blocks
        ##################################################
        self._sqelch_range = Range(-70, -50, 1, -63, 200)
        self._sqelch_win = RangeWidget(self._sqelch_range, self.set_sqelch, 'sqelch', "counter_slider", float)
        self.top_layout.addWidget(self._sqelch_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            466.07e6, #fc
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
        self._lowpass_transition_range = Range(1000, 30e3, 1000, 1e3, 200)
        self._lowpass_transition_win = RangeWidget(self._lowpass_transition_range, self.set_lowpass_transition, 'lowpass_transition', "counter_slider", float)
        self.top_layout.addWidget(self._lowpass_transition_win)
        self._lowpass_cutoff_range = Range(5e3, 50e3, 1000, 10e3, 200)
        self._lowpass_cutoff_win = RangeWidget(self._lowpass_cutoff_range, self.set_lowpass_cutoff, 'lowpass_cutoff', "counter_slider", float)
        self.top_layout.addWidget(self._lowpass_cutoff_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_fcc(decimation, firdes.low_pass(1,samp_rate, fsk_deviation_hz, fsk_deviation_hz*decimation), 0, samp_rate)
        self._freq_adjust_range = Range(-1000e3, 1000e3, 1e3, -160e3, 200)
        self._freq_adjust_win = RangeWidget(self._freq_adjust_range, self.set_freq_adjust, 'freq_adjust', "counter_slider", float)
        self.top_layout.addWidget(self._freq_adjust_win)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samp_rate/(decimation*symbol_rate)*(1+0.0), 0.01, 0, 0.1, 0.01)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1472, '127.0.0.1', 15000, 1472, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_char*1, 1472)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/root/test_ook_output', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ook_pocsat_from_file")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_transition_bw(self):
        return self.transition_bw

    def set_transition_bw(self, transition_bw):
        self.transition_bw = transition_bw

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_rate/(self.decimation*self.symbol_rate)*(1+0.0))

    def get_sqelch(self):
        return self.sqelch

    def set_sqelch(self, sqelch):
        self.sqelch = sqelch

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_rate/(self.decimation*self.symbol_rate)*(1+0.0))
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1,self.samp_rate, self.fsk_deviation_hz, self.fsk_deviation_hz*self.decimation))
        self.qtgui_freq_sink_x_0.set_frequency_range(466.07e6, self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_lowpass_transition(self):
        return self.lowpass_transition

    def set_lowpass_transition(self, lowpass_transition):
        self.lowpass_transition = lowpass_transition

    def get_lowpass_cutoff(self):
        return self.lowpass_cutoff

    def set_lowpass_cutoff(self, lowpass_cutoff):
        self.lowpass_cutoff = lowpass_cutoff

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1,self.samp_rate, self.fsk_deviation_hz, self.fsk_deviation_hz*self.decimation))

    def get_freq_adjust(self):
        return self.freq_adjust

    def set_freq_adjust(self, freq_adjust):
        self.freq_adjust = freq_adjust

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_rate/(self.decimation*self.symbol_rate)*(1+0.0))
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1,self.samp_rate, self.fsk_deviation_hz, self.fsk_deviation_hz*self.decimation))





def main(top_block_cls=ook_pocsat_from_file, options=None):

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

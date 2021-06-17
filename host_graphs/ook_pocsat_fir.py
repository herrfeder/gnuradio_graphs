#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ook_pocsat_fir
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
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
import math
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class ook_pocsat_fir(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ook_pocsat_fir")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ook_pocsat_fir")
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

        self.settings = Qt.QSettings("GNU Radio", "ook_pocsat_fir")

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
        self.sqelch = sqelch = -65
        self.samp_rate = samp_rate = 2e6
        self.offset = offset = 0
        self.lowpass_transition = lowpass_transition = 1e3
        self.lowpass_cutoff = lowpass_cutoff = 10e3
        self.fsk_deviation_hz = fsk_deviation_hz = 2.5e3
        self.freq_adjust = freq_adjust = -229.3e3
        self.decimation = decimation = 20
        self.choose_freq = choose_freq = 466.07e6-7e4

        ##################################################
        # Blocks
        ##################################################
        self._sqelch_range = Range(-70, -50, 1, -65, 200)
        self._sqelch_win = RangeWidget(self._sqelch_range, self.set_sqelch, 'sqelch', "counter_slider", float)
        self.top_layout.addWidget(self._sqelch_win)
        self._freq_adjust_range = Range(-1000e3, 1000e3, 1e3, -229.3e3, 200)
        self._freq_adjust_win = RangeWidget(self._freq_adjust_range, self.set_freq_adjust, 'freq_adjust', "counter_slider", float)
        self.top_layout.addWidget(self._freq_adjust_win)
        # Create the options list
        self._choose_freq_options = [466230000.0, 465970000.0, 466000000.0, 3, 4]
        # Create the labels list
        self._choose_freq_labels = ['466.23e6', '465.97e6', '466.07e6', '3', '4']
        # Create the combo box
        self._choose_freq_tool_bar = Qt.QToolBar(self)
        self._choose_freq_tool_bar.addWidget(Qt.QLabel("choose_freq: "))
        self._choose_freq_combo_box = Qt.QComboBox()
        self._choose_freq_tool_bar.addWidget(self._choose_freq_combo_box)
        for _label in self._choose_freq_labels: self._choose_freq_combo_box.addItem(_label)
        self._choose_freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._choose_freq_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._choose_freq_options.index(i)))
        self._choose_freq_callback(self.choose_freq)
        self._choose_freq_combo_box.currentIndexChanged.connect(
            lambda i: self.set_choose_freq(self._choose_freq_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._choose_freq_tool_bar)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_center_freq(choose_freq, 0)
        self.uhd_usrp_source_0.set_gain(50, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec())
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=int(2000),
                taps=None,
                fractional_bw=0.4)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            choose_freq, #fc
            samp_rate/decimation, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate/decimation, #samp_rate
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
        self.qtgui_freq_sink_x_0_0_0_0 = qtgui.freq_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            choose_freq, #fc
            samp_rate/decimation, #bw
            'after_nbfm', #name
            1
        )
        self.qtgui_freq_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0.enable_control_panel(False)


        self.qtgui_freq_sink_x_0_0_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            choose_freq, #fc
            samp_rate/decimation, #bw
            'after_lowpass', #name
            1
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)



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
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self._offset_range = Range(-5, 5, 0.1, 0, 200)
        self._offset_win = RangeWidget(self._offset_range, self.set_offset, 'offset', "counter_slider", float)
        self.top_layout.addWidget(self._offset_win)
        self._lowpass_transition_range = Range(1000, 30e3, 1000, 1e3, 200)
        self._lowpass_transition_win = RangeWidget(self._lowpass_transition_range, self.set_lowpass_transition, 'lowpass_transition', "counter_slider", float)
        self.top_layout.addWidget(self._lowpass_transition_win)
        self._lowpass_cutoff_range = Range(5e3, 50e3, 1000, 10e3, 200)
        self._lowpass_cutoff_win = RangeWidget(self._lowpass_cutoff_range, self.set_lowpass_cutoff, 'lowpass_cutoff', "counter_slider", float)
        self.top_layout.addWidget(self._lowpass_cutoff_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(decimation, firdes.low_pass(5, samp_rate, samp_rate/(10*decimation), 1000), choose_freq, samp_rate)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samp_rate/(decimation*symbol_rate)*(1+0.0), 0.01, 0, 0.1, 0.01)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_udp_sink_1 = blocks.udp_sink(gr.sizeof_int*1, '127.0.0.1', 14000, 1, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1472, '127.0.0.1', 15000, 1472, True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_char*1, 1472)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_float_to_int_0 = blocks.float_to_int(1, 100)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(0.5)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(sqelch, 1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_adjust, 1, 0, 0)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf((samp_rate/(decimation))/(2*math.pi*fsk_deviation_hz/8.0))
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=int(samp_rate),
        	quad_rate=int(samp_rate),
        	tau=75e-6,
        	max_dev=fsk_deviation_hz,
          )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_float_to_int_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_float_to_int_0, 0), (self.blocks_udp_sink_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_simple_squelch_cc_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ook_pocsat_fir")
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
        self.analog_simple_squelch_cc_0.set_threshold(self.sqelch)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/(self.decimation))/(2*math.pi*self.fsk_deviation_hz/8.0))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_rate/(self.decimation*self.symbol_rate)*(1+0.0))
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(5, self.samp_rate, self.samp_rate/(10*self.decimation), 1000))
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.choose_freq, self.samp_rate/self.decimation)
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(self.choose_freq, self.samp_rate/self.decimation)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate/self.decimation)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.choose_freq, self.samp_rate/self.decimation)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset

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
        self.analog_nbfm_rx_0.set_max_deviation(self.fsk_deviation_hz)
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/(self.decimation))/(2*math.pi*self.fsk_deviation_hz/8.0))

    def get_freq_adjust(self):
        return self.freq_adjust

    def set_freq_adjust(self, freq_adjust):
        self.freq_adjust = freq_adjust
        self.analog_sig_source_x_0.set_frequency(self.freq_adjust)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/(self.decimation))/(2*math.pi*self.fsk_deviation_hz/8.0))
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_rate/(self.decimation*self.symbol_rate)*(1+0.0))
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(5, self.samp_rate, self.samp_rate/(10*self.decimation), 1000))
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.choose_freq, self.samp_rate/self.decimation)
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(self.choose_freq, self.samp_rate/self.decimation)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate/self.decimation)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.choose_freq, self.samp_rate/self.decimation)

    def get_choose_freq(self):
        return self.choose_freq

    def set_choose_freq(self, choose_freq):
        self.choose_freq = choose_freq
        self._choose_freq_callback(self.choose_freq)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.choose_freq)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.choose_freq, self.samp_rate/self.decimation)
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(self.choose_freq, self.samp_rate/self.decimation)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.choose_freq, self.samp_rate/self.decimation)
        self.uhd_usrp_source_0.set_center_freq(self.choose_freq, 0)





def main(top_block_cls=ook_pocsat_fir, options=None):

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

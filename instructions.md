# USRP E312 Setup
## My Files

  * https://github.com/herrfeder/gnuradio_graphs


## Build UHD from Source on Host

https://files.ettus.com/manual/page_build_guide.html

  * this tutorial is working but it's more feasible to do it with PyBombs


## Build UHD and GnuRadio with PyBombs

https://github.com/gnuradio/pybombs

  * this approach is fast forward but for having the latest UHD 4.0.0.0 we have to adapt the recipes:
  * after doing
  ```
  sudo apt-get install python3-pip
	sudo pip3 install pybombs
	pybombs auto-config
	pybombs recipes add-defaults
  ```
  
  * we go into `.pybombs/recipes/gr-recipes/` and editing `uhd.lwr`
    * we replace `gitbranch` with `gitbranch: v4.0.0.0`
    
  * now we can continue:
  ```
  pybombs prefix init ~/prefix-3.8 -R gnuradio-default
	source ~/prefix-3.8/setup_env.sh
	gnuradio-companion
  ```

## Downloading and Burning SD Card Images


### With UHD 4.0 

  * when successfully installed latest UHD (4.0.0.0) with PyBombs then we can download the UHD v4.0 Image for the E312:

```bash
uhd_images_downloader -t sdimg -t e310 -t sg3
```

  * this is the path for the recent SDCard Image

https://kb.ettus.com/Writing_the_USRP_File_System_Disk_Image_to_a_SD_Card

  * Latest Image:
    * https://files.ettus.com/e3xx_images/e3xx-release-4/ettus-e3xx-sg3/

### Old Legacy Images

  * https://kb.ettus.com/E310/E312#SD_Card_Images
  * https://files.ettus.com/e3xx_images/

## Communicate with USRP

  * check connected usrp
```
uhd_usrp_probe --args="addr=192.168.10.2"
```

### Network on UHD 4.0.0.0

Place following config into `/lib/systemd/network`:

```
[Match]
Name=eth0

[Network]
Address=192.168.10.2/24
Gateway=192.168.10.1
DNS=192.168.10.1
```

## Gnuradio in Docker

  * I'm using the following Dockerfile with some adaptioins:
    * https://github.com/EttusResearch/ettus-docker/blob/master/ubuntu-uhd/Dockerfile

```
docker build . -t usrp_gnuradio
docker run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix  --network=host -e DISPLAY=unix$DISPLAY usrp_gnuradio:latest
```

  * https://gitlab.com/librespacefoundation/sdrmakerspace/sdr-pr/-/wikis/Partial-reconfiguration-on-the-E310-Board/Tools%20installation%20RFNoC,%20UHD,%20GNU%20Radio
  
  * https://kb.ettus.com/Streaming_processed_data_from_the_E31x_with_GNU_Radio_and_ZMQhttps://kb.ettus.com/Streaming_processed_data_from_the_E31x_with_GNU_Radio_and_ZMQ



## ZMQ Read to Python


  * I used this gist for converting from float to pcm
    * https://gist.github.com/HudsonHuang/fbdf8e9af7993fe2a91620d3fb86a182 --> numpy_audio_helper.py

  * In my repository I have some examples how to process the raw ZMQ Stream from gnuradio
    * https://github.com/herrfeder/gnuradio_graphs/tree/main/python
    
  * zmq_to_google_speech is hard to accomplish as Google Speech-To-Text-API has very strict requirements for how to process the audio stream:
    * https://cloud.google.com/speech-to-text/docs/streaming-recognize
    * --> rebuilding it with the zmq stream seems to be a bigger effort
    
  * wrapper_io_stream wraps the zmq stream into a generator and on top into a file-like object
  * additionally I adapted https://github.com/Uberi/speech_recognition for working with a stream instead a WAVE/FLAC file but the file-like wrapper needs more methods the FLAC oder WAVE libraries are exposing


# On USRP (Old Version)

## Problems

### The rational_resampler_fcc is missing in filter

  * running e312_fm
```
Traceback (most recent call last):
  File "/home/e312_fm_receiver_zmq.py", line 108, in <module>
    main()
  File "/home/e312_fm_receiver_zmq.py", line 97, in main
    tb = top_block_cls()
  File "/home/e312_fm_receiver_zmq.py", line 49, in __init__
    self.rational_resampler_xxx_0 = filter.rational_resampler_fcc(
AttributeError: 'module' object has no attribute 'rational_resampler_fcc'
Traceback (most recent call last):
  File "/home/e312_fm_receiver_zmq.py", line 108, in <module>
    main()
  File "/home/e312_fm_receiver_zmq.py", line 97, in main
    tb = top_block_cls()
  File "/home/e312_fm_receiver_zmq.py", line 49, in __init__
    self.rational_resampler_xxx_0 = filter.rational_resampler_fcc(
AttributeError: 'module' object has no attribute 'rational_resampler_fcc'
```

  * the necessary rational_resampler_fcc is missing in the module:
  ```
  >>> dir(filter)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', 'analysis_filterbank', 'blocks', 'dc_blocker_cc', 'dc_blocker_cc_make', 'dc_blocker_cc_sptr', 'dc_blocker_cc_sptr_swigregister', 'dc_blocker_cc_swigregister', 'dc_blocker_ff', 'dc_blocker_ff_make', 'dc_blocker_ff_sptr', 'dc_blocker_ff_sptr_swigregister', 'dc_blocker_ff_swigregister', 'design_filter', 'fft', 'fft_filter_ccc', 'fft_filter_ccc_make', 'fft_filter_ccc_sptr', 'fft_filter_ccc_sptr_swigregister', 'fft_filter_ccc_swigregister', 'fft_filter_ccf', 'fft_filter_ccf_make', 'fft_filter_ccf_sptr', 'fft_filter_ccf_sptr_swigregister', 'fft_filter_ccf_swigregister', 'fft_filter_fff', 'fft_filter_fff_make', 'fft_filter_fff_sptr', 'fft_filter_fff_sptr_swigregister', 'fft_filter_fff_swigregister', 'filter', 'filter_delay_fc', 'filter_delay_fc_make', 'filter_delay_fc_sptr', 'filter_delay_fc_sptr_swigregister', 'filter_delay_fc_swigregister', 'filter_swig', 'filterbank', 'filterbank_vcvcf', 'filterbank_vcvcf_make', 'filterbank_vcvcf_sptr', 'filterbank_vcvcf_sptr_swigregister', 'filterbank_vcvcf_swigregister', 'fir_filter_ccc', 'fir_filter_ccc_make', 'fir_filter_ccc_sptr', 'fir_filter_ccc_sptr_swigregister', 'fir_filter_ccc_swigregister', 'fir_filter_ccf', 'fir_filter_ccf_make', 'fir_filter_ccf_sptr', 'fir_filter_ccf_sptr_swigregister', 'fir_filter_ccf_swigregister', 'fir_filter_fcc', 'fir_filter_fcc_make', 'fir_filter_fcc_sptr', 'fir_filter_fcc_sptr_swigregister', 'fir_filter_fcc_swigregister', 'fir_filter_fff', 'fir_filter_fff_make', 'fir_filter_fff_sptr', 'fir_filter_fff_sptr_swigregister', 'fir_filter_fff_swigregister', 'fir_filter_fsf', 'fir_filter_fsf_make', 'fir_filter_fsf_sptr', 'fir_filter_fsf_sptr_swigregister', 'fir_filter_fsf_swigregister', 'fir_filter_scc', 'fir_filter_scc_make', 'fir_filter_scc_sptr', 'fir_filter_scc_sptr_swigregister', 'fir_filter_scc_swigregister', 'firdes', 'firdes_band_pass', 'firdes_band_pass_2', 'firdes_band_reject', 'firdes_band_reject_2', 'firdes_complex_band_pass', 'firdes_complex_band_pass_2', 'firdes_gaussian', 'firdes_high_pass', 'firdes_high_pass_2', 'firdes_hilbert', 'firdes_low_pass', 'firdes_low_pass_2', 'firdes_root_raised_cosine', 'firdes_swigregister', 'firdes_window', 'fractional_interpolator_cc', 'fractional_interpolator_cc_make', 'fractional_interpolator_cc_sptr', 'fractional_interpolator_cc_sptr_swigregister', 'fractional_interpolator_cc_swigregister', 'fractional_interpolator_ff', 'fractional_interpolator_ff_make', 'fractional_interpolator_ff_sptr', 'fractional_interpolator_ff_sptr_swigregister', 'fractional_interpolator_ff_swigregister', 'fractional_resampler_cc', 'fractional_resampler_cc_make', 'fractional_resampler_cc_sptr', 'fractional_resampler_cc_sptr_swigregister', 'fractional_resampler_cc_swigregister', 'fractional_resampler_ff', 'fractional_resampler_ff_make', 'fractional_resampler_ff_sptr', 'fractional_resampler_ff_sptr_swigregister', 'fractional_resampler_ff_swigregister', 'freq_xlating_fft_filter', 'freq_xlating_fft_filter_ccc', 'freq_xlating_fir_filter_ccc', 'freq_xlating_fir_filter_ccc_make', 'freq_xlating_fir_filter_ccc_sptr', 'freq_xlating_fir_filter_ccc_sptr_swigregister', 'freq_xlating_fir_filter_ccc_swigregister', 'freq_xlating_fir_filter_ccf', 'freq_xlating_fir_filter_ccf_make', 'freq_xlating_fir_filter_ccf_sptr', 'freq_xlating_fir_filter_ccf_sptr_swigregister', 'freq_xlating_fir_filter_ccf_swigregister', 'freq_xlating_fir_filter_fcc', 'freq_xlating_fir_filter_fcc_make', 'freq_xlating_fir_filter_fcc_sptr', 'freq_xlating_fir_filter_fcc_sptr_swigregister', 'freq_xlating_fir_filter_fcc_swigregister', 'freq_xlating_fir_filter_fcf', 'freq_xlating_fir_filter_fcf_make', 'freq_xlating_fir_filter_fcf_sptr', 'freq_xlating_fir_filter_fcf_sptr_swigregister', 'freq_xlating_fir_filter_fcf_swigregister', 'freq_xlating_fir_filter_scc', 'freq_xlating_fir_filter_scc_make', 'freq_xlating_fir_filter_scc_sptr', 'freq_xlating_fir_filter_scc_sptr_swigregister', 'freq_xlating_fir_filter_scc_swigregister', 'freq_xlating_fir_filter_scf', 'freq_xlating_fir_filter_scf_make', 'freq_xlating_fir_filter_scf_sptr', 'freq_xlating_fir_filter_scf_sptr_swigregister', 'freq_xlating_fir_filter_scf_swigregister', 'gr', 'gru', 'high_res_timer_epoch', 'high_res_timer_now', 'high_res_timer_now_perfmon', 'high_res_timer_tps', 'hilbert_fc', 'hilbert_fc_make', 'hilbert_fc_sptr', 'hilbert_fc_sptr_swigregister', 'hilbert_fc_swigregister', 'iir_filter_ccc', 'iir_filter_ccc_make', 'iir_filter_ccc_sptr', 'iir_filter_ccc_sptr_swigregister', 'iir_filter_ccc_swigregister', 'iir_filter_ccd', 'iir_filter_ccd_make', 'iir_filter_ccd_sptr', 'iir_filter_ccd_sptr_swigregister', 'iir_filter_ccd_swigregister', 'iir_filter_ccf', 'iir_filter_ccf_make', 'iir_filter_ccf_sptr', 'iir_filter_ccf_sptr_swigregister', 'iir_filter_ccf_swigregister', 'iir_filter_ccz', 'iir_filter_ccz_make', 'iir_filter_ccz_sptr', 'iir_filter_ccz_sptr_swigregister', 'iir_filter_ccz_swigregister', 'iir_filter_ffd', 'iir_filter_ffd_make', 'iir_filter_ffd_sptr', 'iir_filter_ffd_sptr_swigregister', 'iir_filter_ffd_swigregister', 'interp_fir_filter_ccc', 'interp_fir_filter_ccc_make', 'interp_fir_filter_ccc_sptr', 'interp_fir_filter_ccc_sptr_swigregister', 'interp_fir_filter_ccc_swigregister', 'interp_fir_filter_ccf', 'interp_fir_filter_ccf_make', 'interp_fir_filter_ccf_sptr', 'interp_fir_filter_ccf_sptr_swigregister', 'interp_fir_filter_ccf_swigregister', 'interp_fir_filter_fcc', 'interp_fir_filter_fcc_make', 'interp_fir_filter_fcc_sptr', 'interp_fir_filter_fcc_sptr_swigregister', 'interp_fir_filter_fcc_swigregister', 'interp_fir_filter_fff', 'interp_fir_filter_fff_make', 'interp_fir_filter_fff_sptr', 'interp_fir_filter_fff_sptr_swigregister', 'interp_fir_filter_fff_swigregister', 'interp_fir_filter_fsf', 'interp_fir_filter_fsf_make', 'interp_fir_filter_fsf_sptr', 'interp_fir_filter_fsf_sptr_swigregister', 'interp_fir_filter_fsf_swigregister', 'interp_fir_filter_scc', 'interp_fir_filter_scc_make', 'interp_fir_filter_scc_sptr', 'interp_fir_filter_scc_sptr_swigregister', 'interp_fir_filter_scc_swigregister', 'optfir', 'os', 'pfb', 'pfb_arb_resampler_ccc', 'pfb_arb_resampler_ccc_make', 'pfb_arb_resampler_ccc_sptr', 'pfb_arb_resampler_ccc_sptr_swigregister', 'pfb_arb_resampler_ccc_swigregister', 'pfb_arb_resampler_ccf', 'pfb_arb_resampler_ccf_make', 'pfb_arb_resampler_ccf_sptr', 'pfb_arb_resampler_ccf_sptr_swigregister', 'pfb_arb_resampler_ccf_swigregister', 'pfb_arb_resampler_fff', 'pfb_arb_resampler_fff_make', 'pfb_arb_resampler_fff_sptr', 'pfb_arb_resampler_fff_sptr_swigregister', 'pfb_arb_resampler_fff_swigregister', 'pfb_channelizer_ccf', 'pfb_channelizer_ccf_make', 'pfb_channelizer_ccf_sptr', 'pfb_channelizer_ccf_sptr_swigregister', 'pfb_channelizer_ccf_swigregister', 'pfb_decimator_ccf', 'pfb_decimator_ccf_make', 'pfb_decimator_ccf_sptr', 'pfb_decimator_ccf_sptr_swigregister', 'pfb_decimator_ccf_swigregister', 'pfb_interpolator_ccf', 'pfb_interpolator_ccf_make', 'pfb_interpolator_ccf_sptr', 'pfb_interpolator_ccf_sptr_swigregister', 'pfb_interpolator_ccf_swigregister', 'pfb_synthesizer_ccf', 'pfb_synthesizer_ccf_make', 'pfb_synthesizer_ccf_sptr', 'pfb_synthesizer_ccf_sptr_swigregister', 'pfb_synthesizer_ccf_swigregister', 'pm_remez', 'rational_resampler', 'rational_resampler_base_ccc', 'rational_resampler_base_ccc_make', 'rational_resampler_base_ccc_sptr', 'rational_resampler_base_ccc_sptr_swigregister', 'rational_resampler_base_ccc_swigregister', 'rational_resampler_base_ccf', 'rational_resampler_base_ccf_make', 'rational_resampler_base_ccf_sptr', 'rational_resampler_base_ccf_sptr_swigregister', 'rational_resampler_base_ccf_swigregister', 'rational_resampler_base_fcc', 'rational_resampler_base_fcc_make', 'rational_resampler_base_fcc_sptr', 'rational_resampler_base_fcc_sptr_swigregister', 'rational_resampler_base_fcc_swigregister', 'rational_resampler_base_fff', 'rational_resampler_base_fff_make', 'rational_resampler_base_fff_sptr', 'rational_resampler_base_fff_sptr_swigregister', 'rational_resampler_base_fff_swigregister', 'rational_resampler_base_fsf', 'rational_resampler_base_fsf_make', 'rational_resampler_base_fsf_sptr', 'rational_resampler_base_fsf_sptr_swigregister', 'rational_resampler_base_fsf_swigregister', 'rational_resampler_base_scc', 'rational_resampler_base_scc_make', 'rational_resampler_base_scc_sptr', 'rational_resampler_base_scc_sptr_swigregister', 'rational_resampler_base_scc_swigregister', 'rational_resampler_ccc', 'rational_resampler_ccf', 'rational_resampler_fff', 'single_pole_iir_filter_cc', 'single_pole_iir_filter_cc_make', 'single_pole_iir_filter_cc_sptr', 'single_pole_iir_filter_cc_sptr_swigregister', 'single_pole_iir_filter_cc_swigregister', 'single_pole_iir_filter_ff', 'single_pole_iir_filter_ff_make', 'single_pole_iir_filter_ff_sptr', 'single_pole_iir_filter_ff_sptr_swigregister', 'single_pole_iir_filter_ff_swigregister', 'synthesis_filterbank', 'sys', 'window']
>>> filter.__file__
'/usr/lib/python2.7/site-packages/gnuradio/filter/__init__.pyc'
```

> Add the class prototype into `/usr/lib/python2.7/site-packages/gnuradio/filter/rational_resampler.py`
{.is-success}

```python
class rational_resampler_fcc(_rational_resampler_base):
    def __init__(self, interpolation, decimation, taps=None, fractional_bw=None):
        """
        Rational resampling polyphase FIR filter with
        complex input, complex output and complex taps.
        """
        _rational_resampler_base.__init__(self, filter.rational_resampler_base_fcc,
                                          interpolation, decimation, taps, fractional_bw)
```

# On Docker Host
  
>   The X11 QT Gui Stuff with multiple popping windows is difficult to forward via Docker, therefore it's a bad idea and should be done using a virtual machine.
{.is-danger}

  
## Problems

### ZMQ is missing
```
  Missing Traceback (most recent call last):
  File "/home/untitled.py", line 33, in <module>
    from gnuradio import zeromq
  File "/usr/lib/python3/dist-packages/gnuradio/zeromq/__init__.py", line 37, in <module>
    from .probe_manager import probe_manager
  File "/usr/lib/python3/dist-packages/gnuradio/zeromq/probe_manager.py", line 25, in <module>
    import zmq
ModuleNotFoundError: No module named 'zmq'
```  

> zmq was only installed for Python2.7. Installing `apt install python3-zmq` solved it
{.is-success}

### DBUS issues in Docker container

```
dbus[378]: The last reference on a connection was dropped without closing the connection. This is a bug in an application. See dbus_connection_unref() documentation for details.
Most likely, the application was supposed to call dbus_connection_close(), since this is a private connection.
  D-Bus not built with -rdynamic so unable to print a backtrace

```

  * somehow connected to this issue https://answers.ros.org/question/301056/ros2-rviz-in-docker-container/

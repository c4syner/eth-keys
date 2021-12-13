#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""
import argparse
import math
import shutil

import numpy as np
from numpy import fft
import sounddevice as sd

# @dev Return list of magnitudes of microphone
# @param duration How many recording events
# @param how many chars of noise to collect
def get_audio_noise(duration: int, gain: int) -> int:
    def int_or_str(text):
        """Helper function for argument parsing."""
        try:
            return int(text)
        except ValueError:
            return text
    try:
        columns, _ = shutil.get_terminal_size()
    except AttributeError:
        columns = 80

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        '-b', '--block-duration', type=float, metavar='DURATION', default=50,
        help='block size (default %(default)s milliseconds)')
    parser.add_argument(
        '-c', '--columns', type=int, default=columns,
        help='width of spectrogram')
    parser.add_argument(
        '-d', '--device', type=int_or_str,
        help='input device (numeric ID or substring)')
    parser.add_argument(
        '-g', '--gain', type=float, default=gain,
        help='initial gain factor (default %(default)s)')
    parser.add_argument(
        '-r', '--range', type=float, nargs=2,
        metavar=('LOW', 'HIGH'), default=[100, 2000],
        help='frequency range (default %(default)s Hz)')
    args = parser.parse_args(remaining)
    low = 100
    high = 2000
    if high <= low:
        parser.error('HIGH must be greater than LOW')


    try:
        samplerate = sd.query_devices(args.device, 'input')['default_samplerate']
        bsize = (int(samplerate * args.block_duration / 1000))
        delta_f = (high - low) / (args.columns - 1)
        fftsize = math.ceil(samplerate / delta_f)
        low_bin = math.floor(low / delta_f)
        def callback(indata):
            magnitude = np.abs(np.fft.rfft(indata[:fftsize], n=fftsize))
            magnitude *= args.gain / fftsize
            return (sum(magnitude))
        data = []
        with sd.InputStream(device=args.device, channels=1,
                            blocksize=bsize,
                            samplerate=samplerate) as f:
            while(True):
                dt = [i[0] for i in f.read(bsize)[0]]
                data.append(callback(dt))
                if(len(data) > duration):
                    return data
    except KeyboardInterrupt:
        parser.exit('Interrupted by user')
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))
    
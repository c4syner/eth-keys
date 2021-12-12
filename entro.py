import pyautogui
import time
import random
from web3 import Web3
import pyaudio


# @dev retrieve some audio data from the mic
# @param seconds how long to record for
def rec_audio(seconds: int) -> str:
    CHUNK = 1024
    WIDTH = 2
    CHANNELS = 2
    RATE = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        stream.write(data, CHUNK)
    return data

# @dev Retrieve a "random" number between up and lower bounds
# @param bottom index (inclusive)
# @param top index (exclusive)
# @param _seed number to sample between the above numbers
def mapping(bottom, top, _seed):
    return  (_seed % (top)) if (_seed % top) >= bottom else (_seed % (top))+bottom

# @dev Generates a keccak256 hash from some mouse positions.  
# @param record How many bytes to read
# @param encoding 0: In House ASCII Encoding Algorithm (94 "chars")
# @param encoding 1: BIP-0039 Word List (2048 "chars")

def entropy_event(record: int, encoding: int = 0) -> str:
    with open("bip_wordlist.csv", "r") as f:
        wl = f.readlines()
    init = time.time()
    master_string = ""
    b_last = -1
    i = 1
    while(record > i):
        x, y = pyautogui.position()
        d = rec_audio(2)   
        print(d)
        entr_int = (x * y) ^ d
        if(x*y == b_last):
            continue
        
        b_last = Web3.toInt(Web3.keccak(text=str(x*y))) #seed a keccak256 hashing function with our entropy bit
        if(encoding):
            master_string += wl[b_last % 2048]
        else:
            master_string += chr(mapping(33, 127, b_last))
        i += 1
    return master_string

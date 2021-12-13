import pyautogui
import time
import random
from web3 import Web3
import e_audio


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
    suff = -1
    i = 1
    while(record > i):
        x, y = pyautogui.position()
        d = int(str(e_audio.get_audio_noise(0, 200)[0])[-7:])
        entr_int = str((x*y)^(d))

        if(x*y == suff):
            continue
        suff = x*y
        b_last = Web3.toInt(Web3.keccak(text=entr_int)) #seed a keccak256 hashing function with our entropy bit
        if(encoding):
            master_string += wl[b_last % 2048][:-1] + " "
        else:
            master_string += chr(mapping(33, 127, b_last))
        i += 1
    print("Done!")
    return master_string

import pyautogui
import time

# @dev Retrieve a "random" number between up and lower bounds
# @param bottom index (inclusive)
# @param top index (exclusive)
# @param _seed number to sample between the above numbers
def mapping(bottom, top, _seed):
    return  (_seed % (top)) if (_seed % top) >= bottom else (_seed % (top))+bottom

# @dev Generates a keccak256 hash from some mouse positions.  
# @param record How many bytes to read
def entropy_event(record: int) -> str:
    init = time.time()
    master_string = ""
    b_last = -1
    i = 1
    while(record > i):
        x, y = pyautogui.position()
        if(x*y == b_last):
            continue
        b_last = x*y
        master_string += chr(mapping(33, 127, b_last))
        i += 1
    return master_string

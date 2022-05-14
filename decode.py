from base64 import decode
import code
from itertools import count


def numWays(decoded):
    codes = { str(key - 96) : chr(key) for key in range(97, 97 + 26)}
    # reversed = {value : key for key, value in codes.items() }
    counter = 0
    if decoded.length < 1:
        return ''
    else:
        if decoded.legth == 1:
            counter += 1
            return counter
        else:
            counter += 1
            return numWays(deco)
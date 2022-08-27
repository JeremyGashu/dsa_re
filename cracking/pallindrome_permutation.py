from itertools import count
from typing import Counter


def pallindrmePermutation(s: str) -> bool:
    if s.strip() == '':
        return True
    s = ''.join(s.strip().lower().split(' '))
    print(s)
    count = Counter(s)
    hasOdd = False
    for c in count.values():
        if c % 2 == 1:
            if not hasOdd:
                hasOdd = True
            else:
                return False
    return True


if __name__ == '__main__':
    print(pallindrmePermutation('Tact Coa'))

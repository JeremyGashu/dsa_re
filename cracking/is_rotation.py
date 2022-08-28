from typing import Counter


def isRotation(s1: str, s2: str) -> bool:
    if len(s1) == len(s2) and len(s1) > 0:
        total = s1 + s1
        return s2 in total

    return False


if __name__ == '__main__':
    print(isRotation('waterbottle', 'rbottlewat'))

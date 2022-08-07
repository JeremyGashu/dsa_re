from typing import List


def special(s: List):
    if len(s) < 1:
        return -1
    s.sort()
    special_int = s[0]
    length = len(s)
    for i in range(length):
        # print(length - i - 1)
        if i == (length - i - 1):
            special_int = i

    if special_int == 0:
        return -1
    return special_int


print(special([0, 1, 2, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4]))

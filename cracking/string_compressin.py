from typing import Counter


def stringCompression(s: str) -> str:
    if s == '':
        return ''
    current = ''
    count = 0
    res = ''
    for i in range(len(s)):
        if current == '':
            current = s[i]
            count = 1
        else:
            if current == s[i]:
                count += 1
            else:
                res += s[i - 1] + str(count)
                count = 1
                current = s[i]
    res += current + str(count)
    if len(res) >= len(s):
        return s
    return res


if __name__ == '__main__':
    print(stringCompression('aaabbbcbbbbbddddddeeeeeeffffgge'))

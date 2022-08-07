def getMappings(a:str):
    counter = {}
    for i in a:
        counter.setdefault(i, 0)
        counter[i] += 1

    return counter

def checkStringPermutation(a:str, b:str) -> bool:
    if len(a) > len(b):
        return False
    l, r = 0, len(a) - 1
    while r < len(b):
        if getMappings(b[l:r + 1]) == getMappings(a):
            return True
        l += 1
        r += 1

    return False


if __name__ == '__main__':
    print(checkStringPermutation('ab', 'an'))
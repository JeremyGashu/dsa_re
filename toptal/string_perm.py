def getMappings(a: str):
    counter = {}
    for i in a:
        counter.setdefault(i, 0)
        counter[i] += 1

    return counter


def checkStringPermutation(a: str, b: str) -> bool:
    if len(a) > len(b):
        return False
    l, r = 0, len(a) - 1
    while r < len(b):
        if getMappings(b[l:r + 1]) == getMappings(a):
            return True
        l += 1
        r += 1

    return False


def checkPermutationFaster(a: str, b: str):
    counter = getMappings(a)
    l, r = 0, len(a) - 1
    temp_counter = {}
    while r < len(b):
        if(r < len(a)):
            temp_counter.setdefault(b[r], 0)
            temp_counter[b[r]] += 1
        else:
            pass

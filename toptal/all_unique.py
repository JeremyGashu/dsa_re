def isAllUnique(word: str) -> bool:
    counter = {}
    for i in word:
        counter.setdefault(i, 0)
        counter[i] += 1
        if(counter[i] > 1):
            return False
    return True


if __name__ == '__main__':
    print(isAllUnique('Ermiass'))
    print(isAllUnique('Ermias'))

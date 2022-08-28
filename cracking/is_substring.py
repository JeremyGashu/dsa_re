def isSubstring(str1: str, str2: str) -> bool:
    if len(str1) < len(str2):
        return False

    for i in range(len(str1) - len(str2) + 1):
        if i + len(str2) <= len(str1):
            if(str1[i: i + len(str2)] == str2):
                return True

    return False


if __name__ == '__main__':
    print(isSubstring('examplestring', 'example'))

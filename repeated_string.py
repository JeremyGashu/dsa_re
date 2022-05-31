def repeated(s : str):
    counter = {}
    max_count = 0
    max_letter = ''
    for i in range(len(s)):
        counter.setdefault(s[i], 0)
        counter[s[i]] += 1
        if max_count < counter[s[i]]:
            max_count = counter[s[i]]
            max_letter = s[i]
    return max_letter
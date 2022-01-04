def numDistinct( s: str, t: str) -> int:
        count = 0
        for i in t:
            print(i)
            for j in s:
                print(j)
                # elementIndex = 0
                # if(i in s[elementIndex::]):
                #     elementIndex = s.indexOf(i)
                # else:
                #     break
                # count += 1
        return count

print(numDistinct('rabbbit', 'rabbit'))


from collections import Counter


class Solution:
    def palPerm(self, s1: str) -> bool:
        s1 = s1.replace(" ", "")
        s1 = s1.lower()
        counter = Counter(s1)
        hasOdd = False
        for i in counter:
            if counter[i] % 2 != 0 and hasOdd:
                return False
            if counter[i] % 2 != 0 and not hasOdd:
                hasOdd = True
        return True


if __name__ == '__main__':
    solution = Solution()
    assert (solution.palPerm("Tact Coa"))



from collections import Counter


class Solution:
    def oneEditAway(self, s1: str, s2: str) -> bool:
        s1_ctr = Counter(s1)
        s2_ctr = Counter(s2)
        # Todo: do the implementation
        pass


if __name__ == '__main__':
    solution = Solution()
    # assert (solution.oneEditAway("pale", "ple"))
    solution.oneEditAway("pale", "bake")

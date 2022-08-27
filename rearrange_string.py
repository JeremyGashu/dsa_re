from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str):
        count = Counter(s)

        # negate count as it will pop the minumum value first as heap queue
        maxHeap = [[-cnt, val] for val, cnt in count.items()]
        heapq.heapify(maxHeap)
        result = ''
        prev = None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ''

            cnt, char = heapq.heappop(maxHeap)
            result += char
            cnt += 1

            # Check if their is a previous value to make it available for the next selection
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # Check if count is < 0 to place prev value from being selected in the heap
            if cnt != 0:
                prev = [cnt, char]
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.reorganizeString('aaababbbbvb'))

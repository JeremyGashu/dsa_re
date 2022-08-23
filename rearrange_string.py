from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str):
        count = Counter(s)
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

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]
        return result

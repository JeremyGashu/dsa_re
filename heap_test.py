import heapq


nums = [1, 5, 3, 5, 8, 6, 4, 3, 6, 7]

heapq.heapify(nums)
print(heapq.nlargest(3, nums))

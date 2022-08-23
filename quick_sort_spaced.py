from typing import List


def quick_sort(nums : List) -> List:
    if len(nums) <= 1:
        return nums
    
    else:
        pivot = nums.pop()
        left = []
        right = []
        for i in nums:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([1,4,6,4,3,1,4,6,8,6,5,4,3,67,888,6]))
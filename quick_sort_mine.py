from typing import List


def quick_sort(nums: List):
    quick_sort2(nums, 0, len(nums) - 1)


def quick_sort2(nums: List, low: int, hi: int):
    if low < hi:
        p = partition(nums, low, hi)
        quick_sort2(nums, low, p - 1)
        quick_sort2(nums, p + 1, hi)


def get_pivot(nums, low, hi):
    mid = (hi + low) // 2
    s = sorted([nums[low], nums[mid], nums[hi]])
    if s[1] == nums[low]:
        return low
    elif s[1] == nums[mid]:
        return mid
    return hi


def partition(nums : List, low : int, hi : int):
    pivotIndex = get_pivot(nums, low, hi)
    pivotValue = nums[pivotIndex]
    
    nums[low], nums[pivotIndex] = nums[pivotIndex], nums[low]
    border = low

    for i in range(low, hi + 1):
        if nums[i] < pivotValue:
            border += 1
            nums[border], nums[i] = nums[i], nums[border]

    nums[border], nums[low] = nums[low], nums[border]
    return border

from typing import List


def bubblrSort(nums : List) -> List:
    if len(nums) <= 1:
        return nums
    
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums
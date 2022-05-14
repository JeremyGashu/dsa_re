from turtle import left
from typing import List


def merge(l1: List, l2: List) -> List:
    i, j = 0, 0
    sorted_list = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            sorted_list.append(l1[i])
            i += 1
        else:
            sorted_list.append(l2[j])
            j += 1

    while i < len(l1):
        sorted_list.append(l1[i])
        i += 1
    while j < len(l2):
        sorted_list.append(l2[j])
        j += 1

    return sorted_list


def merge_sort(nums: List):
    if len(nums) < 2:
        return nums[:]

    else:
        mid = len(nums) // 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])
        return merge(left, right)


print(merge_sort([1, 2, 6, 2, 8, 3, 1, 6, 8, 5, 3]))

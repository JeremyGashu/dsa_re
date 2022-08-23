from turtle import left, right
from typing import List
from unittest import result


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


# print(merge_sort([1, 2, 6, 2, 8, 3, 1, 6, 8, 5, 3]))

def mergeMine(l1: List, l2: List) -> List:
    i1 = 0
    i2 = 0
    result = []
    while(i1 < len(l1) and (i2 < len(l2))):
        if(l1[i1] > l2[i2]):
            result.append(l2[i2])
            i2 += 1
        else:
            result.append(l1[i1])
            i1 += 1

    while i1 < len(l1):
        result.append(l1[i1])
        i1 += 1

    while i2 < len(l2):
        result.append(l2[i2])
        i2 += 1

    return result


def mergeSortMine(nums: List) -> List:
    if(len(nums) < 2):
        return nums
    else:
        mid = len(nums) // 2
        left = mergeSortMine(nums[:mid])
        right = mergeSortMine(nums[mid:])
        return mergeMine(left, right)


if __name__ == '__main__':
    print(mergeSortMine([1, 4, 56, 3, 1, 4, 6, 7]))

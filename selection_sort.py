from typing import List

from urllib3 import Retry


def selectionSort(L):
    for i in range(len(L)):
        min_idx = i
        for j in range(i+1, len(L)):
            if L[min_idx] > L[j]:
                min_idx = j
        L[min_idx], L[i] = L[i], L[min_idx]

    return L


def selectionMine(nums: List) -> List:    
    if(len(nums) <= 1):
        return nums
    for i in range(len(nums) - 1):
        current = nums[i]
        for j in range(i + 1, len(nums)):
            if(nums[j] < current):
                current = nums[j]
                nums[i], nums[j] = nums[j], nums[i]
    return nums


if __name__ == '__main__':
    print(selectionMine(
        [1, 2, 45, 21, 44, 67, 32, 77, 99, 2222, 56666, 34, 21]))

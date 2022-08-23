from typing import List


def insertion(nums : List) -> List:
    if len(nums) <= 1:
        return nums

    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


def insertionAgain(nums : List) -> List:
    if(len(nums) <= 1):
        return nums
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if(nums[i] > nums[j]):
                nums[i], nums[j] = nums[j], nums[i]

    return nums


if __name__ == '__main__':
    print(insertionAgain([1,67,3,3,2,7]))
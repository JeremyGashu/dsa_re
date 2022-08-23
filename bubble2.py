from typing import List


def bubblrSort(nums : List) -> List:
    if len(nums) <= 1:
        return nums
    
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

def bubbleMine(nums : List) -> List:
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums



if __name__ == '__main__':
    print(bubbleMine([1,6,4,23,7,5,3,7,8]))
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


if __name__ == '__main__':
    # print()
    pass
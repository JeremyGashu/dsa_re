var search = function (nums, target) {
    if (nums.length === 1 && nums[0] !== target) return -1

    let left = 0
    let right = nums.length - 1
    let mid = Math.floor((left + right) / 2)

    while (right >= left) {
        console.log(right, left)
        mid = Math.floor((left + right) / 2)
        if (target > nums[mid]) {
            left = mid + 1
        }
        else if (target < nums[mid]) {
            right = mid - 1
            
        }
        else if (target === nums[mid]) {
            return mid
        }
    }
    return -1
}

console.log(search([-1, 0, 3, 5, 9, 12], 5))
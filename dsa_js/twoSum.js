const twoSum = (arr, target) => {
    let comp = {}
    for (let i = 0; i < arr.length; i++) {
        if (comp[arr[i]] >= 0) {
            return [comp[arr[i]], i]
        }
        comp[target - arr[i]] = i
    }

    return []
}

const reverseNumber = (num) => {
    let isNegative = num < 0
    num = isNegative ? num * -1 : num
    final = 0
    counter = 0
    while (num > 0) {
        let remainder = num % 10
        num = Math.floor(num / 10)
        final = final * 10 + remainder
    }
    return isNegative ? final * -1 : final
}

const isPallindromeNumber = (num) => {
    return reverseNumber(num) === num
}

const smallestMissingInteger = (arr) => {
    let vals = {}
    if (arr.length <= 0) return null
    let min = arr[0]
    for (let num of arr) {
        vals[num] = true
        if (vals[num] < min && vals[num] > 0) min = vals[num]
    }

    for (let num of arr) {
        if (vals[num] > 0 && vals[num] > min && !vals[num + 1]) return num + 1
    }
    let a = {}

    return vals

}

var deleteDuplicates = (head) => {
    
}



const a = [3, 4, -1, 1]
console.log(smallestMissingInteger(a))
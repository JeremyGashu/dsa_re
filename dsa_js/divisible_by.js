/*
@param number => The number to check
@param tupleLength => length of the tuple to group numbers
@param primeFactor => the factor 
*/
const checkDivisibilityOfPrimeByRTuple = (number, tupleLength, primeFactor) => {
    let temp = 0
    let sum = 0
    let accumilator = []
    let counter = 0
    let remainder = 0

    if (number <= primeFactor) {
        return number % primeFactor === 0
    }
    while (number > 0) {
        if (counter < tupleLength) {
            remainder = number % 10
            number = Math.floor(number / 10)

            if (counter === 0) {
                temp = remainder
            }
            else {
                temp = (10 * remainder) + temp
            }
            counter++
        }
        else {
            accumilator.push(temp)
            temp = 0
            counter = 0
        }
    }
    if (temp !== 0) accumilator.push(temp)
    sum = accumilator.reduce((prev, current) => prev + current)
    return sum % primeFactor === 0
}

const getTupleLength = (num, factor) => {

    if(num === 5 || num === 2) return -1

    for (let i = 1; i <= num.toString().length; i++) {
        let valid = checkDivisibilityOfPrimeByRTuple(num, i, factor)
        if (valid) {
            return i
        }
    }
    return -1
}
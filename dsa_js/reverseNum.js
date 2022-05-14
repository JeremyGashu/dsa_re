var reverse = function(x) {
    let isNegative = x > 0 ? false : true
    x = isNegative ? -1 * x : x
    let reversed = 1
    while(x>0){
        reversed = (reversed * 10) + (x % 10)
        x = Math.floor(x / 10)
    }
    return isNegative ? -1 * reversed : reversed
};

console.log(reverse(1234))
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var addTwoNumbers = function (l1, l2) {
    let num1 = ''
    let num2 = ''
    while (l1) {
        num1 = num1 + l1.val.toString()
        l1 = l1.next
    }

    while (l2) {
        num2 = num2 + l2.val.toString()
        l2 = l2.next
    }
    num1 = + num1
    num2 = +num2

    return reverseNumber(reverseNumber(num1) + reverseNumber(num2))
};

const reverseNumber = (num) => {
    let value = 0

    while (num > 0) {
        value = (value * 10) + (num % 10)
        num = Math.floor(num / 10)
    }
    return value
}

let node1 = new ListNode(2, new ListNode(4, new ListNode(3, null)))
let node2 = new ListNode(5, new ListNode(6, new ListNode(4, null)))

console.log(addTwoNumbers(node1, node2))

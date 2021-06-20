// 1
function printUpto(x) { // your code here
    if (x < 0) {
        return "false";

    }
    for (var i = 0; i <= x; i++) {
        console.log(i);
    }
}
printUpto(10); //should print all the intergers from 1 to 1000000
var y = printUpto(-10); // shourld return false
console.log(y); // should print false
console.log('----------------');
// 2
function printSum(x) {
    var sum = 0;
    for (var i = 0; i <= x; i++) {
        sum = sum + i;
        console.log('num is ' + i + ' total so far:' + sum); //your code here
    }
    return sum

}
var y = printSum(255) // should print all the integers from 0 to 255 and with each integer print the sum so far.
console.log(y) // should print 32640
console.log('----------------');
//3
function printSumArray(x) {
    var sum = 0;
    for (var i = 0; i < x.length; i++) {
        sum = sum + x[i]; //your code here
    }
    return sum;
}
console.log(printSumArray([1, 2, 3])); // should log 6
console.log('----------------');

function largestnum(x) {

    return Math.max.apply(Math, x);
}
console.log(largestnum([1, 30, 6, 8, 17, 20]));
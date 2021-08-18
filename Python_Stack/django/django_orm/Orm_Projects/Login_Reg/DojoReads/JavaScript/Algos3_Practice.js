// p1 return the average of an array
function printAverage(x) {
    var sum = 0;
    for (var i = 0; i < x.length; i++) {
        sum = sum + x[i];
    }
    return sum / x.length;    // your code here
}
var y = printAverage([1, 2, 3]);
console.log(y); // should log 2

y = printAverage([5, 2, 8]);
console.log(y); // should log 5

console.log('-----');
// P2 create an array of odd numbers up to 255
var narr = [];
function returnOddArray() {
    for (var i = 1; i <= 255; i++) {
        if (i % 2 != 0) {
            narr.push(i);
        }
    }
    return narr;
}
var y = returnOddArray();
console.log(y); // should log [1,3,5,...,253,255]
console.log('-----');
// 3 Square each value of giver array and return that array of squares

function squareValue(x) {
    for(var i = 0; i<x.length; i++){
       x[i] = x[i] **2;
    }// your code here
    return x;

}
var y = squareValue([1, 2, 3]);
console.log(y); // should log [1,4,9]

y = squareValue([2, 5, 8]);
console.log(y); // should log [4,25,64]
console.log('-----');


// 1
function counter() {
    for (var i = 1; i <= 255; i++) {
        console.log(i);
    }
}
counter();
console.log('-----------------');
// 2
function even() {
    for (var i = 1; i <= 1000; i++) {
        if (i % 2 != 0) {
            console.log(i);
        }
    }
}
even();
console.log('-----------------');
// 3
var sum = 0;

function totalOdd() {
    for (var i = 1; i <= 5000; i++) {
        if (i % 2 != 0) {
            sum = sum + i;
        }
    }
    console.log(sum);
}
totalOdd();
console.log('-----------------');
// 4
var arr = [1, 2, 3, 4, 5];
var sum = 0;

function arrTot() {
    for (var i = 0; i < arr.length; i++) {
        sum = sum + arr[i];
    }
    console.log(sum)
}
arrTot();
console.log('-----------------');
// 5
var n = 0;
var arr1 = [-3, 3, 5, 7];

function HighNum() {
    n = Math.max.apply(Math, arr1);
    console.log(n);
}
HighNum();
console.log('-----------------');
// 6
var arr2 = [1, 3, 5, 7, 20];
var x = 0;
var sum = 0;

function avg() {
    for (var i = 0; i < arr2.length; i++) {
        sum = sum + arr2[i];
    }
    x = sum / arr2.length;
    console.log(x);
}
avg();
console.log('-----------------');
// 7
var odd = [];

function arr3() {
    for (var i = 1; i < 50; i++) {
        if (i % 2 != 0) {
            odd.push(i);
        }
    }
    console.log(odd);
}
arr3();
console.log('-----------------');
// 8
var y = 3;
var z = 0;
var c = 0;
var newarr = [];
// not working
function greaterthan() {
    for (var i = 0; i < arr2.length; i++) {
        if (y < arr2[i])
            c = arr2[i];
        z = z + 1;
        newarr.push(c);
    }
    console.log('There are ' + z + ' values greather than ' + y + ' and they are ' + newarr);

}
greaterthan();
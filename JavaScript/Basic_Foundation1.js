// 1 Get 1 to 255
function counter() {
    for (var i = 1; i <= 255; i++) {
        console.log(i);
    }
}
counter();
console.log('-----------------');
// 2 Get even numbers to 1000
function even() {
    for (var i = 1; i <= 1000; i++) {
        if (i % 2 != 0) {
            console.log(i);
        }
    }
}
even();
console.log('-----------------');
// 3 Sum of odd to 5000
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
// 4 Iterate an array
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
// 5 Find Max
var n = 0;
var arr1 = [-3, 3, 5, 7];

function HighNum() {
    n = Math.max.apply(Math, arr1);
    console.log(n);
}
HighNum();
console.log('-----------------');
// 6 Find Average
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
// 7 Arrayodd
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
// 8 Greater than y
var y = 3;
var z = 0;
var newarr = [];

function greaterthan() {
    for (var i = 0; i < arr2.length; i++) {
        if (y < arr2[i])
            newarr.push(arr2[i]);
        z = z + 1;
    }
    console.log('There are ' + z + ' values greather than ' + y + ' and they are ' + newarr);
}
greaterthan();
console.log('-----------------');
// 9 Squares
var newarr1 = [];

function squares() {
    for (var i = 0; i < arr2.length; i++) {
        newarr1[i] = arr2[i] ** 2;
    }
    console.log('Array:', arr2)
    console.log('Array squared')
    console.log(newarr1);
}
squares();
console.log('-----------------');
// 10 Negatives
var arr1 = [-3, 3, 5, 7];

function negArr() {
    for (var i = 0; i < arr1.length; i++) {
        if (arr1[i] < 0) {
            arr1[i] = 0
        }
    }
    console.log(arr1);
}
negArr();
console.log('-----------------');
// 11 Max/Min/Avg
var newarr2 = [];
var arr2 = [1,5,10,-2];
var x = 0;
var sum = 0;
var n = 0;
var z = 0;
function maxMinavg (){
    for(var i = 0; i<arr2.length; i++){
        sum = sum + arr2[i];
        n = Math.max.apply(Math, arr2);
        z = Math.min.apply(Math, arr2);
    }
    x = sum / arr2.length;
    newarr2.push(n,z,x);
    console.log(newarr2);
}
maxMinavg();
console.log('-----------------');
// 12 Swap Values
var b = 0;
var arr2 = [1,5,10,-2];

function swap(){
    b = arr2[0];
    arr2[0] = arr2[arr2.length - 1];
    arr2[arr2.length -1] = b;
    console.log(arr2)
}
swap();
console.log('-----------------');
// 13 numbers to String
var b = 0;
var arr4 = [1,-5,10,-2];

function dojo(){
    for(var i = 0; i<arr4.length; i++){
        if(arr4[i] < 0){
            arr4[i] = "Dojo";
        }
        
        console.log(arr4)
    }
}
dojo();
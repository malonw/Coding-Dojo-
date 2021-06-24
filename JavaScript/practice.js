for (var i = 0; i < 5; i++) {
    console.log(i);
}
// output 0,1,2,3,4
console.log('---');
for (var i = 0; i < 5; i++) {
    i = i + 1;
    console.log(i);
}
// output 1,3,5
console.log('---');
for (var i = 0; i < 5; i++) {
    i = i + 3;
    console.log(i);
}
// 3,7
console.log('---');
function y(num1, num2) {
    return num1 + num2;
}
console.log(y(2, 3));
console.log(y(3, 5));
// 5,8
console.log('---');
function y(num1, num2) {
    console.log(num1);
    return num1 + num2;
}
console.log(y(2, 3));
console.log(y(3, 5));
// 2,5,3.8
console.log('---');
a = 15;
console.log(a);
function y(a) {
    console.log(a);
    return a;
}
b = y(10);
console.log(b);
// 15,10,10
console.log('---');
a = 15;
console.log(a);
function y(a) {
    console.log(a);
    return a * 2;
}
b = y(10);
console.log(b);
// 15,10,20
console.log('---');

// Predict the output Part 2
function c() {
    console.log('hello');
}
console.log('Dojo');
// Dojo
console.log('---');

function d() {
    console.log('hello');
    return 15;
}
x = d();
console.log('x is', x);
// hello, x is 15
console.log('---');
function f(n) {
    console.log('n is', n);
    return n + 15;
}
z = f(3);
console.log('x is', z);
// n is 3, x is 18
console.log('---');
function ab(n) {
    console.log('n is', n);
    y = n * 2;
    return y;
}
x = ab(3) + ab(5);
console.log('x is', x);
// n is 3,n is 5, x is 16

console.log('---');
function op(a, b) {
    c = a + b;
    console.log('c is', c);
    return c;
}
x = op(2, 3) + op(3, 5);
console.log('x is', x);
// c is 5, c is 8, x is 13
console.log('---');
function op(a, b) {
    c = a + b;
    console.log('c is', c);
    return c;
}
x = op(2, 3) + op(3, op(2, 1)) + op(op(2, 1), op(2, 3));
console.log('x is', x)
// c is 5, c is 3, c is 6,c is3, c is 5, c is 8, x is 19
console.log('---');
var x = 15;
function m() {
    var x = 10;
}
console.log(x);
m();
console.log(x);
// 15, 15
console.log('---');
function multiply(x, y) {
    return x * y;
}
var b = multiply(2, 3);
console.log(b);
console.log(multiply(5, 2));
// 6, 10
console.log('---');
var x = [1, 2, 3, 4, 5, 10];
for (var i = 0; i < 5; i++) {
    i = i + 3;
    console.log(i);
}
// 3, 7
console.log('---');
var x = 15;
console.log(x);
function foo() {
    var x = 10;
    console.log(x);
}
console.log(x);
foo();
console.log(x);
// 15,15,10,15
console.log('---');
for (var i = 0; i < 15; i += 2) {
    console.log(i);
}
// 0,2,4,6,8,10,12,14
console.log('---');
for (var i = 0; i < 3; i++) {
    for (var j = 0; j < 2; j++) {
console.log(i*j);
    }  
}
// 0,0,0,1,0,2 
console.log('-----');
function foo(x, y) {
    for (var i = 0; i < x; i++) {
        for (var j = 0; j < x; j++) {
            console.log(i*j);
        } 
    }
}
var z= foo(3,3 );
console.log(z);
console.log('-----');
function fool(x,y){
    for(var i=0;i<x; i++){
        for(var j=0;j<y; j++){
            console.log(i*j);
        }
    }
    return x*y;
}
var zx = fool(3,5);
console.log(zx);
// 1
for(var i = 1; i <=20; i++){
    if(i % 2 != 0){
        console.log(i)
    }
}
// output 1,3,5,7,9,11,13,15,17,19
console.log('----');
// 2
var sum=0;
for(var i = 0; i <=5; i++){
    console.log('num =',i);
    sum=sum+i;
    console.log('sum =',sum);
}
// num=0, sum=0, num=1 ,sum=1, num=2, sum=3, num=3, sum=6 num=4, sum=10 ,num=5 ,sum=15 
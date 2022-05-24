function fibonacci(n){

    if(n <= 0){
        return 0;
    }

    if(n == 1){
        return 1;
    }
    else{
        console.log(`calculating fibonacci ${n}`)
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
// console.log(fibonacci(5));
// console.log(fibonacci(6));
// console.log(fibonacci(7));
console.log(fibonacci(5));
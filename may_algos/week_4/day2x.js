// memoization

function fibonacci(n, memo = {}){
    // default parameter

    if(n <= 0){
        return 0;
    }

    if(n == 1){
        return 1;
    }
    else{
        if (memo[n] != undefined) {
            console.log(`accessed fibonacci ${n} from storage`)
            return memo[n];
        }
        else {
            x = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
            console.log(`calculated fibonacci ${n} and stored it`)
            memo[n] = x;
            return x;
        }
    }
}

// console.log(fibonacci(5));
// console.log(fibonacci(6));
console.log(fibonacci(5));
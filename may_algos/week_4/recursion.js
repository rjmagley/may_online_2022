// recursion

// non-recursive function
// sigma(n)
// returns sum of numbers from 1 to n
// 3 -> 3 + 2 + 1 = 6
// 4 -> 10
// 5 -> 15

function sigma(n) {
    var sum = 0;
    var i = 0;
    while (i <= n) {
        sum += i;
        i++;
    }
    return sum;
}

console.log(sigma(100000));

// recursive version

function sigmaRecursive(n) {

    // console.log(`called sigmaRecursive with a argument of ${n}`)
    // establish a base case
    // base cases stop recursion
    if (n <= 0) {
        // console.log("base case reached")
        return 0;
    }
    // otherwise, perform recursive call
    else {
        var x = sigmaRecursive(n - 1);
        // console.log(`completed function call to sigmaRecursive with argument of ${n} and returning value`);
        return n + x;
    }
}

console.log(sigmaRecursive(100000));

function failingSigmaRecursive(n) {
    return n + failingSigmaRecursive(n - 1);
}

// console.log(failingSigmaRecursive(6));
function swapPairs(arr) {

    if (arr.length < 2) {
        return arr;
    }

    for (var i = 0; i < arr.length; i += 2) {
        if (i + 1 < arr.length) {
            var temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }

    return arr;
}

function swapPairs(arr) {
    for (let i = 1; i < arr.length; i += 2) {
        let temp = arr[i - 1];
        arr[i - 1] = arr[i];
        arr[i] = temp;
    }
    return arr;
}

console.log(swapPairs([1, 2, 3, 4, 5, 6])) // [2, 1, 4, 3, 6, 5]
console.log(swapPairs([1, 2, 3, 4, 5])) // [2, 1, 4, 3, 5]
console.log(swapPairs([9, 1, 6, 3, 0, 12, 9, 4, 5])) // [1, 9, 3, 6, 12, 0, 4, 9, 5]
console.log(swapPairs(["apple", "pear", "avocado", "banana"])) // ["pear", "apple", "banana", "avocado"]
console.log(swapPairs([0,0, 0,0])) // [0, 0, 0, 0]
console.log(swapPairs([])) // 
console.log(swapPairs([true])) // [true]
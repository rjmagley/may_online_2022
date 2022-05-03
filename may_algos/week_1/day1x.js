function rotateArray(arr, shiftBy) {
    // modify arr instead of creating a new array

    for (var j = 0; j < shiftBy; j++) {
        var lastItem = arr[arr.length - 1]
        for (var i = arr.length - 1; i > 0; i--) {
            arr[i] = arr[i - 1];
            // console.log(arr);
        }
        arr[0] = lastItem;
    }
    return arr;
}

// var result = rotateArray([1, 2, 3, 4, 5], 1);
// console.log(result);

// var result = rotateArray([1, 2, 3, 4, 5], 2);
// console.log(result);

var result = rotateArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 13);
console.log(result);
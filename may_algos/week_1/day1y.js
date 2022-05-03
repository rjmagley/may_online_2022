function rotateArray(arr, shiftBy) {
    let newArr = [];
    if (shiftBy > arr.length) {
        shiftBy = // some modification
    }
    for(var i=0; i<arr.length; i++) {
        newArr.push(arr[((arr.length + i - shiftBy)%arr.length)]);
    }
    arr.length = 0;
    arr = [... newArr];
    return arr;
}

var result = rotateArray([1, 2, 3, 4, 5], 1);
console.log(result);

var result = rotateArray([1, 2, 3, 4, 5], 2);
console.log(result);

var result = rotateArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 13);
console.log(result);

var result = rotateArray([1, 2, 3, 4, 5], -2);
console.log(result);

var result = rotateArray([1, 2, 3, 4, 5], 16);
console.log(result);
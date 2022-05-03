function sampleFunctionName(arr){
    let output = [];

    // for (var i = 0; i < arr.length; i++) {
    //     if (arr[i] >= 0) {
    //         output.push(arr[i])
    //     }
    // }

    for (const number of arr) {
        if (number >= 0) {
            output.push(number);
        }
    }

    return output;
}

console.log(sampleFunctionName([1, -3, 9, -2, 7]))
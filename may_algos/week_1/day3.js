function bubbleSort(arr) {
    // var temp;
    for (var i = 0; i < arr.length; i++) {
        for (var j = 0; j < arr.length - i; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
}

var x = [1, 6, 8, 9, 23, 3, 6, 9];
console.log(`Before sort: ${x}`);
bubbleSort(x);
console.log(`After sort: ${x}`);
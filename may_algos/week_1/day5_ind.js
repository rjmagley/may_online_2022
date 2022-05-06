// [1, 1, 1, 1, 2, 2, 3, 5, 5, 5, 7]

// [1, 2, 3, 5, 7]

// this works, but the splice operation can be expensive
function deduplicateSortedArray(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] == arr[i + 1]) {
            arr.splice(i, 1)
            i--
        }
    }
    return arr
}

// this gets the desired result, but isn't doing it in place
// arr = new_arr doesn't actually modify the array referenced by arr
function deduplicateSortedArray(arr) {
    var new_arr = [];
    //loop through each element in the array 
    for (var i = 0; i < arr.length; i++) {
        //if the element is not equal to the right neighbor, add it to the temp array
        if (arr[i] != arr[i + 1]) {
            new_arr.push(arr[i]);
        }
    }
    arr = new_arr
    // Write your solution here!
    return arr
}

// this is as above, but kind of cheats to do it 'in place'
// in that it just changes the *contents* of the array
function deduplicateSortedArray(arr) {
    let tempArray = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] != arr[i + 1]) {
            tempArray.push(arr[i]);
        }
    }
    arr.length = 0;
    for (let x of tempArray) {
        arr.push(x);
    }
}

// this is the most optimal, but hardest to understand
// basically, shifts all non-duplicates to the front, then chops off the remainder
function deduplicateSortedArray(arr) {
    var dupes = 0;
    var temp;
    for(var i=0; i<arr.length; i++) {
        console.log(arr);
      if(arr[i] === temp) {
        dupes++;
      } else {
        arr[i-dupes] = arr[i];
      }
      temp = arr[i];
    }
    arr.length -= dupes;
    return arr;
}

// this very slowly shifts items to the front, one by one, then shrinks the array
// it is not at all efficient, but maybe understandable
// (although many people immediately see that it can be improved)
function deduplicateSortedArray(arr) {
    for (let i = 0; i < arr.length; i++) {
        let shiftCount = 0;
        let x = i;
        while (arr[x] == arr[x + 1] && arr[x + 1] != undefined) {
            shiftCount += 1;
            x += 1;
        }
        console.log(shiftCount);
        if (shiftCount != 0) {
            for (let j = i; j < arr.length; j++) {
                arr[j] = arr[j + shiftCount];
            }
            arr.length -= shiftCount;
        }
        console.log(arr);
    }
}

// let x = [0, 0, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6];
// deduplicateSortedArray(x);
// console.log(x);

let y = [8, 8, 11, 11, 11, 11, 11, '11', 23, 23, 34, '87', 87, 87, 1919, 1919, 200021];
deduplicateSortedArray(y);
console.log(y);
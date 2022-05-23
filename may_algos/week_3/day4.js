function bookIndex(pages) {
    var strArray = [];

    for (var i = 0; i < pages.length; i++) {
        var left = pages[i];
        var right = pages[i];

        while (pages[i] + 1 == pages[i+1]) {
            i++;
            right = pages[i];
            // console.log(`${left} and ${right}`)
        }

        if (left == right) {
            strArray.push(left.toString());
        }
        else {
            strArray.push(`${left}-${right}`);
            // in Python: strList.append(f"{left} - {right})
        }
    }

    return buildIndexString(strArray);
}

function buildIndexString(arr) {
    var output = '';
    for (i in arr) {
        output += arr[i];
        if (i != arr.length - 1) {
            output += ', ';
        }
    }
    return output;
}

console.log(bookIndex([1, 2, 3, 6, 7, 9, 11, 12, 13, 17])) // should return "1-3, 6-7, 9, 11-13, 17"
console.log(bookIndex([223, 224, 225, 226, 227, 231, 232, 233])) // should return "223-227, 231-233"
console.log(bookIndex([5, 8, 11, 21, 172])) // should return "5, 8, 11, 21, 172"
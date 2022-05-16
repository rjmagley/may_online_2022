export function interleaveArrays(arrayA, arrayB) {
  
    var newArray = [];
  
    if (arrayA.length > arrayB.length) {
      var longerArray = arrayA;
    }
    else {
      var longerArray = arrayB;
    }
  
    for (var i = 0; i < longerArray.length; i++) {
      if(i < arrayA.length) {
        newArray.push(arrayA[i]);
      }
      if(i < arrayB.length) {
        newArray.push(arrayB[i]);
      }
  
    }
  
    return newArray;
  }
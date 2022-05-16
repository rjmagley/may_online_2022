export function interleaveArrays(arrayA, arrayB) {
  
    var newArray = [];
  
    if (arrayA.length > arrayB.length) {
      var longerArray = arrayA;
    }
    else if (arrayA.length < arrayB.length) {
      var longerArray = arrayB;
    }
    else {
      var longerArray = arrayA;
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
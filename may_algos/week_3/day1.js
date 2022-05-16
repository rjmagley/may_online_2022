export function interleaveArrays(arrayA, arrayB) {
  
    var newArray = [];

    for (var i = 0; i < arrayA.length || i < arrayB.length; i++) {
      if(i < arrayA.length) {
        newArray.push(arrayA[i]);
      }
      if(i < arrayB.length) {
        newArray.push(arrayB[i]);
      }
  
    }
  
    return newArray;
  }
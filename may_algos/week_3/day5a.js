function findMissingValue(input) {
  
    if (input.length <= 1) {
      return undefined;
    }
  
    var minimumItem = input[0];
    var maximumItem = input[0];
    var sumOfItems = 0;
  
    for (var i = 0; i < input.length; i++) { // i <= input.length - 1
  
      sumOfItems += input[i];
  
      if (input[i] < minimumItem) {
        minimumItem = input[i];
      }
  
      else if (input[i] > maximumItem) {
        maximumItem = input[i];
      }
    }
  
    var expectedSum = 0;
    for (var i = minimumItem; i <= maximumItem; i++) {
      expectedSum += i;
    }
  
    return expectedSum - sumOfItems;
  }
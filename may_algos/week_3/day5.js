// find missing element in array

// O(n) - no nested for loops, no sorting
// another for loop is okay, just not nested
// items may be sequential but this is not guaranteed
// list is n items long but is missing one - length *should* be n+1
// no duplicates

// min and max items are determinable
// integers are comparable

// series of integers can be summed up
// we can determine the expected sum based on the minimum and maximum values
// actual, observed of input can differ based on which integer is missing

function findMissingValue(input) {

    var lowest = input[0];
    var highest = input[0];
    var sum1 = 0;
  
    for (var i = 0; i < input.length; i++){
      if (input[i] < lowest){
        lowest = input[i];
      } else if (input[i] > highest){
        highest = input[i];
      }
      sum1 += input[i]
    }
  
  
    var sum2 = 0;
    for (var k = lowest; k <= highest; k++){
      sum2 += k;
    }
  
    return sum2 - sum1;
  
  }
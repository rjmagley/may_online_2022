function missingValueSeenTable(unorderedNums) {
    if (unorderedNums.length < 1) {
      return null;
    }
  
    const seen = {};
    let min = unorderedNums[0];
    let max = unorderedNums[0];
  
    for (let i = 0; i < unorderedNums.length; i++) {
      if (!seen[unorderedNums[i]]) {
        seen[unorderedNums[i]] = true;
      }
      if (unorderedNums[i] < min) {
        min = unorderedNums[i];
      }
      if (unorderedNums[i] > max) {
        max = unorderedNums[i];
      }
    }
  
    let val = min + 1;
  
    while (val < max) {
      if (!seen[val]) {
        return val;
      }
      val += 1;
    }
    return null;
  }
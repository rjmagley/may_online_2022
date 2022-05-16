function isAnagram(string_a, string_b) {
    string_a = string_a.replace(/[^\w]/g, '').toLowerCase()
    string_b = string_b.replace(/[^\w]/g, '').toLowerCase()
    var dictA = {};
    var dictB = {};
    for(var i=0; i<string_a.length; i++){
      if(dictA[string_a[i]] == {}){
        dictA[i] = dictA['i'][0];
      }
      else{
        dictA['i']++;
      }
    for(var j=0; j<string_b.length; j++){
      if(dictB['j'] == {}){
        dictB['j'] = dictB['j'][0];
      }
      else{
        dictB['j']++;
      }
    } 

    }
    if(tempA != tempB){
      return false;
    }
    else{
      return true;
    }
  }

console.log(isAnagram("William Shakespeare", "I am a weakish speller"))
   
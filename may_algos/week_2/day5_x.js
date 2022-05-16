function isAnagram(string_a, string_b) {

    var str1 = string_a.toUpperCase();
    str1 = str1.split('');
    str1.sort()
    str1 = str1.join('')

    var str2 = string_b.toUpperCase();
    str2 = str2.split('');
    str2.sort()
    str2 = str2.join('')

    console.log(`String 1: ${str1}, length: ${str1.length}`)
    console.log(`String 2: ${str2}, length: ${str2.length}`)

    if (str1 === str2) {
        return true
    } else {
        return false
    }
}

console.log(isAnagram("William Shakespeare", "I am a weakish speller"))
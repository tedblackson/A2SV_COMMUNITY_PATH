/**
 * @param {string} s
 * @return {string}
 */
 var sortSentence = function(s) {
    
    let arr = s.split(' ')
    
    arr.sort( (word1, word2) => word1[word1.length - 1] - word2[word2.length - 1]);
    
    return arr.map( word => word.slice(0, word.length - 1)).join(' ')
    
};
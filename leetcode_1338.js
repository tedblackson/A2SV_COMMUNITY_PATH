/**
 * @param {number[]} arr
 * @return {number}
 */
 var minSetSize = function(arr) {
    
    let counted = new Map()
    let chosen = new Set()
    for(let x of arr){
        
        if(counted.get(x) === undefined){
            counted.set(x, 1)
        }
        else{
            counted.set(x, counted.get(x)+1)
        }
    }
    arr.sort((x,y) => y-x)
    arr.sort((x,y) => {
        
        return counted.get(y) - counted.get(x)
    })
    
    let half = arr.length/2
    chosen.add(arr.shift())
    while(arr.length > half || chosen.has(arr[0])){
        chosen.add(arr.shift())
    }
    return chosen.size
};
/**
 * @param {number[]} changed
 * @return {number[]}
 */
 var findOriginalArray = function(changed) {
    
    let original = []
    let locateMap = new Map()
    changed.sort((x, y) => x - y)

    changed.forEach((x,i) => {

        
        if(locateMap.get(x) === undefined){
            
            locateMap.set(x , 1)
        }
        
        else{
            locateMap.set(x, locateMap.get(x) + 1)
        }
    })

    let doubleLength = changed.length
    
    for(let x of changed){
        
        let double = x * 2
        
        
        
        if(x === 0 && locateMap.get(x)%2 === 0 && locateMap.get(x)!== 0 ){
            original.push(x)
            locateMap.set(x, locateMap.get(x) - 2)
            
        }
        
        else if(locateMap.has(double) && locateMap.get(double) && locateMap.get(x) && x !== 0){
            original.push(x)
            locateMap.set(double, locateMap.get(double) - 1)
            locateMap.set(x, locateMap.get(x) - 1)
            
        }
        
        
    }
    
    return original.length === doubleLength/2? original: []
    
};
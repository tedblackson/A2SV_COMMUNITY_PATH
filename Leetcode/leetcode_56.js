/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
 var merge = function(intervals) {
    
    intervals.sort((interval1, interval2) => interval1[0] - interval2[0])
    let results = intervals
    for(let j = 0; j <= 10000; j++){
        for(let i = 0; i < results.length - 1; i++){
        
            let one = results[i][0]
            let two = results[i][1]
            let three = results[i + 1][0]
            let four = results[i + 1][1]
    
            
            if(four <= two && three <= two){
                
                results = [...results.slice(0, i), [one, two], ...results.slice(i + 2, results.length)]
                
                
            }
            else if (three <= two){
                
                
                results = [...results.slice(0,i), [one, four], ...results.slice(i + 2, results.length)]
                
            }
    
    
           
        }

    }
    
    
    return results
    
};


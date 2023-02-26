/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    
        
    
        if(Number(nums.join('')) ===0){
            return '0'
        }
        
    
        nums.sort((x, y) => {
            
            let temp1 = String(x)
            let temp2 = String(y)
            console.log(temp1, temp2)
            
            

            
            if(temp1.length === temp2.length ){
                
                return (Number(temp2) - Number(temp1))
            }
            
            else{
                
                
                
                let boundary = temp2.length > temp1.length ? temp2.length : temp1.length
                
                for(let i = 0; i < boundary; i++){

                if(temp1[i] === temp2[i]){
                    continue
                }
                else if(temp1[i] === undefined && temp2[i] !== undefined){
                    
                    
                    if(temp1.slice(0, temp1.length) === temp2.slice(0, temp1.length) ){
                        let temporary1 = Number([temp1, temp2].join(""))
                        let temporary2 = Number([temp2, temp1].join(""))

                        return temporary2 - temporary1
                    
                             
                    }
            
                    
                    return  Number(temp2[i]) - Number(temp1[temp1.length - 1])
                }
                else if (temp2[i] === undefined && temp1[i] !== undefined){
                    if(temp2.slice(0, temp2.length) === temp1.slice(0, temp2.length) ){
                        let temporary1 = Number([temp1, temp2].join(""))
                        let temporary2 = Number([temp2, temp1].join(""))

                        return temporary2 - temporary1
                    
                             
                    }
                
                    return  Number(temp2[temp2.length - 1]) - Number(temp1[i])
                }
                    
                else{
                    return temp2[i] - temp1[i]
                }
                    
                    
            }
                
            }
           

           
            
           
            
            
        })
    
        
                  
        return nums.join('')

    
    
    
};
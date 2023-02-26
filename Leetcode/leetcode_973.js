/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
 var kClosest = function(points, k) {
    
    return points.sort( (point1, point2) => {
        
        let distance1 = Math.sqrt(point1[0]**2 + point1[1]**2)
        let distance2 = Math.sqrt(point2[0]**2 + point2[1]**2)
        
        return distance1 - distance2
    }).slice(0, k)
    
};
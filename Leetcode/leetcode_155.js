
var MinStack = function() {
    
    this.stack = []
    this.min = []

    return this
    
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    
    this.stack.push(val)
    
    if (val < this.min[this.min.length - 1] || this.min.length === 0){
        
        this.min.push(val)
    }
    else{
            this.min.push(this.min[this.min.length - 1])

    }
    
    
    
    
    return null
    
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    
    this.stack.pop()
    this.min.pop()
    
    return null
    
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    
   return this.stack[this.stack.length - 1]
    
    
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    
    
    return this.min[this.min.length - 1]
    
    
    
    
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
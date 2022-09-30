
var MyQueue = function() {
    this.queue = []
    this.temp = []
    
   return this
    
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    
    while(this.queue.length > 0){
        
        this.temp.push(this.queue.pop())
    }
    this.temp.push(x)
    
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    
    while(this.temp.length > 0){
        this.queue.push(this.temp.pop())
    }
    
    return this.queue.pop()
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    

    
    if(this.queue.length === 0){
        while(this.temp.length > 0){
        this.queue.push(this.temp.pop())
    }
     }
    
        return this.queue[this.queue.length - 1]

    
    
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    
    if(this.queue.length === 0  && this.temp.length === 0){
        return true
    }
    else{
        return false
    }
    
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
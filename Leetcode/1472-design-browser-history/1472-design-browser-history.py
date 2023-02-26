class ListNode:
    def __init__(self, val= 0, nextt =None, prev = None):
        self.val = val
        self.prev = prev
        self.next = nextt
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        self.cur = self.home
        
        

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(val = url, nextt = None, prev = self.cur)
        self.cur = self.cur.next
    
    
        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur and self.cur.prev:
                self.cur = self.cur.prev
            else:
                break
           
        return self.cur.val
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur and self.cur.next:
                self.cur = self.cur.next
            else:
                break
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
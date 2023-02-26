class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance
        
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        N = len(self.accounts)
        if account1 > 0 and account2 > 0 and account1 <= N and  account2 <= N and self.accounts[account1 - 1] >= money:
            self.accounts[account1 - 1]  -= money
            self.accounts[account2 - 1] += money
            return True
        return False
        
        

    def deposit(self, account: int, money: int) -> bool:
        N = len(self.accounts)
        if account > 0 and account <= N:

            self.accounts[account -1 ] += money
            return True
        return False
    
        

    def withdraw(self, account: int, money: int) -> bool:
        N = len(self.accounts)

        if account > 0 and account <= N  and self.accounts[account - 1] >= money:
            self.accounts[account - 1] -= money
            return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
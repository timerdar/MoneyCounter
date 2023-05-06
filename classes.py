class Balance:
    def __init__(self, balance_num: int) -> None:
        self.balance = balance_num
        pass
    
    def get_current_balance(self) -> int:
        return self.balance
    
    def income(self, money: int) -> None:
        self.balance += money
    
    def outgo(self, money: int) -> None:
        self.balance -= money
    
from src.models.Transactions import Transaction


class Account:
    def __init__(self, name: str, number_account: str, agency = 1000):
        self.name = name
        self.number_account = number_account
        self.agency = agency
        self.balance = 0.0
        self.transactions = []
    
    def show_account(self):
        return {
            "name": self.name,
            "number_account": self.number_account,
            "agency": self.agency,
            "balance": self.balance
        }
    
    def show_transactions(self):
        if self.transactions.__len__ == 0:
            raise FileNotFoundError("Not transactions.")
        return self.transactions

    def deposit( self, value: float):
        if value > 5000:
            raise ValueError("Value above the daily limit.")
        
        self.balance += value
        self._add_transaction(transaction_type="deposit", value= value)
            

    def withdraw(self, value: float):
        if value > self.balance:
            raise ValueError("Not enough balance.")
        
        self.balance -= value
        self._add_transaction(transaction_type= "withdraw", value= value)
    
    def _add_transaction(self, transaction_type: str, value: float):
        self.transactions.append(Transaction(transaction_type, value))
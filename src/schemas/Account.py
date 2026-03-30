from pydantic import BaseModel
    
class AccountCreate(BaseModel):
    name: str
    number_account: str

class DepositRequest(BaseModel):
    number_account: str
    value: float
    
class WithdrawRequest(BaseModel):
    number_account: str
    value: float

class GetTransactionsRequest(BaseModel):
    number_account: str
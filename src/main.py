from fastapi import FastAPI, status
from src.models.Account import Account
from src.schemas.Account import AccountCreate, DepositRequest, WithdrawRequest, GetTransactionsRequest
import asyncio

app = FastAPI()

fake_db = {}
lock = asyncio.Lock()

@app.post("/create_account/", status_code=status.HTTP_201_CREATED)
async def create_account(data: AccountCreate):
    await asyncio.sleep(0)
    
    async with lock:
        user_account = Account(
            name=data.name,
            number_account=data.number_account
        )

    fake_db[user_account.number_account] = user_account

    return {
        "message": "Account created successfully",
        "account": user_account.show_account()
    }

@app.post("/deposit/")
async def make_deposit(data: DepositRequest):
    await asyncio.sleep(0)
    
    async with lock:
        account = fake_db.get(data.number_account)

    if not account:
        return {"error": "Account not found"}

    try:
        account.deposit(data.value)
    except ValueError as e:
        return {"error": str(e)}

    return {
        "message": "Deposit successfully.",
        "account": account.show_account()
    }
    
@app.post("/withdraw/")
async def make_withdraw(data: WithdrawRequest):
    asyncio.sleep(0)
    
    async with lock:
        account = fake_db.get(data.number_account)
    
    if not account:
        return {"error": "Account not found"}
    
    try:
        account.withdraw(data.value)
    except ValueError as e:
        return {"error": str(e)}
    return{
        "message" : "Withdraw successfully.",
        "account" : account.show_account()
    }
    
@app.get("/transactions/")
async def get_transactions(data : GetTransactionsRequest):
    asyncio.sleep(0)
    async with lock:
        account = fake_db.get(data.number_account)
    
    if not account:
        return {"error": "Account not found"}
    
    try:
        transactions = account.show_transactions()
        return {"message" : "Successfully",
                "transactions" : transactions}
    except FileNotFoundError as e:
        return {"Error" : str(e)}
        
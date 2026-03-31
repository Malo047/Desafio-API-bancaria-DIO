from fastapi import FastAPI, status, Depends, HTTPException
from src.utils.auth import get_current_user, generate_token
from src.models.Account import Account
from src.schemas.Account import AccountCreate, DepositRequest, WithdrawRequest, GetTransactionsRequest
from src.schemas.security import LoginSecurity
import asyncio

app = FastAPI()
fake_db = {}
fake_users = {
    "marlon": {"password": "123", "name": "Marlon"}
}

lock = asyncio.Lock()

@app.post("/login/")
async def login(data: LoginSecurity):
    user = fake_users.get(data.username)

    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = generate_token(sub=data.username, name=user["name"])

    return {"access_token": token,
            "token_type": "Bearer"}

@app.post("/create_account/", status_code=status.HTTP_201_CREATED)
async def create_account(data: AccountCreate, user: dict = Depends(get_current_user)):
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
async def make_deposit(data: DepositRequest, user: dict = Depends(get_current_user)):
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
async def make_withdraw(data: WithdrawRequest, user: dict = Depends(get_current_user)):
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
async def get_transactions(data : GetTransactionsRequest, user: dict = Depends(get_current_user)):
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
        
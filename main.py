from datetime import datetime
from enum import Enum

from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from pydantic import BaseModel, Field
from typing import List, Optional

from auth.database import User
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from auth.manager import get_user_manager

app = FastAPI(
    title="FastApi Test"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"




fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]

class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType

class User(BaseModel):
    id: int = Field(ge=0)
    role: str
    name: str
    degree: Optional[List[Degree]] = []

@app.get("/")
async def read_root():
    return {"Hell": "World"}


@app.get("/user/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [ user for user in fake_users if user.get("id") == user_id ]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "USD", "side": "buy", "price": 100, "amount": 100},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 1010, "amount": 12.10}
]

@app.get("/trades")
def get_trades(limit: int = 1, offset: int=0):
    return fake_trades[offset:][:limit]

fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))

    current_user[0]["name"] = new_name
    return {"status": 200, "data": current_user}



class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    side: str
    price: float = Field(ge=0)
    amount: float

@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status":200, "data": fake_trades}
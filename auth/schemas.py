from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    hashed_password: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


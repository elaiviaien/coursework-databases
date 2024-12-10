from sqlmodel import SQLModel, Field
from typing import Optional


class UserBase(SQLModel):
    username: str
    email: str
    role: Optional[str] = "member"
    isBanned: bool = False


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int


class UserUpdate(SQLModel):
    username: Optional[str]
    email: Optional[str]
    role: Optional[str]
    isBanned: Optional[bool]
    password: Optional[str]


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str

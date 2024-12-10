from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from db import get_session
from models import User, UserCreate, UserRead, UserUpdate

api_router = APIRouter()


@api_router.post("/users/", response_model=UserRead, status_code=201)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    db_user = session.exec(select(User).where(User.username == user.username)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User.from_orm(user)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


@api_router.get("/users/", response_model=List[UserRead])
def read_users(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    users = session.exec(select(User).offset(skip).limit(limit)).all()
    return users


@api_router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@api_router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_update: UserUpdate, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user_update.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@api_router.delete("/users/{user_id}", response_model=UserRead)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return user

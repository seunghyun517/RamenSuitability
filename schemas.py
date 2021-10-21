from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    content: str
    writer_id: int

class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    meal_id: int

    class Config:
        orm_mode = True

class RatingBase(BaseModel):
    rating: int
    writer_id: int

class RatingCreate(RatingBase):
    pass


class Rating(RatingBase):
    id: int
    meal_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    comments: List[Comment] = []

    class Config:
        orm_mode = True


class MealBase(BaseModel):
    time: int
    menu: str

class MealCreate(MealBase):
    pass

class Meal(MealBase):
    id: int
    score: int
    comments: List[Comment] = []
    ratings: List[Rating] = []
    
    class Config:
        orm_mode = True

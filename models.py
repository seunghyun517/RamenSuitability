from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(Integer)
    menu = Column(String)
    score = Column(Integer)
    comments = relationship("Comment", back_populates="meal")
    ratings = relationship("Rating", back_populates="meal")


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    writer_id = Column(Integer, ForeignKey("users.id"))
    meal_id = Column(Integer, ForeignKey("meals.id"))
    writer = relationship("User", back_populates="ratings")
    meal = relationship("Meal", back_populates="ratings")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    writer_id = Column(Integer, ForeignKey("users.id"))
    meal_id = Column(Integer, ForeignKey("meals.id"))
    writer = relationship("User", back_populates="comments")
    meal = relationship("Meal", back_populates="comments")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")
    comments = relationship("Comment", back_populates="writer")
    ratings = relationship("Rating", back_populates="writer")



class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")

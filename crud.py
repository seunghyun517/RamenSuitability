from sqlalchemy import schema
from sqlalchemy.orm import Session
from mealScore import computeMealScore
import models, schemas


def get_meals(db: Session, skip: int = 0, limit: int = 7):
    return db.query(models.Meal).offset(skip).limit(limit).all()


def get_meal(db: Session, meal_id: int):
    return db.query(models.Meal).filter(models.Meal.id == meal_id).first()


def create_meal(db: Session, meal: schemas.MealCreate):
    score = computeMealScore(meal.menu)
    db_meal = models.Meal(time = meal.time, menu = meal.menu, score = score)
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):

    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_comment(db: Session, comment: schemas.CommentCreate, meal_id: int):
    db_comment = models.Comment(**comment.dict(), meal_id=meal_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
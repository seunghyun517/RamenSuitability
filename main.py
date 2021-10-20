from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mealScore import computeMealScore
from sqlalchemy.orm import Session

import crud, schemas, models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

datameals = [
    {"id": 1, "meal": "아침", "menu":"쌀밥 쇠고기떡국⑤⑯ 돈육꽈리장조림⑤⑩ 명란구운김⑤ 배추김치 바나나 우유식빵①②⑥ 아몬드시리얼/우유 ①②⑥"},
    {"id": 2, "meal": "점심", "menu":"차조밥 된장찌개⑤⑱ 차돌박이숙주볶음⑤⑯ 까르보떡볶이②⑩ 배추나물무침⑤ 갓김치⑨ 단감 불고기후랑크⑤⑩⑮ /머스터드①"},
    {"id": 3, "meal": "저녁", "menu":"쌀밥 김치찌개⑤⑩ 불낙전골⑤⑯ 참치야채볶음⑤ 오이부추무침⑤ 깍두기⑨ 아이브② 물떡꼬치"},
    {"id": 4, "meal": "아침", "menu":"쌀밥 전복죽⑱ 쇠고기데리야끼볶음⑤⑯ 연두부⑤/양념장⑤ 콘샐러드①⑤⑥ 배추김치⑨ 찰보리빵①⑤⑬ 요거링/초코볼②⑤⑥ 바나나/우유②"},
    {"id": 5, "meal": "점심", "menu":"강황미밥(학생쌀밥) 닭곰탕⑮ 쇠갈비떡찜⑤⑯ 해물부추전①⑤⑥ 무오이채장아찌무침 매콤츄러스만두 ⑤⑥⑩⑯ 고들빼기김치⑨ 포도 공주님/왕자님쥬스"},
    {"id": 6, "meal": "저녁", "menu":"참치새싹비빔밥⑤ 들깨시락국⑤ 버팔로윙오븐구이⑤⑮ 알배추겉절이 총각김치⑨ 바나나우유② 찹쌀고구마치즈볼 ①②⑤⑥"},
    {"id": 7, "meal": "아침", "menu":"쌀밥 맑은소고기국⑤⑯ 베이컨스크램블에그 ①②⑨⑩ 찐두부/볶음김치⑤⑨ 김구이⑤ 바나나 에너지바①②⑤⑥ 아몬드시리얼⑥/우유②"},
]

ratingofMeals = {
    1: [{"user": "sangwoo", "rating": 2}, {"user": "seunghyun", "rating": 4}],
    2: [{"user": "sangwoo", "rating": 1}, {"user": "seunghyun", "rating": 4}],
    3: [{"user": "sangwoo", "rating": 4}, {"user": "seunghyun", "rating": 5}],
    4: [{"user": "sangwoo", "rating": 3}, {"user": "seunghyun", "rating": 4}],
    5: [{"user": "sangwoo", "rating": 3}, {"user": "seunghyun", "rating": 4}],
    6: [{"user": "sangwoo", "rating": 3}, {"user": "seunghyun", "rating": 5}],
    7: [{"user": "sangwoo", "rating": 3}, {"user": "seunghyun", "rating": 4}]
}

commentsofMeals = {
    1: [{"user": "sangwoo", "content": "별로입니다"}, 
    {"user": "seunghyun", "content": "생각보다 괜찮은듯?"}],
    2: [{"user": "sangwoo", "content": "별로에요"}, 
    {"user": "seunghyun", "content": "생각보다 괜찮은듯?"}],
    3: [{"user": "sangwoo", "content": "별로라고요"}, 
    {"user": "seunghyun", "content": "생각보다 괜찮은듯?"}],
    4: [{"user": "sangwoo", "content": "별로라니까요"}, 
    {"user": "seunghyun", "content": "생각보다 괜찮은듯?"}],
    5: [{"user": "sangwoo", "content": "맛없어요"}, 
    {"user": "seunghyun", "content": "생각보다 괜찮은듯?"}],
    6: [{"user": "sangwoo", "content": "싫어요"}, 
    {"user": "seunghyun", "content": "생각보다 괜찮은듯?"}],
    7: [{"user": "sangwoo", "content": "예아"}, 
    {"user": "seunghyun", "content": "생각보다 괜찮은듯?"}]
}

for meal in datameals:
    meal["score"] = computeMealScore(meal["menu"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/meals/", response_model=List[schemas.Meal])
def read_meals(skip: int = 0, limit: int = 7, db: Session = Depends(get_db)):
    mealsFromDatabase = crud.get_meals(db, skip=skip, limit=limit)
    return mealsFromDatabase


@app.post("/meals/", response_model=schemas.Meal)
def create_meal(meal: schemas.MealCreate, db: Session = Depends(get_db)):
    return crud.create_meal(db=db, meal=meal)


@app.get("/meals/{meal_id}", response_model=schemas.Meal)
def read_meal(meal_id: int, db: Session = Depends(get_db)):
    return crud.get_meal(db=db, meal_id=meal_id)

# @app.get("/meals/{meal_id}/ratings")
# def read_meal_ratings(meal_id: int):
#     ratings = ratingofMeals[meal_id]
#     ratingsum = sum([rating["rating"] for rating in ratings])
#     ratingavg = ratingsum / len(ratings)
#     return {"ratings": ratings, "ratingavg": ratingavg}


@app.post("/meals/{meal_id}/comments", response_model=schemas.Comment)
def create_meal_comments(meal_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment, meal_id=meal_id)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

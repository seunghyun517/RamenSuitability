from dishScore import *
import re

def compileMeal(meal):
    predishes = meal.split()
    dishes = []
    for predish in predishes:
        tmp = re.compile('[가-힣]+').findall(predish)
        if len(tmp) != 0:
            dishes.append(tmp[0])
    return dishes


def computeMealScore(meal):
    dishes = compileMeal(meal)
    if __name__ == "__main__":
        for dish in dishes:
            print(dish, computeDishScore(dish))
    dishScoreAvg = round(sum(computeDishScore(dish) for dish in dishes) / len(dishes))
    mealScore = dishScoreAvg + (len(dishes)- 9) * 5
    return mealScore


if __name__ == "__main__":
    today_meal = "쌀밥 맑은소고기국⑤⑯ 베이컨스크램블에그 ①②⑨⑩ 찐두부/볶음김치⑤⑨ 김구이⑤ 바나나 에너지바①②⑤⑥ 아몬드시리얼⑥/우유②"
    print(computeMealScore(today_meal))

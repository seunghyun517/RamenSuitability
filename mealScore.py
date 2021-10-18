from menuScore import *
import re

def compileMeal(meal):
    premenus = meal.split()
    menus = []
    for premenu in premenus:
        tmp = re.compile('[가-힣]+').findall(premenu)
        if len(tmp) != 0:
            menus.append(tmp[0])
    return menus


def computeMealScore(meal):
    menus = compileMeal(meal)
    if __name__ == "__main__":
        for menu in menus:
            print(menu, computeMenuScore(menu))
    return round(sum(computeMenuScore(menu) for menu in menus) / len(menus))


if __name__ == "__main__":
    today_meal = "쌀밥 맑은소고기국⑤⑯ 베이컨스크램블에그 ①②⑨⑩ 찐두부/볶음김치⑤⑨ 김구이⑤ 바나나 에너지바①②⑤⑥ 아몬드시리얼⑥/우유②"
    print(computeMealScore(today_meal))

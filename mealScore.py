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


def computeMealScore(menus):
    for menu in menus:
        print(menu, computeMenuScore(menu))
    return sum(computeMenuScore(menu) for menu in menus) / len(menus)


today_meal = "단호박로제스파게티 ①②⑤⑥⑫ 게살스프⑧ 수비드폭립⑤⑩ 모짜렐라펄샐러드② 과일요거화채② 감자부꾸미 무피클 스파클링 (밥.김치.김)"
today_menus = compileMeal(today_meal)
print(computeMealScore(today_menus))

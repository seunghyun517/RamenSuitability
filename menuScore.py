f = open("data.txt", 'r', encoding='UTF8')

menuData = dict()
cnt = 0

for line in f:
    idx, menu, rate = line[1:-3].split(',')
    idx = int(idx)
    menu = menu[1:].strip("'")
    rate = int(rate[1:].strip("'"))
    menuData[idx] = (menu, rate)


def getLinearAverage(L):
    N = len(L)
    summ = 0
    for i in range(N):
        summ += L[i] * (i+1)
    return summ / (N*(N+1)/2)


def computeMenuScore(menu):
    N = len(menu)

    rateWithCmpstrLength = [0]*N

    for i in range(1,N+1):
        ratesum = 0
        matchcnt = 0
        for j in range(N-i+1):
            cmpstr = menu[j:j+i]
            for dat in menuData:
                if cmpstr in menuData[dat][0]:
                    ratesum += menuData[dat][1]
                    matchcnt += 1
        if matchcnt == 0 :
            rateWithCmpstrLength[i-1] = None
        else: 
            rateWithCmpstrLength[i-1] = ratesum / matchcnt
            
    # print(rateWithCmpstrLength)

    reducedList = [k for k in rateWithCmpstrLength if k != None]
    score = getLinearAverage(reducedList) - 1
    score = 25 * (score - 2) + 50
    if score > 100: score = 100
    if score < 0: score = 0
    return score


if __name__ == '__main__':
    print(computeMenuScore("찹쌀고구마치즈볼"))
                
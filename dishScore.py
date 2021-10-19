f = open("data.txt", 'r', encoding='UTF8')

dishData = dict()
cnt = 0

for line in f:
    idx, dish, rate = line[1:-3].split(',')
    idx = int(idx)
    dish = dish[1:].strip("'")
    rate = int(rate[1:].strip("'"))
    dishData[idx] = (dish, rate)


def getLinearAverage(L):
    N = len(L)
    summ = 0
    for i in range(N):
        summ += L[i] * (i+1)
    return summ / (N*(N+1)/2)


def computeDishScore(dish):
    N = len(dish)

    rateWithCmpstrLength = [0]*N

    for i in range(1,N+1):
        ratesum = 0
        matchcnt = 0
        for j in range(N-i+1):
            cmpstr = dish[j:j+i]
            for dat in dishData:
                if cmpstr in dishData[dat][0]:
                    ratesum += dishData[dat][1]
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
    print(computeDishScore("찹쌀고구마치즈볼"))
                
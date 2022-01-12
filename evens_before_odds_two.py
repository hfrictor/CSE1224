li = [3,4,6,5,2,1,8]

def evens_before_odds_2(li):
    result = [0] * len(li)
    even = 0
    odd = (len(li)-1)

    for e in range(len(result)):
        if int(li[e]) % 2 == even and li[e] != 0:
            result.append(li[e])
        else:
            print((len(li)-e-1))
            result.append(li[(len(li)-e-1)])

    print(result)


evens_before_odds_2(li)
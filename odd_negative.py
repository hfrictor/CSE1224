li = [2,-3,4,-2,-7,7,10]

def odd_negative(li):
    result = []
    for o in range(len(li)):
        if int(li[o]) % 2 != 0 and li[o] < 0:
            result.append(li[o])

    print(result)





input_li = input("Please input a list of numbers in the format (1, 2, 3, 4) : ")

li = [3,4,6,5,2,1,8]
result = []

li_length  = len(li)
print(li_length)

for e in range(li_length):
    if int(li[e]) % 2 == 0 and li[e] != 0:
        result.append(li[e])

for o in range(li_length):
    if int(li[o]) % 2 != 0 or li[o] == 0:
        result.append(li[o])


print(result)
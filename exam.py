#1
n = 10
n1 = 12

def solution2(n):
    x = int(3)

    if n % x == 1:
        return x
    else:
        return n1


print(solution2(n))
print(solution2(n1))


#2
absolutes = [4, 7, 12]
signs = [True, False, True]

absolutes2 = [1,2,3]
signs2 = [False,False,True]

def solution3(absolutes, signs):
    result = []
    info = dict(zip(absolutes,signs))

    for str,kor in info.items():
        if kor == True:
            result.append(str)
        else:
            result.append(-str)
        
    return sum(result)

print(solution3(absolutes,signs))
print(solution3(absolutes2,signs2))

#3

def solution4(price, money, count):
    result = 0

    for num in range(1, count + 1):
        own = price * num
        result += own

    if(money - result < 0):
        result = money - result
    else:
        result = 0

    return abs(result)
        

price = 3
money = 20
count = 4
count2 = 3
count3 = 2

print(solution4(price,money,count))
print(solution4(price,money,count2))
print(solution4(price,money,count3))


def add(*args):
    result = 0

    for i in args:
        result += i

    return result

print(add(1,2,2,3,4))





def solution4(price, money, count):
    result = 0

    for i in range(1, count + 1):

        return i
     #   num = price * i
     #   result += num

    #if(money - result < 0):
    #    result = money - result
    #else:
     #   result = 0

    #return abs(result)

#price = 3
#money = 20
#count = 4
#count2 = 3
#count3 = 2

print(solution4(price,money,count))
#print(solution4(price,money,count2))
#print(solution4(price,money,count3))

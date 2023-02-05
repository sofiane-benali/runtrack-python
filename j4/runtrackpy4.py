#job 1
def list():
    fruits = ["pomme", "cerise", "orange"]
    return fruits

#job 2
def listb():
    fruitsb = ["pomme", "cerise", "orange"]
    print(fruitsb[1])
    return fruitsb

listb()

#job 3
def listc():
    fruitsc = ["pomme", "cerise", "orange"]
    fruitsc.append("melon")
    print(fruitsc)
    return fruitsc

listc()

#job 4
def listd():
    fruitsd = ["pomme", "cerise", "orange", "melon"]
    fruitsd.insert(2,"mangue")
    print(fruitsd)
    return fruitsd
listd()

#job 5
def liste():
    L = [1, 2, 3, 4, 5]
    print(L[1])
    L[3] = L[2] + L[4]
    print(L[-1])

liste()

# job6

def listf():
    L = [1, 2, 3, 4, 5]
    first = L[0]
    last = L[-1]
    L[0] = last
    L[-1] = first
    print(L)
    return L
listf()
# job 7
def countmultipl():
    L = [8, 24, 48, 2, 16]
    count = 0
    for i in L:
        if i % 3 == 0:
            count += 1
    print(count)
countmultipl()

#job 8
def countpair():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    count = 0
    for i in L:
        if i % 2 == 0:
            count += 1
    print(count)
countpair()
#job 9
def diremax():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    lemax = max(L)
    lemin = min(L)
    print("Le max est "+str(lemax)+"Le min est "+str(lemin))

diremax()

#job 10

def calcullist():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    product = 1
    for num in L:
        if num > 25 and num < 90:
            product *= num
    print(product)


calcullist()

#job 11
def plusunlist():

    L = [7, 11, 42, 39, 2]
    for i in range(len(L)):
        L[i] += 1
    print(L)

plusunlist()
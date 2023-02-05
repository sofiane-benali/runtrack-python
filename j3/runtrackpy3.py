#job1
def nombreunavingt():
    for number in range(0,21):
        print(number)

nombreunavingt()

#job2
def nombreunsurdeux():
   for number in range(0,21):
       if number %2 ==0:
           print(number)

nombreunsurdeux()

#job3
def numberonly():
    for chiffre in range(0,101):
        if chiffre == 26 or chiffre == 37 or chiffre == 88:
            continue
        print(chiffre)
numberonly()
#job4
def fizzbuzz():
    for number in range(0,101):
        if number % 3 == 0 :
            print("Fizz")
        elif number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        print(number)
fizzbuzz()
#job5
def firstnumberto1000():
    for number in range(0,1001):
        print(number)

firstnumberto1000()
#job6
# def pyramidalph():
#     chaine = "abcdefghijklmnopqrstuvwxyz" * 10
#
#     for i in range(1, int((-1 + (1 + 8 * len(chaine)) ** 0.5) // 2) + 1):
#         print(chaine[:i])
#         chaine = chaine[i:]
#
# pyramidalph()




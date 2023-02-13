#job 1
def hellotoi():
    askname = input("Quel est votre nom ?")
    return print("Votre nom est ",askname)

#job 2
def rectangledessin(h,l):

    print("|", "-"*(l-2), "|")
    for i in range(h-2):
        print("|", " "*(l-2), "|")
    print("|", "-"*(l-2), "|")



#job 3
def tapis(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                print(" ", end=" ")
            else:
                print("#", end=" ")
        print()


#job 4
def chiffrement(lettre,clef):
    key = ord(lettre) + clef
    if key > 122:
        key -= 26
    return chr(key)

print(chiffrement("o",3))

def c_chiffrement(message,clef):
    chiffr = ""
    for lettre in message:
        if lettre == " ":
            chiffr += " "
        else: chiffr += chiffrement(lettre,clef)

    return chiffr

print(c_chiffrement("hello wolrd",10))

#jo 4










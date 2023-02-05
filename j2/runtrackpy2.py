#job 1
def my_print():
    return print("Hello")
my_print()
#job 2
def print_name(name):
    return print(name)

print_name("sofiane")
#job 3
def add(un,deux):
    addition = un + deux
    print(addition)
    return addition
add(1,2)
#job 4
def get_hello():
    phrase = "Hello la Plateforme"
    print(phrase)
    return phrase

get_hello()
# job 5
def calculatrice(un,op,deux):
    if op == "+":
        result = un + deux
    elif op == "-":
        result = un - deux
    elif op == "/":
        result = un / deux
    print(result)
    return result
calculatrice(1,"/",2)
#job 6
def checknumber(number):
    if number > 0:
        return "positif"
    elif number < 0:
        return "negatif"

print(checknumber(30))

#job7

def blabla(langage):
    if langage == "js":
        return "tu es un dev web"
    elif langage == "python":
        return  "tu es un dev ia"

print(blabla("js"))
#job 8
def mangezsaison(type,saison):
    if type == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
    elif type == "fruits" and saison == "été":
        return "Poire, fraise, cassis"
    elif type == "légume" and saison == "hiver":
        return "carotte, topinambour, endive"
    elif type == "légume" and saison == "été":
        return "artichaut, aubergine,navet"

print(mangezsaison("fruits","été"))



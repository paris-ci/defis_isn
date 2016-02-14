import math


def eq2():
    a = int(input("Vueillez entrer la valeur de a dans l'expression ax²+bx+c >"))
    b = int(input("Vueillez entrer la valeur de b dans l'expression ax²+bx+c >"))
    c = int(input("Vueillez entrer la valeur de c dans l'expression ax²+bx+c >"))
    delta = b * b - 4 * a * c
    print("∆ = " + str(delta))
    if delta == 0:
        print("La valeur de l'unique racine est", (-b / (2 * a)))
    elif delta > 0:
        print("La valeur de la première racine est", ((-b - math.sqrt(delta)) / (2 * a)))
        print("La valeur de la deuxième racine est", ((-b + math.sqrt(delta)) / (2 * a)))
    elif delta < 0:
        print("La valeur de la première racine imaginaire est", ((-b - math.sqrt(- delta)) / (2 * a)))
        print("La valeur de la deuxième racine imaginaire est", ((-b + math.sqrt(- delta)) / (2 * a)))


eq2()

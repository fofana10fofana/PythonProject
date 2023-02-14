import math
def discrinant(a,b,c) :
    delta = (b ** 2) - 4 * a * c
    return delta
def solution(a,b,c) :
    delta = discrinant(a,b,c)
    if delta < 0 :
        print("pas de solution")
    elif delta == 0 :
        x =(-b)/(2*a)
        print("la solution est :",format(x,"2f"))
    else:
        x1 = (-b-math.sqrt(delta)) / (2 * a)
        x2 = (-b+math.sqrt(delta)) / (2 * a)
        print("les solution sont :",format(x1, ".2f"),"et",format(x2, ".2f"))
a = float(input("veillez saisir la valeur de a : "))
if a == 0:
    print('pas de solution')
else:
    b = float(input("veuiller saisir la valeur de b"))
    c = float(input("veuiller saisir la valeur de c"))
solution(a,b,c)


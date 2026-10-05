Xa = float(input("Veuillez défénir la valeur de Xa :  "))
Xb = float(input("Veuillez défénir la valeur de Xb :  "))
Ya = float(input("Veuillez défénir la valeur de Ya :  "))
Yb = float(input("Veuillez défénir la valeur de Yb :  "))

a = 0
b = 0

if (Xa == Xb):
    print("pas de fonction affine une droite verticale")
else:
    a = float((Yb-Ya)/(Xb-Xa))
    print("la valeur du directeur a est de ")
    print(a)
    b = float(Ya - a * Xa)
    print("l'équation de la droite est de")
    print(b)
    
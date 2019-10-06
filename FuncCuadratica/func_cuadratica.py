import os
from FuncCuadratica.calc_func_cuadratica import *

# Visual de la parte de Funcion Cuadratica.


def polinomio2():
    while True:

        try:

            a = float(input("\nPrimer valor (a): "))
            b = float(input("Segundo valor (b): "))
            c = float(input("Tercer valor (c): "))

            x1, x2, xv, yv = PolinomioCuadratico(a, b, c).calcular()

            print("Las raices valen " + "{" + "{}. {}".format("%.2f" % x1, "%.2f" % x2) + "}")
            print("El vertice es ({}, {})".format("%.2f" % xv, "%.2f" % yv))

            PolinomioCuadratico(a, b, c).graficar()

            input("\nEnter para volver.")

            break
        except:
            print("Valor no valido, intentelo de nuevo")
            continue


def factorizada2():
    while True:

        try:

            a = float(input("\nPrimer valor (a): "))
            x11 = float(input("Segundo valor (x1): "))
            x22 = float(input("Tercer valor (x2): "))

            b, c = cuadratica_factorizada(a, x11, x22)

            x1, x2, xv, yv = PolinomioCuadratico(a, b, c).calcular()

            print("Las raices valen " + "{" + "{}. {}".format("%.2f" % x1, "%.2f" % x2) + "}")
            print("El vertice es ({}, {})".format("%.2f" % xv, "%.2f" % yv))

            PolinomioCuadratico(a, b, c).graficar()

            input("\nEnter para volver.")

            break

        except:
            print("Valor no valido, intentelo de nuevo")
            continue


def canonica1():
    while True:

        try:

            a = float(input("\nPrimer valor (a): "))
            xv1 = float(input("Segundo valor (xv): "))
            yv2 = float(input("Tercer valor (yv): "))

            b, c = cuadratica_canonica(a, xv1, yv2)

            x1, x2, xv, yv = PolinomioCuadratico(a, b, c).calcular()

            print("Las raices valen " + "{" + "{}. {}".format("%.2f" % x1, "%.2f" % x2) + "}")
            print("El vertice es ({}, {})".format("%.2f" % xv, "%.2f" % yv))

            PolinomioCuadratico(a, b, c).graficar()

            input("\nEnter para volver.")

            break

        except:
            print("Valor no valido, intentelo de nuevo")
            continue


def menu():
    os.system('clear')
    print("Eliga una opcion:")
    print("1-- Polinomio")
    print("2-- Factorizada")
    print("3-- Canonica")
    print("4-- Salir")

    option = input("Opción: ")
    return option
    

def funcion_cuadratica():

    while True:
        option = menu()
        
        if option == '1':
            os.system('clear')
            polinomio2()
            continue

        elif option == '2':
            os.system('clear')
            factorizada2()
            continue

        elif option == '3':
            os.system('clear')
            canonica1()
            continue

        elif option == '4':
            break

        else:
            print("El valor no es valido, intentelo de nuevo")
            continue


def Saludo_Personalzado(Nombre):

    print("Hola!", Nombre)

Saludo_Personalzado("Cesar")

def radio_cuadrado(radio):


    formula = 3.14*radio**2

    print(formula)
    return radio_cuadrado
radio_cuadrado(2)

def millas_Kilometros(milas):

    formula2 = milas*1.60934
    print(formula2)
    return millas_Kilometros

millas_Kilometros(2)

def Repetir_texto(Nombre):

    for i in Nombre:
        print(i)

Repetir_texto("cesar")

def mutliplicacion_simple(a,b):

    formula= a*b

    print(formula)
    return mutliplicacion_simple
mutliplicacion_simple(2,3)

def perimetro_Rentaongo(largo,ancho):

    formula = 2*(largo+ancho)
    
    print(formula)
    return perimetro_Rentaongo

perimetro_Rentaongo(10,3)

def calcular_temperatura_media(maxima, minima):
    return (maxima + minima) / 2

def programa_principal():

    numero_dias = int(input("Cuantos dias vas a introducir: "))

    for i in range(numero_dias):
        maxima = float(input(f"Dia {i + 1} -  temperatura maxima: "))
        minima = float(input(f"Dia {i + 1} -  temperatura mínima: "))
        media = calcular_temperatura_media(maxima, minima)
        print(f"Dia {i + 1} - La temperatura media {media} grados celcius")

programa_principal()



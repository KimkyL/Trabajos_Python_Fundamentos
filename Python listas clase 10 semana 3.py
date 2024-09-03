Hola = ['Fisica', 'Matemaicas', 'Materia y Energia', 'Espanol', 'Cuidado del cuerpo humano']
print(Hola[1])
print(Hola[0])
print(Hola[3])
print(Hola[0],Hola[2],Hola[4])
print(Hola[2:])
Hola [3] = 'Matematicas'
for Hola in Hola:
    print(Hola)
else:
    print("no hay materias a cursar")

Numeros = ['1','2','3','4','5','6','7']

print(Numeros[4:])

"""
Oh... Hola como estas este codigo lo hice yo pero ya me trabe en que hacer mas, creo que la programacion no es lo mio Jejeje.... bueno
quiero dejar que en la linea 32 (Si no es que se ha movido) era .copy antes que append pero bueno que soy yo para cambiarlo XD.
"""

Frutas = ['Manzana','Pera','Manzana_Golden','Manzana_Peruana','Manzana_Argentina','Manzana Negra','Manzana Dorada', 'Manzana_Quepongomas']
    
print("Lista original de frutas:")
print(Frutas)
indice = int(input(f"Elige el índice (1-{len(Frutas)+1}) de la fruta que quieres cambiar: "))
    

Frutas4 = input("Introduce la nueva fruta: ")
    

FrutasCambiadas23 = Frutas.copy()
    

FrutasCambiadas23[indice] = Frutas4
    

print("\nLista nueva de frutas:")
    

print(FrutasCambiadas23)

"""
Hola!, como estas bueno ya pude arreglar esto y aunque si actualiza la variable de lista no le puse while para que no sea tannnn complicado
con esto te dejo la ultima parte de este trabajo y pues ahi como va.
"""

lista = ['Numero', 9, False]

for lista in lista:
    print(type(lista))

"""
ya con esto te dejo con una variable sin variable

"""


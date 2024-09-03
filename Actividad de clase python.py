# Conversión de temperatura de Celsius a Fahrenheit
TP = float(input("Ingresa tu temperatura en grados Celsius: "))
fahrenheit = (9 / 5 * TP) + 32
print("La temperatura equivale a", fahrenheit, "Grados Fahrenheit")

# Cálculo del área de un círculo
Radio = float(input("Ahora proporciona el radio de un círculo: "))
HC = 3.1416
area = HC * Radio ** 2
print("Tu área equivale a", area)

# Cálculo del perímetro de un rectángulo
Base = float(input("Proporciona la base del rectángulo: "))
Altura = float(input("Proporciona la altura del rectángulo: "))
perimetro = (Base * 2) + (Altura * 2)
print("El perímetro del rectángulo es de", perimetro)

# Cálculo de la suma de los primeros numeros enteros
Juan = int(input("Proporciona un entero: "))
resultado = (Juan * (Juan + 1)) / 2
print("El resultado es", resultado)

# Cálculo de la capital obtenida en una inversión
PesoDolar = float(input("Proporciona una cantidad de dinero para invertir: "))
Elinteres = float(input("Proporciona un interés: "))
Años = int(input("Proporciona el número de años: "))
capital_obtenida = PesoDolar + (PesoDolar * (Elinteres / 100)) * Años
print("La capital obtenida en la inversión es de", capital_obtenida)

# Cálculo de ahorro en cuenta con interés compuesto
deposito = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))
i = float(input("Introduce el interés anual en decimal (por ejemplo, 0.05 para 5%): "))

ahorro1 = deposito * (1 + i)
ahorro2 = ahorro1 * (1 + i)
ahorro3 = ahorro2 * (1 + i)

print("Cantidad de ahorros tras el primer año: ", ahorro1)
print("Cantidad de ahorros tras el segundo año: ", ahorro2)
print("Cantidad de ahorros tras el tercer año: ", ahorro3)

# Cálculo del costo final de barras de pan no frescas
precio_habitual = 3.49
descuento = 0.60

num_barras = int(input("Introduce el número de barras vendidas que no son del día: "))
coste_final = num_barras * precio_habitual * (1 - descuento)

print("Precio habitual de una barra de pan: $", precio_habitual)
print("Descuento por no ser fresca:", descuento * 100, "%")
print("Coste final total: $", coste_final)

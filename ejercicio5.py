# Solicitar al usuario el valor de los dos lados del rectángulo
lado1 = float(input("Introduce la longitud del primer lado del rectángulo: "))
lado2 = float(input("Introduce la longitud del segundo lado del rectángulo: "))

# Calcular el perímetro del rectángulo
perimetro = 2 * (lado1 + lado2)

# Calcular el área del rectángulo
area = lado1 * lado2

# Mostrar los resultados
print(f"El perímetro del rectángulo es: {perimetro}")
print(f"El área del rectángulo es: {area}")

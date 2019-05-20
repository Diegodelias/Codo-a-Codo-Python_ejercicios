

def maximo(x,y,z):
    valorMaximo = x
    if(y > valorMaximo):
        valorMaximo = y
    if (z > valorMaximo):
        valorMaximo = z
    return valorMaximo

print("Escriba tres valores de punto flotante, separados por espacios:")

numero1= float(input("ingrese el primer numero "))

numero2= float(input("ingrese el segundo numero "))

numero3= float(input("ingrese el tercer numero "))

resultado = maximo(numero1,numero2,numero3)
print("El maximo es: " , resultado)




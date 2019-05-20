"""
Ingresar 20 notas  y almacenarlas en una lista

calcular sumatoria de todas las notas e imprimirla en pantalla

mostrar notas ingresadas
"""

sumatoria = []
sum = 0
nrnota = 0
print("Complete 20 notas, ingresando de una en una")

for n in range(0,44):
    print("=", end = '')
print('\n')
for n in range (0,20):
    print("ingrese la nota nro", (n + 1), ":"  )
    nota = int(input())
    sumatoria.append(nota)
for numero in sumatoria:
   sum = sum + numero
print("la suma es =" ,sum)

for contar in sumatoria:
    nrnota = nrnota + 1
    print("Nota" , nrnota , "= " , sumatoria[nrnota-1])
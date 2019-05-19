import random
#declaracion lista tiradas vacía
tiradas = []
#realiza 6000000 tiradas y le asigna una valor aleatorio entre 1 y 6 a cada posición en la lista tiradas
for tiro in range (0 , 6000000):
    aleatorio = ( random.randint(1,6))
    tiradas.append(aleatorio)

for cara in range (1,7):
   print ("cara",cara , "frecuencia:" , tiradas.count(cara))



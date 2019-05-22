import math

principal= 10000
tasa = 0.74

print("{:<15} {}".format("Anio","Monto en deposito"))

for anio in range(1,11):
    monto = principal * pow(1.0 + 0.74 , anio)
    print("{:<15} {}".format(anio,monto))

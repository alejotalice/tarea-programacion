monto = float(input("Cantidad de invercion? "))
interes = float(input("Interés anual? "))
años = int(input("Años?"))
for i in range(años):
    monto *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(monto, 2)))
edad = int(input("Ingrese su edad: "))
try:
    if edad < 18:
        print("")
except ValueError:
    print("No puedes accesor")

def prueba1():
        
    import time 

    print("Bienvenido!!")
    time.sleep(5) # Simulamos que tarda 5 segundos
    input("Dame tu nombre: ")


import time
def prueba2():
    inicio = time.time() #guardamos el proceso antes de dar inicio o ejecutar la tarea

    time.sleep(2) #Simulamos un proceso que tarda 2 segundos 

    fin = time.time() #Guarda el tiempo despues del proceso
    print(f"El proceso tardo {fin} segundos")



def hora():
    horaActual = time.localtime()
    print(horaActual)
    formato = time.strftime("%Y-%m-%d %H-%M")
    print(formato)
hora()
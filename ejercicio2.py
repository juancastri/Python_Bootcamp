#Problema:
""" Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla """

#datos
peso=float(input("Por favor ingrese su peso corporal en kg: "))
estatura=float(input("Por favor ingrese su estatura en metros: "))

#calcular indice de masa corporal
IMC= peso / estatura**2

#imprimir resultados
print("Tu indice de masa corporal es: {:.2f}".format(IMC))


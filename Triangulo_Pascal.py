#Taller 3,3
#Realice una función que imprima como salida (a) las primeras N filas del triángulo de pascal. Utilice funciones y ciclos.

n = int(input("Ingrese por favor el numero de filas a generar: "))
matriz=[]
z=0
for x in range(n):
	matriz.append([])

for x in range(n): 
	for y in range(x+1): 
		if y==0 or y==x: #Como en los extremos siempre es 1 por eso se usa esta funcion 
			matriz[x].append(1)
		else:
			z=matriz[x-1][y]+matriz[x-1][y-1] #Se realiza la suma de los dos elementos de la fila de arriba que corresponden a la posicion
			matriz[x].append(z)
	print(str(matriz[x]))		
input()
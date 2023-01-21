# parcial
phyton
'''Elaborar el código de la multiplicación de una matriz bidimensional, 
utilizar funciones para realizar la operación multiplicación. Asimismo,
 el resultado ordenar de manera descendente. Finalmente, 
 realizar una función de búsqueda para revisar si la matriz resultado tiene el valor 9,
  en caso fuese afirmativo, indicar por pantalla
   " La matriz tiene el valor 9 y se encuentra en la posición i (fila) y j (columna).'''

def multiplicacion_de_matrizes(x,y)

# función de dos matrizes
result = [o for i in range(len(y[0]))]

for j in range(len(x)):

# usaremos el bucle for y hacemos funcion a las matrizes
for
for i in range (len(x)):
        for j in range(len(y[0])):
            for k in range (len(y)):
                #la operacion
                result[i][j] += x[i][k]*y[k][j]
        return result

#continuamos ordenando la matriz

def matriz_ordenar(matriz):
    #la funcion ordenaremos de forma ascendenete
    return sorted(matriz,key=lambda)x:x,reverse=true

def matriz_evalue(matriz_evalue)
    return "la mtriz si enconctro el valor 9 y se encuentra en a posicion"
result.index[evalue]

 return "en esta matriz no se encuenntra el valor 9"

x= [[5,6,7]],[[10,11,12]]
y=[[11,10,9]],[[7,6,5]]
result=
matriz_multiplicacion(x,y)
result=matriz_ordenar(result)
print(result)
print(buscamos_en_la_matriz(result,9))



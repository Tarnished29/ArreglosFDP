playlistT = [
    "After Hours.mp3" ,  #Elemento 0
    "Wake me up feat Justice.mp3" , #Elemento 1
    "Arms around you.mp3" , #Elemento 2
    "In Your Eyes.mp3" , #Elemento 3
    "Starboy.mp3" #Elemento 4
    # 4 elementos para Python (cuenta a partir del 0), 5 elementos vistos por el humano (se cuenta a partir del 1)

]

print("#######################")
print(playlistT[0])
print("#######################")

print("Tamaño del arreglo")
# Tamaño = mostrar cantidad de elementos
size = len(playlistT) #Variable nueva = len(nombre objeto)
print("La última canción es: ")
print(playlistT[size - 1])
#Para añadir el último valor de la lista, es size - 1



nuevapalabra = "esternocleidomastoideo"
print("Imprimir todas las letras de una palabra: La palabra escogida es",nuevapalabra,"")

# for = iteración (suma acumulativa)
# -> for i in range(len(variable)):



for i in range(len(nuevapalabra)):
    print(nuevapalabra[i])
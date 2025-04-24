palabra = ""

print("Ingresa la palabra para revisar si es palíndromo:")
palabra = input()

nuevapalabra = ""

for i in range(len(palabra)):
    print( palabra[ (len(palabra) - 1 ) - i] )
    nuevapalabra += palabra[ (len(palabra) - 1 ) - i]
    print("La nueva palabra es: " + nuevapalabra)

if palabra == nuevapalabra:
    print("La palabra: " + palabra + " es igual a la palabra " + nuevapalabra + ". Son palíndromos.")
else:
    print("La palabra: " + palabra + " es distinta a la palabra " + nuevapalabra + ". No son palíndromos.")

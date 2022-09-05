# Version beta 1.0.0

text1 = input('Dime la primera cadena de texto: ')
text2 = input('Dime la segunda cadena de texto: ')
contador = 0
lista = []
index = []
lista2 = []
index2 = []

if len(text1) > len(text2):
    contador = len(text1)
else:
    contador = len(text2)

def conparar(text1, text2):
    for i in range(contador):
        letra1 = text1[i:i+1]
        letra2 = text2[i:i+1]
        if letra1 == letra2:
            result = 'Correcto las dos cadenas coinciden '
        else:
            index.append(i+1)
            lista.append(letra1)

        if letra2 == letra1:
            result = 'Correcto las dos cadenas coinciden '
        else:
            index2.append(i+1)
            lista2.append(letra2)
    for i in range(len(index)):
        print(f'\nLa posicion {index[i]} de la cadena 1 el error es "{lista[i]}" pues no conicide con la 2')
    for i in range(len(index2)):
        print(f'\nLa posicion {index2[i]} de la cadena 2 el error es "{lista2[i]}" pues no conicide con la 1')
    if len(index) == 0:
        print(result)

conparar(text1, text2)

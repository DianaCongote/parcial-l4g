texto_palabras = 'El Universo es todo lo que podemos tocar, sentir, percibir, medir o detectar. Abarca los cosas vivas, los planetas, las estrellas, las galaxias, las nubes de polvo, la luz e incluso el tiempo.'

quitar=", : ; . ! ¡"

for puntos in quitar:
    texto_palabras=texto_palabras.replace(puntos," ")
texto_palabras = texto_palabras.lower()
cadena_palabras = texto_palabras.split()
a=cadena_palabras
h=0
contar = []
for i in cadena_palabras:
    contar.append(cadena_palabras.count(i))
    h=h+1
b=contar
for k in range(h):
    print(a[k] + " = " + str(b[k]))
    

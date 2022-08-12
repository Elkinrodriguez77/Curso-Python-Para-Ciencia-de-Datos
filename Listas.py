# Listas son un tipo de dato en python

ciudades = ["Bogotá", "Medellin", "Buenos Aires", "Santiago de Chile"]

print(ciudades)

# LLamar elementos dentro de la lista:

# Es un lenguaje de base 0

print(ciudades[-1])

# conocer la cantidad de elementos de una lista:

longitud_lista = len(ciudades)
print(longitud_lista)

#Insertar elementos en una lista: 

ciudades.append("La paz")

print(ciudades)

# Elimino elementos a mi lista:

print(f"La ciudad eliminada de la lista es: {ciudades.pop(-2)}")


# Ejemplo 2

numeros = [45, 15, 30, 5, 1, 101]

print(numeros)

print(sorted(numeros))

# número mínimo y máximo de mi lista:

print(max(numeros))
print(min(numeros))

# eliminar registros / elementos de mi lista:

numeros.remove(15)

print(numeros)


# unir dos listas en una:

numeros.extend(ciudades)

print(numeros)


 #listas dentro de una lista:

Nombres_Apellidos = [["Elkin", "Rodriguez"], ["Paola", "Arévalo"], ["Patricia", "Escamilla"]]

print(Nombres_Apellidos[1][1])


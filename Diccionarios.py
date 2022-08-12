# Diccionarios que es un tipo de dato en python

Estudiante = {'Nombre': 'Laura', 'Edad': 28, 'Materias': ['Python', 'SQL']}

print(Estudiante)

# Consultar partes de mi diccionario:

print(Estudiante['Materias'][0])

# Consultar las llaves que componen mi diccionario:

print(Estudiante.keys())

# Las claves que están asociadas a cada una de las llaves:

print(Estudiante.values())

#reemplazar valores de mis llaves:

Estudiante['Nombre'] = 'Marcela'

print(Estudiante)

# Agregar 

Estudiante['Jornada'] = 'Nocturna'

print(Estudiante)

# Eliminar una variable de mi diccionario:

del(Estudiante['Jornada'])

print(Estudiante)


# Otro metodos que puedo implementar con los diccionarios:

##Dict > representar por ejemplo una tupla como un diccionario:

diccionario = dict(a = 1, b = 2, c = 3)

print(diccionario)

# zip 

diccionario2 = dict(zip('abc', [1,2,3]))

print(diccionario2)

# clear 

diccionario2.clear()

print(diccionario2)


diccionario2 = diccionario.copy()

print(diccionario2)


# JSON (JavaScript Object Notation):

Estudiante = {
    'Nombre': 'Laura', 
    'Edad': 28, 
    'Materias': ['Python', 'SQL']
    }

Valor_get = Estudiante.get('Nombre')

print(Valor_get)

# pop 

Valor_pop = Estudiante.pop('Edad')

print(Valor_pop)

print(Estudiante)
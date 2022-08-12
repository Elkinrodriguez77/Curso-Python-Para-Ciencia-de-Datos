"""Condicionales
1. Estructura básica
2. Condicional anidado
3. Uso de AND/OR dentro del condicional
"""

# 1. Estructura básica del condicional

Name = 'Isabel'
Age = 30
Es_Mayor_de_edad = True

if Age >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


#2 condicional anidado

if Name == 'Elkin':
    print(f"Si, su nombre es {Name}")
elif Name == 'Juan':
    print("Si, su nombre es Juan")
elif Name == 'Paola':
    print("Si, su nombre es Paola")
else:
    print("No es ninguno de los nombres relacionados")
    if Name == 'Mario':
        print("Si, su nombre es Mario")

#3 Uso del AND y el OR:

if Name == 'Elkin' or Es_Mayor_de_edad == True:
    print ("Se cumple una de las condiciones") #uso de or
    #print ("Se cumplen ambas condiciones") # uso de and
else:
    print ("No se cumple ninguna de las condiciones")



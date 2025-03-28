# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 19:19:25 2025

@author: LENOVO
"""

import numpy as np

lista_nombres = ["Sofía", "Mateo", "Isabella", "Lucas", "Valentina", "Alejandro", "Emma", "Santiago", "Martina",
                 "Sebastián", "Camila", "Nicolás", "Valeria", "Gabriel", "Antonella", "Daniel", "Lucía", "Andrés",
                 "Renata", "Adrián", "Sara", "Diego", "Julieta", "Joaquín", "Paula", "Leonardo", "Victoria", "Benjamín",
                 "María", "Samuel", "Amelia", "David", "Elena", "Maximiliano", "Montserrat", "Ángel", "Regina", "Tomás",
                 "Jimena", "Cristóbal", "Fernanda", "Bruno", "Ana", "Ricardo", "Ximena", "Gael", "Andrea", "Matías", "Carolina",
                 "Thiago", "Daniela", "Emilio", "Alicia", "Jerónimo", "Natalia", "Dylan", "Claudia", "Iker", "Patricia",
                 "Iván", "Alejandra", "Alan", "Laura", "Franco", "Gabriela", "Jesús", "Mariana", "Rodrigo", "Lorena", "Martín",
                 "Melissa", "Juan", "Paola", "Carlos", "Diana", "Pedro", "Carmen", "Miguel", "Rosa", "Jorge", "Gloria", "Luis",
                 "Silvia", "Antonio", "Isabel", "José", "Esther", "Manuel", "Beatriz", "Francisco", "Raquel", "Javier", "Susana",
                 "Raúl", "Pilar", "Alberto", "Eva", "Enrique", "Dolores", "Sergio", "Mercedes", "Óscar", "Cristina", "Julio",
                 "Rosario"]

dict_users = {}

for i_name in lista_nombres:
    dict_users[i_name.lower()] = {
        'saldo': np.random.randint(10000, 500000),
        'contraseña': str(np.random.randint(1000, 9999))  # Genera contraseña de 4 dígitos
    }

str_nombre = ''

for enu, i_name in enumerate(lista_nombres):
    str_nombre = str_nombre + f'\n{enu}: ' + i_name

while True:
    try:
        seleccion = int(input(f'¿Usted quién es?: {str_nombre}\n105: SALIR\n'))
    except ValueError:
        print('Selección inválida')
        continue

    if seleccion == 105:
        break
    elif 0 <= seleccion < len(lista_nombres):
        seleccion_cliente = lista_nombres[seleccion].lower()  # Usar nombres en minúsculas para coincidir con las claves del diccionario
        
        while True:
            contraseña_ingresada = input('Ingrese su contraseña de 4 dígitos: ')
            if contraseña_ingresada == dict_users[seleccion_cliente]['contraseña']:
                break
            else:
                print('Contraseña incorrecta. Intente de nuevo.')
        
        while True:
            operaciones = int(input('¿Qué quiere hacer?:\n0: Ver\n1: Retirar\n2: Consignar\n3: SALIR\n'))
            saldo_cuenta_usuario = dict_users[seleccion_cliente]['saldo']

            if operaciones == 0:
                print(saldo_cuenta_usuario)
            elif operaciones == 1:
                valor_retiro = int(input('¿Cuánto quiere retirar?: '))
                if valor_retiro <= saldo_cuenta_usuario:
                    print('Retiro exitoso')
                    dict_users[seleccion_cliente]['saldo'] = saldo_cuenta_usuario - valor_retiro
                    print('Su saldo es:', dict_users[seleccion_cliente]['saldo'])
                else:
                    print('Saldo insuficiente')
            elif operaciones == 2:
                valor_consignar = int(input('¿Cuánto quiere consignar?: '))
                dict_users[seleccion_cliente]['saldo'] = saldo_cuenta_usuario + valor_consignar
                print('Consignación exitosa. Su nuevo saldo es:', dict_users[seleccion_cliente]['saldo'])
            elif operaciones == 3:
                break
            else:
                print('Operación no válida')
    else:
        print('Error: no seleccionó una opción válida')
 
print('Rama alternativo')
 
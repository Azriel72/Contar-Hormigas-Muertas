'''
    Autor: Juan Manuel Abréu
    Fecha: 16-05-2024
    Descripción: Contar las hormigas muertas en un texto. 
    
    - Se asume que el cuerpo completo de una hormiga es 'ant' 
      donde 't' es la cabeza, 'n' el cuerpo y 'a' la cola.
'''

import re

ant_text = "...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t"

def count_dead_ants(text: str):
    ''' Esta función cuenta las hormigas muertas en un texto. '''
    text = text.strip(".")
    text = re.split("\.+", text)
    dead_ants = 0
    for word in text:
        if word != "ant":
            match = re.search('^(?!.*ant).*$', word)
            if match:
                debris = match.group(0)  # Obtiene los escombros de hormigas
                if 't' in debris:  # Si 't' se encuentra en los escombros, incrementa el contador de hormigas muertas
                    dead_ants += 1
    return dead_ants

print(count_dead_ants(ant_text))

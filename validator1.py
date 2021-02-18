import os
#import os.path
import platform
#try:
def validar(NombreArchivo):
    ###Validar que el archivo existe
    if os.path.exists(NombreArchivo):
        if str(platform.system()) == 'Darwin' or str(platform.system())=='Linux':
            cadena = 'python3 '+NombreArchivo
            c = os.system(cadena)
        if str(platform.system()) == 'Windows':
            cadena = 'python '+NombreArchivo
            c = os.system(cadena)
    ##Si el archivo no existe regresar 300
    else:
        c = 300
    return c
#c = validar('pruebaTurtle.py')
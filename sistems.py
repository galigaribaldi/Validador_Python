###Informacion del usuario
import os
import sys
import socket
from getpass import getuser
from datetime import date, datetime
import platform
####Script principal sobre la informaicon del usuario que trae ifno del usuario
def user_information(option):
    listaDatos = []
    
    if option > 0:
        if str(platform.system()) == 'Darwin' or str(platform.system())=='Linux':
            from subprocess import call
            call('clear')
        if str(platform.system()) == 'Windows':
            from subprocess import call
            call('cls')
        print("Directorio de Ejecucion: ", os.getcwd())
        print("Tipo de sistema operativo: ", platform.system())
        print("Nombre del sistema operativo: ", sys.platform)
        print("Nombre de la versión: ", sys.version)
        print("Versión de python que se ejecuta: ", platform.python_version())
        print("Direccion ip de ejecución: ", socket.gethostbyname(socket.gethostname()))
        print("Usuario que ejecuta el programa: ", getuser())
        print("Fecha sin hora: ", date.today())
        print("Fecha con hora: ", datetime.now())
        
    listaDatos.append(str(os.getcwd()));listaDatos.append(str(platform.system()));listaDatos.append(str(platform.system()))
    listaDatos.append(str(sys.version));listaDatos.append(str(platform.python_version())); listaDatos.append(str(socket.gethostbyname(socket.gethostname())))
    listaDatos.append(str(getuser()));listaDatos.append(str(date.today())); listaDatos.append(str(datetime.now()))
    #print(listaDatos)
    return listaDatos
user_information(1)
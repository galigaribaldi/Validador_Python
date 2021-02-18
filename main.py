from correos import enviar_correo_PDF
from txtGenerator import txt
from validator1 import validar
nombrePrograma = 'pruebaTurtle.py'
try:
    c = validar(nombrePrograma)
    print(c)
    #input()
    if c == 256:
        opcion = int(input("Tu porgrama Falla en algùn punto\nPresiona 1 para enviar correo o presiona otra tecla para salir>> "))
        if opcion ==1:
            nombre = 'calificacion_'+nombrePrograma+'_.txt'
            txt(nombre, opcion)
            print("Tu programa ha fallado pero tu calificacion se ha guardad")            
            enviar_correo_PDF('galigaribaldi70@gmail.com', 'Calificacion No exitosa',nombre )
    if c == 300:
        opcion = int(input("El nombre ingresado en tu programa no existe\nPresiona 1 para enviar correo o presiona otra tecla para salir>> "))
        if opcion ==1:
            nombre = 'calificacion_'+nombrePrograma+'_.txt'
            txt(nombre, opcion)
            print("Tu programa ha fallado pero tu calificacion se ha guardado")
            enviar_correo_PDF('galigaribaldi70@gmail.com', 'Calificacion No exitosa',nombre )            
    if c == 0:
        opcion = 0
        nombre = 'calificacion_'+nombrePrograma+'_.txt'
        txt(nombre, opcion)
        print("Completado con exito! La calificacion se actualziará!")
        enviar_correo_PDF('galigaribaldi70@gmail.com', 'Calificacion Exitosa',nombre )        
except Exception as e:
    print("Fallo inesperado, intentalo nuevamente", e)
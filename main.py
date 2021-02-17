from correos import enviar_correo_PDF
from txtGenerator import txt
nombre = 'Nombre.txt'
txt(nombre)
enviar_correo_PDF('galigaribaldi70@gmail.com', 'Calificacion',nombre )
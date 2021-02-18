class Master:
    def enviar_correo_PDF(self, correo_destinatario, asunto,nombre_PDF):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders
        remitente = 'govnocyk@gmail.com'
        destinatarios = []
        destinatarios.append(correo_destinatario)
        asunto = asunto
        cuerpo = "Comprobacion de calificacion"
        ruta_adjunto = nombre_PDF
        nombre_adjunto = nombre_PDF
        # Creamos el objeto mensaje
        mensaje = MIMEMultipart()
        # Establecemos los atributos del mensaje
        mensaje['From'] = remitente
        mensaje['To'] = ", ".join(destinatarios)
        mensaje['Subject'] = asunto
        # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        # Abrimos el archivo que vamos a adjuntar
        archivo_adjunto = open(ruta_adjunto, 'rb')
        # Creamos un objeto MIME base
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        # Y le cargamos el archivo adjunto
        adjunto_MIME.set_payload((archivo_adjunto).read())
        # Codificamos el objeto en BASE64
        encoders.encode_base64(adjunto_MIME)
        # Agregamos una cabecera al objeto
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        # Y finalmente lo agregamos al mensaje
        mensaje.attach(adjunto_MIME)
        # Creamos la conexión con el servidor
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        # Ciframos la conexión
        sesion_smtp.starttls()
        # Iniciamos sesión en el servidor
        sesion_smtp.login('govnocyk@gmail.com','gyka9912')
        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()
        # Enviamos el mensaje
        try:
            sesion_smtp.sendmail(remitente, destinatarios, texto)
        except:
            print("No se Pudo enviar el Correo a:")
        # Cerramos la conexión
        sesion_smtp.quit()
        
    def txt(self, NombreTitulo, opcion):
        from sistems import user_information
        valor = user_information(1)
        titulo = str(NombreTitulo)
        f = open (titulo,'w')
        for i in valor:
            f.write(i+'\n')
        if opcion != 0:
            f.write("Status: Fallido, checar revision")
        else:
            f.write("Status: Completado, checar revision")
        f.close()
    
    def validar(self, NombreArchivo):
        import os
        import platform    
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
    def main(self, nombrePrograma):
        try:
            c = self.validar(nombrePrograma)
            print(c)
            #input()
            if c == 256:
                opcion = int(input("Tu porgrama Falla en algùn punto\nPresiona 1 para enviar correo o presiona otra tecla para salir>> "))
                if opcion ==1:
                    nombre = 'calificacion_'+nombrePrograma+'_.txt'
                    self.txt(nombre, opcion)
                    print("Tu programa ha fallado pero tu calificacion se ha guardad")            
                    self.enviar_correo_PDF('galigaribaldi70@gmail.com', 'Calificacion No exitosa',nombre )
            if c == 300:
                opcion = int(input("El nombre ingresado en tu programa no existe\nPresiona 1 para enviar correo o presiona otra tecla para salir>> "))
                if opcion ==1:
                    nombre = 'calificacion_'+nombrePrograma+'_.txt'
                    self.txt(nombre, opcion)
                    print("Tu programa ha fallado pero tu calificacion se ha guardado")
                    self.enviar_correo_PDF('galigaribaldi70@gmail.com', 'Calificacion No exitosa',nombre )            
            if c == 0:
                opcion = 0
                nombre = 'calificacion_'+nombrePrograma+'_.txt'
                self.txt(nombre, opcion)
                print("Completado con exito! La calificacion se actualziará!")
                self.enviar_correo_PDF('galigaribaldi70@gmail.com', 'Calificacion Exitosa',nombre )        
        except Exception as e:
            print("Fallo inesperado, intentalo nuevamente", e)

if __name__ =='__main__':
    nombrePrograma = 'pruebaTurtle.py'
    m = Master()
    m.main(nombrePrograma)
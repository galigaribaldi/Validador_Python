from sistems import user_information
def txt(NombreTitulo, opcion):
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
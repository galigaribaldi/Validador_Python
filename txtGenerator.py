from sistems import user_information
def txt(NombreTitulo):
    valor = user_information(1)
    titulo = str(NombreTitulo)
    f = open (titulo,'w')
    for i in valor:
        f.write(i+'\n')
    f.close()
import os
#try:
c = os.system('python3 pruebaTurtle.py')
if c ==0:
    print("Validación terminada! completado")
#except Exception as e:
else:
    #error = str(e)
    #c = 1
    print("El codigo no corrio debido al error: ", c)
#print(c)
#if c == 0:
#else:
    
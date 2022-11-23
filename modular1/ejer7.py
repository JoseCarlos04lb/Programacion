'''
Created on Nov 17, 2022

@author: estudiante
'''








listadomino=[4,6]
listadomino2=[3,4]
def encaja (listadomino=[], listadomino2=[]):
    mensaje=""
    print(listadomino)
    print(listadomino2)
    if (listadomino[-1]==listadomino2[0])or (listadomino2[-1] ==listadomino[0]):
        mensaje="encaja"
    else:
        mensaje="no encaja"
    return mensaje
print(encaja(listadomino,listadomino2))
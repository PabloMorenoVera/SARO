#!/usr/bin/python3

D_usuario = {}

fd = open("/etc/passwd")

linea = fd.readline()
while linea != '':
    linea_troceada = linea.split(':')

    if linea_troceada[0] == 'pablo':
        print('Usuario:', linea_troceada[0], 'consola:', linea_troceada[-1])
        #Opcional1
        D_usuario[linea_troceada[0]] = linea_troceada[-1]

    #Opcional2
    if linea_troceada[0] == 'root':
        print('Usuario_root:', linea_troceada[0], 'consola_root:', linea_troceada[-1])

    linea=fd.readline()

fd.close()

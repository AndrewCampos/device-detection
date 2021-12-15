# Bibliotecas
from PIL import Image as img
import numpy as np
import util as u
import os

metric_andrew = 0
metric_bien = 0
metric_wash = 0
dp_andrew = 0
dp_bien = 0
dp_wash = 0
dim = 2000
error = 0

print('--------------------------------------\n' + u.BOLD
    + '          CAMERA IDENTIFIER\n' + u.RESET
    + '--------------------------------------')

sign = img.open('sign_andrew_2-5.jpeg')
sign = sign.convert(mode="L")
pattern_andrew = np.asarray(sign)

sign = img.open('sign_bien_2-5.jpeg')
sign = sign.convert(mode="L")
pattern_bien = np.asarray(sign)

sign = img.open('sign_wash_2-5.jpeg')
sign = sign.convert(mode="L")
pattern_wash = np.asarray(sign)

avg = img.open('avg_andrew.jpeg')
avg = avg.convert(mode="L")
grayM_andrew = np.asarray(avg)

avg = img.open('avg_bien.jpeg')
avg = avg.convert(mode="L")
grayM_bien = np.asarray(avg)

avg = img.open('avg_wash.jpeg')
avg = avg.convert(mode="L")
grayM_wash = np.asarray(avg)

print(u.RESET + 'Analysing photos')
for i in range(1,31):
    path = '/home/andrew/Documentos/Unifesp/Segurança/testes/IMG_' + str(i) + '.jpg'
    photo = img.open(path)
    photo = photo.convert(mode="L")
    photo_data = np.asarray(photo)
    for col in range(dim):
        for row in range(dim):

            if pattern_andrew[col][row] == u.BLACK:
                dp_andrew += 1
                metric_andrew += abs(int(photo_data[col][row]) - int(grayM_andrew[col][row]))

            if pattern_bien[col][row] == u.BLACK:
                dp_bien += 1
                metric_bien += abs(int(photo_data[col][row]) - int(grayM_bien[col][row]))

            if pattern_wash[col][row] == u.BLACK:
                dp_wash += 1
                metric_wash += abs(int(photo_data[col][row]) - int(grayM_andrew[col][row]))

    metric_andrew = metric_andrew/dp_andrew
    metric_bien = metric_bien/dp_bien
    metric_wash = metric_wash/dp_wash

    

    if metric_andrew < metric_bien:
        if metric_andrew < metric_wash:
            print('Match: ' + u.GREEN + 'Andrew     - ' + u.RESET,end='')
            match = 2
        else:
            print('Match: ' + u.GREEN + 'Washington - ' + u.RESET,end='')
            match = 3
    else:
        if metric_bien < metric_wash:
            print('Match: ' + u.GREEN + 'André      - ' + u.RESET,end='')
            match = 1
        else:
            print('Match: ' + u.GREEN + 'Washington - ' + u.RESET,end='')
            match = 3

    if i < 11:
        print('Photo ' + str(i) + ': André')
        if match != 1:
            print(u.BRED + 'MISMATCH' + u.RESET)
            error += 1
        else:
            print(u.BGREEN + 'MATCH' + u.RESET)
    elif i < 21:
        print('Photo ' + str(i-10) + ': Andrew ')
        if match != 2:
            print(u.BRED + 'MISMATCH' + u.RESET)
            error += 1
        else:
            print(u.BGREEN + 'MATCH' + u.RESET)
    else:
        print('Photo ' + str(i-20) + ' Washington ')
        if match != 3:
            print(u.BRED + 'MISMATCH' + u.RESET)
            error += 1
        else:
            print(u.BGREEN + 'MATCH' + u.RESET)

print('')
print(u.BOLD + 'End Of Execution!' + u.RESET)
print('Accuracy: ' + u.GREEN + str(100*((30-error)/30)) + '%' + u.RESET)
# Bibliotecas
from PIL import Image as img
import numpy as np
import util as u
import os

# Inicializa variáveis
dim = 2000
total_images = 60
total_pixels = 2000**2
avg = 0
miss_pixel = 0
alpha = 2
signature = np.zeros((dim,dim))

print('--------------------------------------\n' + u.BOLD
    + '           SIGNATURE MAKER\n' + u.RESET
    + '--------------------------------------')

for item in range(1,61):
    try:
        path = "/home/andrew/Documentos/Unifesp/Segurança/fotos-andrew/IMG_" + str(item) + ".jpg"
        print(u.YELLOW + 'Open image: IMG_' + str(item) + '.jpg',end='\r')
        photo = img.open(path)
    except:
        print(u.BRED + "Can't open image '" + path + "1")
        continue
    photo = photo.convert(mode="L")
    data = np.asarray(photo)

    for col in range(dim):
        for row in range(dim):
            signature[col][row] += data[col][row]

print(u.RESET + '\nMaking average image')
for col in range(dim):
    for row in range(dim):
        signature[col][row] = signature[col][row]/total_images
        avg += signature[col][row]

avg_img = img.fromarray(signature)
avg_img = avg_img.convert(mode="L")
avg_img.save('avg-img.jpeg',format="JPEG")

avg = avg/total_pixels
st_dev = np.std(signature)
i_min = avg - (st_dev*alpha)
i_max = avg + (st_dev*alpha)

print('Making signature')
for col in range(dim):
    for row in range(dim):
        if signature[col][row] < i_min or signature[col][row] > i_max:
            signature[col][row] = u.BLACK
            miss_pixel += 1
        else:
            signature[col][row] = u.WHITE

result = img.fromarray(signature)
result = result.convert(mode='L')
result.save("sign_andrew_2.jpeg",format="JPEG")

print(u.BGREEN + 'End of execution!' + u.RESET)
print('Standard deviation: ' + u.CYAN + str(st_dev) + u.RESET)
print('Average: ' + u.CYAN + str(avg) + u.RESET)
print('Hot/Dead pixels: ' + u.CYAN + str(miss_pixel) + u.RESET)
print('Normal pixels: ' + u.CYAN + str(dim**2 - miss_pixel) + u.RESET)

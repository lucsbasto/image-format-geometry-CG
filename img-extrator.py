def getType(img):
    print (img)
    if (img == '6677'):
        print ("Imagem: BMP - Identificação: Sim")
    else:
        print ("Imagem: null - Identificação: Não")


def get_h_w(bytes):
    w = 0
    h = 0
    for b in range(len(bytes)):
        if (b >= 18 and b < 22):
            h += bytes[b]
        if (b >= 22 and b < 26):
            w += bytes[b]

    print("height: ", h)
    print("width: ", w)

img = open('imagem.bmp', 'rb')
img_big = open('The_death.bmp', 'rb')
img_big_read = img_big.read()
img_read = img.read()
two_pos = str(img_read[0]) + str(img_read[1])
two_pos = str(img_big_read[0]) + str(img_big_read[1])

getType(two_pos) #passar as duas primeiras posições
get_h_w(bytearray(img_big_read)) #passar a o imagem.read()
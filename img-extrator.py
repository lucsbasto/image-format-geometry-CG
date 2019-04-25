def getType(img):
    if (img == '6677' or img == b'BM'):
        print ("Imagem: BMP - Identificação: Sim")
    else:
        print ("Imagem: null - Identificação: Não")


def get_height_width(bytes):
    height = img[18]
    width = img[22]
    print("height: ", height)
    print("width: ", width)


file = open('imagem.bmp', 'rb')
img = file.read()
size = len(img)
type = img[:2]
header = img[:14]

print (size)
getType(type)
get_height_width(img)

#funciona apenas para imagem com heigth e width menores que 256
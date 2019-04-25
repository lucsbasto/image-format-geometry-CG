def getType(img):
    if (img == '6677' or img == b'BM'):
        print ("Imagem: BMP - Identificação: Sim")
    else:
        print ("Imagem: null - Identificação: Não")


def get_height_width(bytes):
    height = img[18]
    width = img[22]
    if (height < 255 and img[19] != 0):
        height = 256 + height
    if(width < 255 and img[23] != 0):
        width = 256 + width
    print("height: ", height)
    print("width: ", width)


file = open('imagem.bmp', 'rb')
img = file.read()
size = len(img)
type = img[:2]

getType(type)
get_height_width(img)


def getType(img):
    if (img == '6677' or img == b'BM'):
        print ("Imagem: BMP - Identificação: Sim")
    else:
        print ("Imagem: null - Identificação: Não")


def get_height_width(bytes):
    width = img[18]
    height = img[22]
    if (width < 255 and img[19] != 0):
        width = 256 + width
    if(height < 255 and img[23] != 0):
        height = 256 + height
    print("height: ", height)
    print("width: ", width)


file = open('imagem.bmp', 'rb')
img = file.read()
size = len(img)
type = img[:2]

getType(type)
get_height_width(img)
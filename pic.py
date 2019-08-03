from PIL import Image

def Pic(file):
    pil_im = Image.open(file +'.jpg').convert('L')
    box = (600, 0, 700, 1024)
    region = pil_im.crop(box)
    region.show()
    print('..............')
    print('..............')


Pic('cap/cat0')

import cv2
from PIL import Image

img = Image.open("mask.png")

# pixels = img.load() # create the pixel map

def func (im):
    newimdata = []
    redcolor = (255,0,0)
    greencolor = (0,255,0)
    blackcolor = (0,0,0)
    for color in im.getdata():
        if color == redcolor:
            newimdata.append( redcolor )
        elif color == greencolor:
            newimdata.append(greencolor)
        else:
            newimdata.append( blackcolor )
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

func(img).save("_mask.png")

# pixels = list(img.getdata())
# i=0
# j=0
# for n in range(img.size[0] * img.size[1]): # for every pixel:
#     if pixels[n] != (255, 0, 0) or pixels[n] != (0, 255, 0):
#         # change to black if not red
#         img.putpixel((i, j), (0, 0, 0))
#     j+=1
#     if j == 3000:
#         i+=1
#         j=0
# img.show()
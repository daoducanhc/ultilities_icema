import cv2
import numpy as np
import torchvision.transforms as transforms
import torchvision.transforms.functional as TF

def tensor_to_PIL(tensor):
    image = tensor.cpu().clone()
    image = image.squeeze(0)
    image = transforms.ToPILImage()(image)
    return image

img = cv2.imread('0.png')
img = TF.to_tensor(img)
crop = transforms.RandomCrop((768,768)).get_params(img, (768,768))
print(crop)
img = tensor_to_PIL(img)
x = crop[0] if crop[0]+crop[2] < 1464 else 0
y = crop[1] if crop[1]+crop[3] < 1008 else 0
print(x, y)
img = img.crop((x, y, x+crop[2], y+crop[3]))
img.show()

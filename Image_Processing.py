
#adaptive histogram equilisation - clahe - contrast limited adaptive histogram equilisation
#Image enhancement
import cv2
#read the image
img = cv2.imread('crime.png')
#prepare for applying clahe
clahe = cv2.createCLAHE()
#conver to black and white - grey scale image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#apply enhancement process
enh = clahe.apply(grey_img)
#save it to a file
cv2.imwtite('enhanced.png',enh_img)
print('Done Enhancing')


'''
from PIL import Image
#opening the image
img = Image.open('obtained.png')
#transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
#save it to a file in a human understandable format
transposed_img.save('corrected.png')
print('Done flipping')
'''

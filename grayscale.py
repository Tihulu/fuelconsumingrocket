from PIL import Image as image
#https://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.Image.convert
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def jpgtopng(pic_jpg):
	im = image.open(pic_jpg)
	im.save('foto.png')
def greyconverter(pic_png):
	R=[]
	G=[]
	B=[]
	gray=[]
	l=len(img)
	gimg=img

	R = np.array(gimg[:, :, 0])
	G = np.array(gimg[:, :, 1])
	B = np.array(gimg[:, :, 2])
	gray=(0.2989*R + 0.5870*G + 0.1140*B)
	#gray=(R+G+B)/3
	#print (gray)
	gimg[:,:,0]=gray
	gimg[:,:,1]=gray
	gimg[:,:,2]=gray
	#imggray = image.fromarray(gimg)
	#imggray.save("gray.png")
	plt.imshow(gimg)
	plt.savefig('gray.png')
	plt.show()

imgloc=str(input("Image file png or jpg (type with the extension ex: a.png): "))
a=imgloc.split(".")
imgtype=a[1]
if imgtype=='png':
#	pic_png=str(input('file location:'))
	pic_png=imgloc
	img=mpimg.imread(pic_png)
	greyconverter(pic_png)
if imgtype=='jpg' :
#	pic_jpg=str(input('file location:'))
	pic_jpg=imgloc
	jpgtopng(pic_jpg)
	img=mpimg.imread('foto.png')
	greyconverter('foto.png')

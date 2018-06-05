from PIL import Image, ImageDraw 
from random import randint		
from re import findall
def stega_encrypt():	
	
	keys = []
	img = Image.open(input("path to image: ")) 
	draw = ImageDraw.Draw(img)	   
	width = img.size[0]  		   
	height = img.size[1]		   
	pix = img.load()

	f = open('keys.txt','w')
	for i,elem in enumerate([ord(elem) for elem in input("text here: ")]):
		key = (randint(1,width-10),randint(1,height-10))		
		g, b = pix[key][1:3]
		draw.point(key, (elem,g , b))														
		f.write(str(key)+'\n')								
	
	print('keys were written to the keys.txt file')
	img.save("image.png", "PNG")
	f.close()
												
stega_encrypt()











"""
open_img  = open('image.jpg','a')
open_img.write('---'+str(input('text: '))+'---')
open_img.close()

open_img  = open('image.jpg','rb')
print('| '+re.sub('---',' || ',''.join(re.findall(r'---(.+)---',str(open_img.read()))))+' |')

####################
def decimal_to_binary(event):
	return [int(format(ord(elem),'b')) for elem in event]


def binary_to_decimal(event):
	return [chr(int(str(elem),2)) for elem in event]

"""
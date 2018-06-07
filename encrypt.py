from PIL import Image, ImageDraw 
from random import randint		


def stega_encrypt():	
	
	keys = [] 					#сюда будут помещены ключи
	img = Image.open(input("path to image: ")) 	#создаём объект изображения
	draw = ImageDraw.Draw(img)	   		#объект рисования
	width = img.size[0]  		   		#ширина
	height = img.size[1]		   		#высота	
	pix = img.load()				#все пиксели тут
	f = open('keys.txt','w')			#текстовый файл для ключей

	for elem in ([ord(elem) for elem in input("text here: ")]):
		key = (randint(1,width-10),randint(1,height-10))		
		g, b = pix[key][1:3]
		draw.point(key, (elem,g , b))														
		f.write(str(key)+'\n')								
	
	print('keys were written to the keys.txt file')
	img.save("newimage.png", "PNG")
	f.close()
												
stega_encrypt()

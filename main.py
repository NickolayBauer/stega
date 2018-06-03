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
		draw.point(key, (elem, 10, 10))														
		f.write(str(key)+'\n')								
	
	print('keys were written to the keys.txt file')
	img.save("image.png", "PNG")
	f.close()
												
	
def stega_decrypt():
	a = []						    
	keys = []
	img = Image.open("image.png")				
	pix = img.load()

	f = open(input('path to keys: '),'r')
	
	y = str([line.strip() for line in f])																		
	for i in range(len(findall(r'\((\d+)\,',y))):
		keys.append((int(findall(r'\((\d+)\,',y)[i]),int(findall(r'\,\s(\d+)\)',y)[i]))) 	
	for key in keys:
		a.append(pix[tuple(key)][0])							
	return ''.join([chr(elem) for elem in a])	

stega_encrypt()
print("you message: ",stega_decrypt())



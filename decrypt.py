from PIL import Image 		
from re import findall

def stega_decrypt():
	
	a = []						    
	keys = []
	img = Image.open(input("path to image: "))				
	pix = img.load()
	f = open(input('path to keys: '),'r')
	y = str([line.strip() for line in f])				
															
	for i in range(len(findall(r'\((\d+)\,',y))):
		keys.append((int(findall(r'\((\d+)\,',y)[i]),int(findall(r'\,\s(\d+)\)',y)[i]))) 	
	for key in keys:
		a.append(pix[tuple(key)][0])							
	return ''.join([chr(elem) for elem in a])	


print("you message: ",stega_decrypt())




import os
from PIL import Image
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


if __name__ == '__main__':

    isExists=os.path.exists("./Temp")
    if not isExists:
        os.makedirs("./Temp")
	
	list = ["Default-568h@2x~iphone.png,640,1136","Default-667h.png,750,1134","Default-736h.png,1242,2208",
	        "Default-2436h.png,1125,2436","Default-Portrait@2x~ipad.png,1536,2048","Default-Portrait~ipad.png,768,1024",
	        "Default@2x~iphone.png,320,480","Default@2x~universal~anyany.png,2732,2732","Default~iphone.png,320,480",
	        "android-logo.png,1080,1920","android-2048.png,2048,2048"]
	file_in = 'bg_logo.png'
	for x in list:
		str = x.split(",")
		w = int(str[1])
		h = int(str[2])
		name = str[0]
		produceImage(file_in, w, h, "Temp/"+name)
		

	    

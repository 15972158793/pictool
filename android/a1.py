import os
from PIL import Image
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


if __name__ == '__main__':

    isExists=os.path.exists("./android_res")
    if not isExists:
        os.makedirs("./android_res")
	list = ["icon-16.png,16,16","icon-32.png,32,32","icon-64.png,64,64",
            "icon-128.png,128,128","icon-256.png,256,256","icon-512.png,512,512",
            "loading-logo.png,64,64"]
	file_in = 'icon.png'
	for x in list:
		str = x.split(",")
		w = int(str[1])
		h = int(str[2])
		name = str[0]
		produceImage(file_in, w, h, "android_res/"+name)
	    

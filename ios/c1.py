import os
from PIL import Image
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


if __name__ == '__main__':

    isExists=os.path.exists("./result")
    if not isExists:
        os.makedirs("./result")
	list = ["icon-29.png,29,29","icon-50@2x.png,100,100","icon-83.5@2x.png,167,167","icon-1024.png,1024,1024","icon-29@2x.png,48,48",
"icon-60@2x.png,120,120","icon-86@2x.png,172,172","icon-20.png,20,20","icon-29@3x.png,87,87","icon-60@3x.png,180,180","icon-98@2x.png,196,196",
"icon-20@2x.png,40,40","icon-40.png,40,40","icon-72.png,72,72","icon.png,57,57","icon-20@3x.png,60,60","icon-40@2x.png,80,80","icon-72@2x.png,144,144",
"icon@2x.png,114,114","icon-24@2x.png,48,48","icon-44@2x.png,88,88","icon-76.png,76,76","icon-27.5@2x.png,55,55","icon-50.png,50,50","icon-76@2x.png,152,152"]
	file_in = 'icon.png'
	for x in list:
		str = x.split(",")
		w = int(str[1])
		h = int(str[2])
		name = str[0]
		produceImage(file_in, w, h, "result/"+name)
    
    isExists=os.path.exists("./construct3")
    if not isExists:
        os.makedirs("./construct3")
	list = ["icon-16.png,16,16","icon-64.png,64,64","icon-114.png,114,114","icon-128.png,128,128",
	"icon-256.png,256,256","icon-512.png,512,512","icon-32.png,32,32","loading-logo.png,64,64"]
	file_in = 'icon.png'
	for x in list:
		str = x.split(",")
		w = int(str[1])
		h = int(str[2])
		name = str[0]
		produceImage(file_in, w, h, "construct3/"+name)
	    

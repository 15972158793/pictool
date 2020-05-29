import os
from PIL import Image
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)

if __name__ == '__main__':
    
    list1 = ["app_icon_144.png,144,144","app_icon_72.png,72,72","app_icon_36.png,36,36",
		    "app_icon_48.png,48,48","app_icon_96.png,96,96","app_icon_192.png,192,192",
		    "app_icon_round_144.png,144,144","app_icon_round_72.png,72,72","app_icon_round_36.png,36,36",
		    "app_icon_round_48.png,48,48","app_icon_round_96.png,96,96","app_icon_round_192.png,192,192"]
    file_in = 'icon.png'
    for x in list1:
		str1 = x.split(",")
		w = int(str1[1])
		h = int(str1[2])
		name = str1[0]
		produceImage(file_in, w, h, "res/"+name)

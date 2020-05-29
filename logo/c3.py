import os
from PIL import Image

def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)

def pasteImage(s):
    str1 = s.split(",")
    scale = float(str1[3])
    w = int(str1[1])
    h = int(str1[2])
    name = str1[0]
    file = "Temp/" + name
    bg = Image.open(file)

    file_in = 'logo.png'
    logo = Image.open(file_in)
    logoW,logoH = logo.size
    logo1 = logo.resize((int(logoW*scale),int(logoH*scale)),Image.ANTIALIAS)
	# left top
    position = ((int((w-logoW*scale)/2), int((h-logoH*scale)/2)))
    r,g,b,a = logo1.convert("RGBA").split()
    # new image
    out_img = Image.new('RGBA',(w,h),(0,0,0,0))
    out_img.paste(bg,(0,0))
    out_img.paste(logo1,position,mask=a)
    #out_img = out_img.resize((w, h), Image.ANTIALIAS)
    #out_img = out_img.convert("RGBA")
    out_img.save("LaunchImage/"+name)

if __name__ == '__main__':

    isExists=os.path.exists("./LaunchImage")
    if not isExists:
        os.makedirs("./LaunchImage")
    #
	list = ["Default-568h@2x~iphone.png,640,1136,0.4",
	        "Default-667h.png,750,1134,0.4",
	        "Default-736h.png,1242,2208,0.8",
	        "Default-2436h.png,1125,2436,0.7",
	        "Default-Portrait@2x~ipad.png,1536,2048,1",
	        "Default-Portrait~ipad.png,768,1024,0.4",
	        "Default@2x~iphone.png,320,480,0.2",
	        "Default@2x~universal~anyany.png,2732,2732,1.2",
	        "Default~iphone.png,320,480,0.2",
            "android-logo.png,1080,1920,0.7",
            "android-2048.png,2048,2048,1"]
	
	for x in list:
	    pasteImage(x)
	
        
		
	    

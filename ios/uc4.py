import os
from PIL import Image
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)

if __name__ == '__main__':
    isExists=os.path.exists("./unity_icon")
    if not isExists:
        os.makedirs("./unity_icon")
    list1 = ["Icon-Store-1024.png,1024,1024",
			"Icon-iPad-76.png,76,76",
			"Icon-iPad-152.png,152,152",
			"Icon-iPad-167.png,167,167",
			"Icon-iPad-Notification-20.png,20,20",
			"Icon-iPad-Notification-40.png,40,40",
			"Icon-iPad-Settings-29.png,29,29",
			"Icon-iPad-Settings-58.png,58,58",
			"Icon-iPad-Spotlight-40.png,40,40",
			"Icon-iPad-Spotlight-80.png,80,80",
			"Icon-iPhone-120.png,120,120",
			"Icon-iPhone-180.png,180,180",
			"Icon-iPhone-Notification-40.png,40,40",
			"Icon-iPhone-Notification-60.png,60,60",
			"Icon-iPhone-Settings-29.png,29,29",
			"Icon-iPhone-Settings-58.png,58,58",
			"Icon-iPhone-Settings-87.png,87,87",
			"Icon-iPhone-Spotlight-80.png,80,80",
			"Icon-iPhone-Spotlight-120.png,120,120"]
    file_in = 'unity_icon.png'
    for x in list1:
		str1 = x.split(",")
		w = int(str1[1])
		h = int(str1[2])
		name = str1[0]
		produceImage(file_in, w, h, "unity_icon/"+name)

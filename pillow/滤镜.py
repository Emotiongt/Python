from PIL import Image
from PIL import ImageFilter

imga=Image.open('4.jpg')

w,h=imga.size

img_output=Image.new('RGB',(2*w,h))
img_output.paste(imga,(0,0))

fltrs=[]                                         #建立空滤镜列表
fltrs.append(ImageFilter.EDGE_ENHANCE)           #边缘强化滤镜
fltrs.append(ImageFilter.FIND_EDGES)             #查找边缘滤镜
fltrs.append(ImageFilter.GaussianBlur(4))        #高斯模糊滤镜
for fltr in fltrs:
    r=imga.filter(fltr)
    img_output.paste(r,(w,0))
    img_output.show()

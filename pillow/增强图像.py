from PIL import Image
from PIL import ImageEnhance

image=Image.open("4.jpg")

w,h=image.size

img_output=Image.new('RGB',(2*w,h))      #建立用于对比的新图像
img_output.paste(image,(0,0))

nhc=ImageEnhance.Color(image)            #建立图像色彩调整器
nhb=ImageEnhance.Brightness(image)       #建立图像亮度调整器
nhc=ImageEnhance.Sharpness(image)        #建立图像清晰度调整器
nhd=ImageEnhance.Contrast(image)         #建立图像对比度调整器
for nh in [nhc,nhb,nhc,nhd]:
    for ratio in [0.6,1.8]:              #使用减弱和增强两种系数
        b=nh.enhance(ratio)
        img_output.paste(b,(w,0))        #粘贴调整后的图像
        img_output.show()

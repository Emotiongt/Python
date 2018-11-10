from PIL import Image
#使用blend混合图像
imga=Image.open('1.jpg')
imgb=Image.open('2.jpg')
Image.blend(imga,imgb,0.5).show()

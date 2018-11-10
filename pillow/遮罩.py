from PIL import Image
#遮罩功能
imga=Image.open('2.jpg')
imgb=Image.open('3.jpg')
mask=Image.open('3.png')
Image.composite(imga,imgb,mask).show()

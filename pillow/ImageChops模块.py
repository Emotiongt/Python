from PIL import Image
from PIL import ImageChops
imga=Image.open('8.jpg')
imgb=Image.open('4.jpg')

#ImageChops.add(imga,imgb,1,0).show()          #像素相加
#ImageChops.subtract(imga,imgb,1,0).show()     #像素相减
#ImageChops.darker(imga,imgb).show()           #变暗（像素较小的被保留）
#ImageChops.lighter(imga,imgb).show()          #变亮
#ImageChops.multiply(imga,imgb).show()         #正片叠底
#ImageChops.screen(imga,imgb).show()           #屏幕
#ImageChops.invert(imga).show()                #反相
#ImageChops.difference(imga,imgb).show()       #比较
ImageChops.constant(imga,100).show()          #灰度填充

from PIL import Image
from PIL import ImageChops

imga=Image.open('4.jpg')
print('图像格式',imga.format)
print('图像模式',imga.mode)
print('图像尺寸',imga.size)
print('图像通道列表',imga.getbands())

imgb=imga.copy()                #复制图像image
imgb.thumbnail((224,168))       #生成图像的缩略图
#imgb.show()

imgc=imga.copy()
region=imgb.crop((50,50,120,120))   #裁剪出一块区域
imgc.paste(region,(130,130))        #将裁剪出区域粘贴到图像imgc
#imgc.show()

img_output=Image.new('RGB',(800,500))   #创建新图像
img_output.paste(imgb,(0,0))
#img_output.show()
b=imgb.convert('CMYK')
img_output.paste(b,(224,0))
#img_output.show()

flip=b.transpose(Image.FLIP_LEFT_RIGHT) #得到一幅左右镜像的图像
img_output.paste(flip,(224,0))
#img_output.show()

b=imgb.convert('L')                     #转换图像为灰度图
img_output.paste(b,(224,0))
#img_output.show()

b=ImageChops.offset(imgb,30)              #对图像移位
img_output.paste(b,(224,0))
#img_output.show()

b=imgb.rotate(45)                       #旋转图像
img_output.paste(b,(224,0))
#img_output.show()

#imgc=Image.open('3.jpg')
#chnls=imgc.split()                      #分离图像通道
#b=Image.merge('RGB',chnls[::-1])        #合并RB互换后的通道
#img_output.paste(b,(224,0))
#img_output.show()

from PIL import ImageFilter
b=imgb.filter(ImageFilter.GaussianBlur) #对图片运用滤镜(高斯模糊)
img_output.paste(b,(224,0))
#img_output.show()

chnls=imgb.split()
r,g,b=chnls
r_after=r.point(lambda i:i if i<100 else 255)  #处理R通道每个像素
b=Image.merge('RGB',(r_after,g,b))
img_output.paste(b,(224,0))
img_output.show()

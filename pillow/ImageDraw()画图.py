from PIL import Image
from PIL import ImageDraw

a=Image.new('RGB',(200,200),'white')              #创建一个背景为白色的图像
drw=ImageDraw.Draw(a)                             #创建绘图对象
drw.rectangle((50,50,150,150),outline='red')      #绘制矩形
drw.text((60,60),"My First Draw",fill='green')    #绘制文本
a.show()

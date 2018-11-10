#使用eval()对每个像素应用函数
from PIL import Image
def div2(v):
    return v//2
imga=Image.open('3.jpg')
Image.eval(imga,div2).show()

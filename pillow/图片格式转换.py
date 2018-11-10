import os
from PIL import Image
import tkinter
import tkinter.filedialog
import tkinter.messagebox
#创建窗口
class Window:
    def __init__(self):
        self.root=root=tkinter.Tk()
        label=tkinter.Label(root,text='选择目录')
        label.place(x=5,y=5)
        self.entry=tkinter.Entry(root)
        self.entry.place(x=60,y=5)
        self.buttonBrowser=tkinter.Button(root,text="浏览",command=self.Browser)
        self.buttonBrowser.place(x=210,y=5)
        frameF=tkinter.Frame(root)
        frameF.place(x=5,y=30)
        frameT=tkinter.Frame(root)
        frameT.place(x=100,y=30)
        self.fImage=tkinter.StringVar()            #生成关联变量
        self.tImage=tkinter.StringVar()
        self.status=tkinter.StringVar()
        self.fImage.set('.bmp')
        self.tImage.set('.bmp')
        labelFrom=tkinter.Label(frameF,text='From')
        labelFrom.pack(anchor='w')
        labelTo=tkinter.Label(frameT,text='to')
        labelTo.pack(anchor='w')
        frBmp=tkinter.Radiobutton(frameF,variable=self.fImage,value='.bmp',text='BMP')
        frBmp.pack(anchor='w')
        frJpg=tkinter.Radiobutton(frameF,variable=self.fImage,value='.jpg',text='JPG')
        frJpg.pack(anchor='w')
        frGif=tkinter.Radiobutton(frameF,variable=self.fImage,value='.gif',text='GIF')
        frGif.pack(anchor='w')
        frPng=tkinter.Radiobutton(frameF,variable=self.fImage,value='.png',text='PNG')
        frPng.pack(anchor='w')
        frBmp=tkinter.Radiobutton(frameT,variable=self.tImage,value='.bmp',text='BMP')
        frBmp.pack(anchor='w')
        frJpg=tkinter.Radiobutton(frameT,variable=self.tImage,value='.jpg',text='JPG')
        frJpg.pack(anchor='w')
        frGif=tkinter.Radiobutton(frameT,variable=self.tImage,value='.gif',text='GIF')
        frGif.pack(anchor='w')
        frPng=tkinter.Radiobutton(frameT,variable=self.tImage,value='.png',text='PNG')
        frPng.pack(anchor='w')
        self.buttonConv=tkinter.Button(root,text='转换',command=self.Conv)
        self.buttonConv.place(x=80,y=160)
        self.labelStatus=tkinter.Label(root,textvariable=self.status)
        self.labelStatus.place(x=50,y=195)
    def MainLoop(self):                          #进入消息循环
        self.root.minsize(250,220)
        self.root.maxsize(250,220)
        self.root.mainloop()
    def Browser(self):                           #浏览目录
        directory=tkinter.filedialog.askdirectory(title='Python')
        if directory:
            self.entry.delete(0,tkinter.END)
            self.entry.insert(tkinter.END,directory)
    def Conv(self):                              #转换文件格式
        n=0
        t=self.tImage.get()
        f=self.fImage.get()
        path=self.entry.get()
        if path=='':
            tkinter.messagebox.showerror('Python tkinter','请输入路径')
            return
        filenames=os.listdir(path)
        os.mkdir(path+'/'+t[-3:])
        for filename in filenames:
            if filename[-4:]==f:
                Image.open(path+'/'+filename).save(path+'/'+t[-3:]+'/'+filename[:-4]+t)
                n=n+1
        self.status.set('成功转换%d张图片' % n)
window=Window()
window.MainLoop()
        

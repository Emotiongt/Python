import os
from PIL import Image
import tkinter
import tkinter.filedialog
import tkinter.messagebox

class Window:
    def __init__(self):
        self.root=root=tkinter.Tk()
        self.Image=tkinter.StringVar()
        self.status=tkinter.StringVar()
        self.mstatus=tkinter.IntVar()                #关联是否批量转换
        self.fstatus=tkinter.IntVar()                #关联是否改变文件格式
        self.Image.set('bmp')
        self.mstatus.set(0)
        self.fstatus.set(0)
        label=tkinter.Label(root,text='输入百分比')
        label.place(x=5,y=5)
        self.entryNew=tkinter.Entry(root)
        self.entryNew.place(x=70,y=5)
        self.checkM=tkinter.Checkbutton(root,text='批量转换',command=self.OnCheckM,variable=self.mstatus,onvalue=1,offvalue=0)
        self.checkM.place(x=5,y=30)
        label=tkinter.Label(root,text='选择文件')
        label.place(x=5,y=55)
        self.entryFile=tkinter.Entry(root)
        self.entryFile.place(x=60,y=55)
        self.buttonBrowserFile=tkinter.Button(root,text='浏览',command=self.BrowserFile)
        self.buttonBrowserFile.place(x=200,y=55)
        label=tkinter.Label(root,text='选择目录')
        label.place(x=5,y=80)
        self.entryDir=tkinter.Entry(root,state=tkinter.DISABLED)
        self.entryDir.place(x=60,y=80)
        self.buttonBrowserDir=tkinter.Button(root,text='浏览',command=self.BrowserDir,state=tkinter.DISABLED)
        self.buttonBrowserDir.place(x=200,y=80)
        self.checkF=tkinter.Checkbutton(root,text='改变文件格式',command=self.OnCheckF,variable=self.fstatus,onvalue=1,offvalue=0)
        self.checkF.place(x=5,y=110)
        frame=tkinter.Frame(root)
        frame.place(x=10,y=130)
        labelTo=tkinter.Label(frame,text='To')
        labelTo.pack(anchor='w')
        self.rBmp=tkinter.Radiobutton(frame,variable=self.Image,value='bmp',text='BMP',state=tkinter.DISABLED)
        self.rBmp.pack(anchor='w')
        self.rJpg=tkinter.Radiobutton(frame,variable=self.Image,value='jpg',text='JPG',state=tkinter.DISABLED)
        self.rJpg.pack(anchor='w')
        self.rGif=tkinter.Radiobutton(frame,variable=self.Image,value='gif',text='GIF',state=tkinter.DISABLED)
        self.rGif.pack(anchor='w')
        self.rPng=tkinter.Radiobutton(frame,variable=self.Image,value='png',text='PNG',state=tkinter.DISABLED)
        self.rPng.pack(anchor='w')
        self.buttonConv=tkinter.Button(root,text='转换',command=self.Conv)
        self.buttonConv.place(x=100,y=175)
        self.labelStatus=tkinter.Label(root,textvariable=self.status)
        self.labelStatus.place(x=80,y=205)
    def MainLoop(self):
        self.root.minsize(250,270)
        self.root.maxsize(250,250)
        self.root.mainloop()
    def BrowserDir(self):                             #选择路径
        directory=tkinter.filedialog.askdirectory(title='Python')
        if directory:
            self.entryDir.delete(0,tkinter.END)
            self.entryDir.insert(tkinter.END,directory)
    def BrowserFile(self):                            #选择文件
        file=tkinter.filedialog.askopenfilename(title='Python Music Player',filetypes=[('JPG','*.jpg'),('BMP','*.bmp'),('GIF','*.gif'),('PNG','*.png')])
        if file:
            self.entryFile.delete(0,tkinter.END)
            self.entryFile.insert(tkinter.END,file)
    def OnCheckM(self):                               #设置组件状态
        if not self.mstatus.get():
            self.entryDir.config(state=tkinter.DISABLED)
            self.entryFile.config(state=tkinter.NORMAL)
            self.buttonBrowserDir.config(state=tkinter.DISABLED)
            self.buttonBrowserFile.config(state=tkinter.NORMAL)
        else:
            self.entryDir.config(state=tkinter.NORMAL)
            self.entryFile.config(state=tkinter.DISABLED)
            self.buttonBrowserDir.config(state=tkinter.NORMAL)
            self.buttonBrowserFile.config(state=tkinter.DISABLED)
    def OnCheckF(self):                               #设置组件状态
        if not self.fstatus.get():
            self.rBmp.config(state=tkinter.DISABLED)
            self.rJpg.config(state=tkinter.DISABLED)
            self.rGif.config(state=tkinter.DISABLED)
            self.rPng.config(state=tkinter.DISABLED)
        else:
            self.rBmp.config(state=tkinter.NORMAL)
            self.rJpg.config(state=tkinter.NORMAL)
            self.rGif.config(state=tkinter.NORMAL)
            self.rPng.config(state=tkinter.NORMAL)
    def Conv(self):                                   #转换图片
        n=0
        if self.mstatus.get():
            path=self.entryDir.get()
            if path=='':
                tkinter.messagebox.showerror('Python tkinter','请输入路径')
                return
            filenames=os.listdir(path)
            if self.fstatus.get():
                f=self.Image.get()
                for filename in filenames:
                    if filename[-3:] in ('bmp','jpg','gif','png'):
                        self.make(path+'/'+filename,f)
                        n=n+1
            else:
                for filename in filenames:
                    if filename[-3:] in ('bmp','jpg','gif','png'):
                        self.make(path+'/'+filename)
                        n=n+1
        else:
            file=self.entryFile.get()
            if file=='':
                tkinter.messagebox.showerror('Python tkinter','请输入路径')
                return
            if self.fstatus.get():
                f=self.Image.get()
                self.make(file,f)
                n=n+1
            else:
                self.make(file)
                n=n+1
        self.status.set('成功转换%d张图片' % n)
    def make(self,file,f=None):                       #生成缩略图
        im=Image.open(file)
        mode=im.mode
        if mode not in ('L','RGB'):
            im=im.convert('RGB')
        width,height=im.size
        s=self.entryNew.get()
        if s=='':
            tkMessageBox.showerror('Python tkinter','请输入百分比')
            return
        else:
            n=int(s)
        nwidth=int(width*n/100)
        nheight=int(height*n/100)
        thumb=im.resize((nwidth,nheight),Image.ANTIALIAS)
        if f:
            thumb.save(file[:(len(file)-4)]+'_thumb.'+f)
        else:
            thumb.save(file[:(len(file)-4)]+'_thumb'+file[-4:])
window=Window()
window.MainLoop()
        
            

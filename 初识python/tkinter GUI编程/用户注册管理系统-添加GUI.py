#添加GUI编程
try:
    from tkinter import *
    from tkinter.messagebox import *
    import pymysql.cursors
    from traceback import *
    from datetime import datetime
    root=Tk()
    #设置初始化窗口大小
    root.geometry('600x300')
    systitle='用户注册信息管理系统'
    #设置系统标题
    root.title(systitle)

    pic=PhotoImage(file=r'1.gif')
    #载入图片作为背景
    label1=Label(image=pic)
    label1.place(x=0,y=0)

    mainframe=LabelFrame()
    mainframe.pack()
    def showall():
        global mainframe
        try:
            
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='spring', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor=connection.cursor()
            cursor.execute("select * from tuser")
            users=cursor.fetchall()
            connection.close()
            mainframe.destroy()           #删除已有用户界面
            if len(users)==0:
                showwarning(systitle,'当前无注册用户')
            else:
                mainframe=LabelFrame(text='当前已注册用户信息如下: ')
                mainframe.pack(anchor=CENTER,pady=20,ipadx=5,ipady=5)
                mainframe.columnconfigure(1,minsize=80)
                mainframe.columnconfigure(2,minsize=200)
                mainframe.columnconfigure(3,minsize=200)
                Label(mainframe,text='序号',font=('隶书',15,'bold'),bd=1,relief=SOLID).grid(row=1,column=1,sticky=N+E+S+W)
                Label(mainframe,text='用户名',font=('隶书',15,'bold'),bd=1,relief=SOLID).grid(row=1,column=2,sticky=N+E+S+W)
                Label(mainframe,text='密码',font=('隶书',15,'bold'),bd=1,relief=SOLID).grid(row=1,column=3,sticky=N+E+S+W) 
                rn=2
                for x in users:
                    Label(mainframe,text=str(rn-1),font=('宋体',14),bd=1,relief=SOLID).grid(row=rn,column=1,sticky=N+E+S+W)
                    Label(mainframe,text=x.get('name'),font=('宋体',14),bd=1,relief=SOLID).grid(row=rn,column=2,sticky=N+E+S+W)
                    Label(mainframe,text=x.get('password'),font=('宋体',14),bd=1,relief=SOLID).grid(row=rn,column=3,sticky=N+E+S+W)
                    rn+=1
        except Exception as ex:
            showerror(systitle,'数据库访问出错: %s' % ex)
            raise ex
    def check_update():
        try:
            global mainframe
            mainframe.destroy()
            mainframe=LabelFrame(text='查找、修改或删除用户:')
            mainframe.pack(anchor=CENTER,pady=20,ipadx=5,ipady=5)

            tf=LabelFrame(mainframe,text="查找用户: ")
            tf.pack(anchor=CENTER,pady=10,ipadx=5,ipady=5)
            Label(tf,text="请输入要查找的用户id: ",anchor=E).grid(row=1,column=1)
            userid=StringVar()
            txtuid=Entry(tf,textvariable=userid)
            txtuid.grid(row=1,column=2)
            btok=Button(tf,text="确定")
            btok.grid(row=1,column=3)

            editframe=LabelFrame(mainframe,text='删除或修改用户数据: ')
            editframe.pack(anchor=CENTER,pady=20,ipadx=5,ipady=5)

            btdel=Button(editframe,text="删除用户",state=DISABLED)
            btdel.pack(anchor=NW)

            op=LabelFrame(editframe,text='修改用户: ')
            op.pack(anchor=CENTER,pady=10,ipadx=5,ipady=5)

            Label(op,text="新用户 ID:",anchor=E).grid(row=1,column=1)
            newuserid=StringVar()
            newtxtuid=Entry(op,textvariable=newuserid)
            newtxtuid.grid(row=1,column=2)
            Label(op,text='新密码: ',anchor=E).grid(row=2,column=1,sticky=E)
            newpassword=StringVar()
            newtxtpwd=Entry(op,textvariable=newpassword)
            newtxtpwd.grid(row=2,column=2)

            bteditsave=Button(op,text='保存修改',state=DISABLED)
            bteditsave.grid(row=1,column=3,rowspan=2,sticky=N+E+S+W)

            def dofind():
                uname=userid.get()
                if find(uname)==-1:
                    showinfo(systitle,'%s 还未注册! ' % uname)
                else:
                    btdel.config(state=NORMAL)
                    bteditsave.config(state=NORMAL)
            def dodelete():
                uname=userid.get()
                if askokcancel('用户注册信息管理系统',"确认删除用户: %s? " % uname):
                    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='spring', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
                    cursor=connection.cursor()
                    cursor.execute('delete from tuser where name=%s',(uname,))
                    connection.commit()
                    connection.close()
                    showinfo(systitle,'成功删除用户: %s' % uname)
            def saveedit():
                uname=userid.get()
                newname=newuserid.get()
                if newname=='':
                    showerror(systitle,'新的用户名输入错误: %s' % newname)
                    newtxtuid.focus_set()
                else:
                    if find(newname)==1:
                        showerror(systitle,'你输入的用户名 %s 已经使用' % newname)
                        newtxtuid.focus_set()
                    else:
                        pwd=newpassword.get()
                        if pwd=='':
                            showerror(systitle,'你输入的密码无效!')
                            newtxtuid.focus_set()
                        else:
                            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='spring', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
                            cursor=connection.cursor()
                            cursor.execute('update tuser set name=%s,password=%s where name=%s',(newname,pwd,uname))
                            connection.commit()
                            connection.close()
                            showinfo(systitle,'已成功修改用户数据!')
            btok.config(command=dofind)
            btdel.config(command=dodelete)
            bteditsave.config(command=saveedit)
        except Exception as ex:
            print('\t 数据库访问出错: ',ex)
            showerror(systitle,'数据库访问出错: %s' % ex)
            raise ex
    def adduser():
        try:
            global mainframe
            mainframe.destroy()
            mainframe=LabelFrame(text='添加新用户:')
            mainframe.pack(anchor=CENTER,pady=20,ipadx=5,ipady=5)

            tf=Frame(mainframe)
            tf.pack()
            Label(tf,text='用户ID： ',anchor=E).grid(row=1,column=1)
            userid=StringVar()
            txtuid=Entry(tf,textvariable=userid)
            txtuid.grid(row=1,column=2)
            Label(tf,text='密码: ',anchor=E).grid(row=2,column=1,sticky=E)
            password=StringVar()
            txtpwd=Entry(tf,textvariable=password)
            txtpwd.grid(row=2,column=2)

            tf2=Frame(mainframe)
            tf2.pack()
            btclear=Button(tf2,text="重置")
            btclear.grid(row=1,column=1)
            btok=Button(tf2,text="保存")
            btok.grid(row=1,column=2)

            def clearall():
                userid.set('')
                password.set('')
            def savenew():
                uname=userid.get()
                pwd=password.get()
                if uname=='':
                    showerror(systitle,'用户名输入无效!')
                else:
                    if find(uname)==1:
                        showerror(systitle,'你输入的用户名已经使用,请重新添加用户')
                        txtuid.focus()
                    else:
                        if pwd=='':
                            showerror(systitle,'登录密码输入无效!')
                        else:
                            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='spring', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
                            cursor=connection.cursor()
                            cursor.execute('insert into tuser(name,password) values(%s,%s)',(uname,pwd))
                            connection.commit()
                            connection.close()
                            showinfo(systitle,'已成功添加用户! ')
            btclear.config(command=clearall)
            btok.config(command=savenew)
        except Exception as ex:
            print('\t 数据库访问出错: ',ex)
            raise ex
    def find(namekey):
        try:
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='spring', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor=connection.cursor()
            cursor.execute('select * from tuser where name=%s',(namekey,))
            user=cursor.fetchall()
            if len(user)>0:
                n=1
            else:
                n=-1
            connection.close()
            return n
        except Exception as ex:
            showerror(systitle,'数据库访问出错: %s' % ex)
            raise ex
    def resetdb():
        try:
            global mainframe
            mainframe.destroy()
            msg='该操作将删除所有已注册用户数据,\n请确认是否继续?'
            if askokcancel('用户注册信息管理系统',msg):
                connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='spring', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
                cursor=connection.cursor()
                cursor.execute('drop table if exists tuser')
                cursor.execute('create table tuser(name varchar(40) primary key,password varchar(40))')
                connection.close()
                showinfo(systitle,'已成功重置用户数据库')
        except Exception as ex:
            showerror(systitle,'数据库访问出错 : %s' % ex)
            raise ex
    def goexit():
        if askokcancel('用户注册信息管理系统','请确认退出系统?'):
            root.destroy()

            
        
    menubar=Menu(root)              #创建Menu对象menubar，作为root窗口子菜单
    root.config(menu=menubar)       #将menubar菜单作为root窗口的顶层菜单栏
    file=Menu(menubar,tearoff=0)    #file将作为menubar菜单的子菜单
    file.add_command(label='创建/重置用户数据库',command=resetdb)
    file.add_separator()
    file.add_command(label='显示全部已注册用户',command=showall)
    file.add_command(label='查找/修改/删除用户信息',command=check_update)
    file.add_command(label='添加新用户',command=adduser)
    file.add_separator()
    file.add_command(label='退出',command=goexit)
    menubar.add_cascade(label='系统操作菜单',menu=file)
    
except Exception as ex:
    from traceback import print_tb
    from datetime import datetime
    log=open(r'D:\text\log.txt','w')
    x=datetime.today()
    print('\n出错了: ')
    print('日期时间: ',x)
    print('异常信息: ',ex)
    print('堆栈跟踪信息:')
    print_tb(ex.__traceback__)
    
    print('\n 出错了: ',file=log)
    print('日期时间: ',x,file=log)
    print('异常信息: ',ex.args[0],file=log)
    print('堆栈跟踪信息: ',file=log)
    print_tb(ex.__traceback__,file=log)
    log.close()
    print('发生了错误，系统已退出')
    

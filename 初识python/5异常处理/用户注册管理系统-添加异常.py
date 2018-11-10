#添加异常处理
try:
    from pickle import dump,load
    class user:
        def __init__(self,uname=None,pwd=None):
            self.uname=uname
            self.pwd=pwd
        def update(self,uname,pwd):
            self.uname=uname
            self.pwd=pwd
        def __repr__(self):
            return 'username=%s \tpassword=%s' % (self.uname,self.pwd)
    def showall():
        global userlist
        if len(userlist)==0:
            print('\t 当前无注册用户')
        else:
            print('\t 当前已注册用户信息如下:')
            n=0
            for x in userlist:
                n+=1
                print('t%s. ' % n,x)
            input('\n\t 按Enter键结束\n')
    def check_update():
        global userlist
        uname=input('\t 请输入要查找的用户名')
        index=find(uname)
        if index==-1:
            print('\t%s 不存在!' % uname)
        else:
            print('\t%s 已经注册!'% uname)
            print('\t请选择操作:')
            print('\t 1.修改用户')
            print('\t 2.删除用户')
            op=input('\t 请输入序号选择相应操作:')
            if op=='2':
                del userlist[index]
                print('\n\t 已成功删除用户!')
            else:
                uname=input('\t 请输入新的用户名:')
                if uname=='':
                    print('\t 用户名输入无效!')
                else:
                    if find(uname)>-1:
                        print('\t 你输入的用户名已经使用!')
                    else:
                        pwd=input('\t 请输入新用户登录密码:')
                        if pwd=='':
                            print('\t 登录密码输入无效')
                        else:
                            userlist[index].update(uname,pwd)
                            print('\n\t已成功修改用户')
        input('\n\t 按Enter键继续...\n')
    def adduser():
        global userlist
        uname=input('\t 请输入新的用户名:')
        if uname=='':
            print('\t用户名输入无效')
        else:
            if find(uname)>-1:
                print('\t你输入的用户名已经使用,请重新添加用户!')
            else:
                pwd=input('\t请输入新用户登录密码:')
                if pwd=='':
                    print('\t登录密码输入无效!')
                else:
                    userlist.append(user(uname,pwd))
                    print('\t已成功添加用户!')
        input('\n\t按Enter键结束...')
    def find(namekey):
        global userlist
        n=-1
        for x in userlist:
            n+=1
            if x.uname==namekey:
                break
        else:
            n=-1
        return n
    def save():
        global userlist
        myfile=open(r'D:\text\userdata.txt','w')
        global userlist
        dump(userlist,myfile)
        myfile.close()
        print('\t已成功保存用户信息')
        input('\n\t按Enter键继续...')
    myfile=open(r'D:\text\userdata.txt','r')
    x=myfile.read(1)
    if x=='':
        userlist=list()
    else:
        myfile.seek(0)
        userlist=load(myfile)
    myfile.close()
    while True:
        print('用户注册信息管理系统')
        print('\t1. 显示全部已注册用户')
        print('\t2. 查找/修改/删除用户信息')
        print('\t3. 添加新用户')
        print('\t4. 保存用户数据')
        print('\t5. 退出系统')
        no=input('请输入序号选择对应菜单:')
        if no=='1':
            showall()
        elif no=='2':
            check_update()
        elif no=='3':
            adduser()
        elif no=='4':
            save()
        elif no=='5':
            print('谢谢使用，系统已退出')
            break
except Exception as ex:
    from traceback import print_tb        #导入print_tb打印堆栈跟踪信息
    from datetime import datetime         #导入日期时间类，为日志文件写入当前时间
    #打开日志文件
    log=open(r'D:\text\log.txt','w')
    x=datetime.today()
    print('\n出错了: ')
    print('日期时间: ',x)
    print('异常信息: ',ex)
    print('堆栈跟踪信息:')
    print_tb(ex.__traceback__)
   #将异常日志信息写入文件 
    print('\n 出错了: ',file=log)
    print('日期时间: ',x,file=log)
    print('异常信息: ',ex.args[0],file=log)
    print('堆栈跟踪信息: ',file=log)
    print_tb(ex.__traceback__,file=log)
    log.close()
    print('发生了错误，系统已退出')
    

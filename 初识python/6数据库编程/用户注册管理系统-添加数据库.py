#添加数据库
try:
    def showall():
        try:
            import pymysql.cursors                 #导入模块
            #连接数据库
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='spring', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            #创建游标
            cursor=connection.cursor()
            #查询所有用户
            cursor.execute("select * from tuser")
            users=cursor.fetchall()
            if len(users)==0:
                print('\t 当前无注册用户')
            else:
                print('\t 当前已注册用户信息如下:')
                n=0
                for x in users:
                    print('\t ',x.get('name'),end='\t')
                    print('\t ',x.get('password'),end='\t')
            connection.close()
            input('\n\t 按Enter键结束\n')
        except Exception as ex:
            print('\t 数据库访问出错: ',ex)
            raise ex
    def check_update():
        try:
            import pymysql.cursors
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='spring', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor=connection.cursor()
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
                    cursor.execute('delete from tuser where name=%s',(uname,))
                    connection.commit()
                    print('\n\t 已成功删除用户!')
                else:
                    newname=input('\t 请输入新的用户名:')
                    if newname=='':
                        print('\t 用户名输入无效!')
                    else:
                        if find(newname)==1:
                            print('\t 你输入的用户名已经使用!')
                        else:
                            pwd=input('\t 请输入新用户登录密码:')
                            if pwd=='':
                                print('\t 登录密码输入无效')
                            else:
                                cursor.execute('update tuser set name=%s,password=%s where name=%s',(newname,pwd,uname))
                                connection.commit()
                                print('\n\t已成功修改用户')
            connection.close()
            input('\n\t 按Enter键继续...\n')
        except Exception as ex:
            print('\t 数据库访问出错: ',ex)
            raise ex
    def adduser():
        try:
            import pymysql.cursors
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='spring', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor=connection.cursor()
            uname=input('\t 请输入新的用户名:')
            if uname=='':
                print('\t用户名输入无效')
            else:
                if find(uname)==1:
                    print('\t你输入的用户名已经使用,请重新添加用户!')
                else:
                    pwd=input('\t请输入新用户登录密码:')
                    if pwd=='':
                        print('\t登录密码输入无效!')
                    else:
                        cursor.execute('insert into tuser(name,password) values(%s,%s)',(uname,pwd))
                        connection.commit()
                        print('\t已成功添加用户!')
            connection.close()
            input('\n\t按Enter键结束...')
        except Exception as ex:
            print('\t 数据库访问出错: ',ex)
            raise ex
    def find(namekey):
        try:
            import pymysql.cursors
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
            print('\t 数据库访问出错: ',ex)
            raise ex
    def resetdb():
        try:
            import pymysql.cursors
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='spring', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor=connection.cursor()
            cursor.execute('drop table if exists tuser')
            cursor.execute('create table tuser(name varchar(40) primary key,password varchar(40))')
            connection.close()
            print('\t已成功重置用户数据库')
            input('\n\t 按Enter键继续...')
        except Exception as ex:
            print('\t 数据库访问出错: ',ex)
            raise ex
        
    while True:
        print('用户注册信息管理系统')
        print('\t1. 显示全部已注册用户')
        print('\t2. 查找/修改/删除用户信息')
        print('\t3. 添加新用户')
        print('\t4. 创建/重置用户数据库')
        print('\t5. 退出系统')
        no=input('请输入序号选择对应菜单:')
        if no=='1':
            showall()
        elif no=='2':
            check_update()
        elif no=='3':
            adduser()
        elif no=='4':
            resetdb()
        elif no=='5':
            print('谢谢使用，系统已退出')
            break
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
    

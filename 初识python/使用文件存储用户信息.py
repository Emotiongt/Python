users=[]
users.append({'id':'admin','pwd':'135@$^'})
users.append({'id':'guest','pwd':'123'})
users.append({'id':'python','pwd':'123456'})
print('代码中创建的账户信息列表如下:')
print(users)
myfile=open(r'D:\python.txt','wb')
import pickle
pickle.dump(users,myfile)              #将列表对象写入文件
myfile.close()
print('账户信息已经写入文件')
myfile=open(r'D:\python.txt','rb')
x=pickle.load(myfile)                  #存储文件对象
print(x)

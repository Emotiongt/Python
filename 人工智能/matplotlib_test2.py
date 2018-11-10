import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-np.pi,np.pi,256,endpoint=True)
plt.figure(figsize=(8,6),dpi=80)              #创建一个8*6点的(point)的图，并设置分辨率为80
plt.subplot(2,2,1)
C,S=np.cos(X),np.sin(X)
plt.plot(X,C)
plt.plot(X,S)
plt.subplot(2,2,2)
C,S=np.cos(X),np.sin(X)
plt.plot(X,C,color="blue",linewidth=1.0,linestyle="-")
plt.plot(X,S,color="green",linewidth=1.0,linestyle="--")

plt.xlim(-4.0,4.0)                            #横轴上下限       
plt.xticks(np.linspace(-4,4,9,endpoint=True))  #横轴记号
plt.ylim(-1.0,1.0)                
plt.yticks(np.linspace(-1,1,5,endpoint=True))
plt.savefig("test2.png",dpi=72)                #以72分辨率来保存图片
plt.subplot(2,1,2)
plt.plot(X,C,color="blue",linewidth=1.0,linestyle="-",label="cosine")
plt.plot(X,S,"r--",label="sine")
plt.xlim(X.min()*1.1,X.max()*1.1)              #更合理的上下限
#更合理的记号
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
plt.ylim(C.min()*1.1,C.max()*1.1)   
plt.yticks([-1,0,1])
ax=plt.gca()                                   #脊柱(上下左右)
ax.spines['right'].set_color('none')           #使右边不可见
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))   #下脊柱移到数据空间零点
ax.spines['left'].set_position(('data',0))
plt.legend(loc='upper left')                   #添加图例
 
t = 2*np.pi/3                                  #为特殊点做注释
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=2.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
         xy=(t, np.cos(t)), xycoords='data',
         xytext=(-90, -50), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.show()

import matplotlib.pyplot as plt
import numpy as np
#angle 是方向盘当前角度(°)
def angleToradius(angle):
    si=np.deg2rad(angle/16)
    cotsi=1/np.tan(si)
    cots0=17/28+cotsi
    tans0=1/cots0
    s0=np.arctan(tans0)
    undernum=np.tan((si+s0)/2)
    radius=2.8/undernum
    return radius
    

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
print("最小转向半径：",angleToradius(470))#最大方向盘转向角(°)，输出最小转向半径(m)
cur=[]
lenv=[]
ve=20/3.6
for i in range(1,470):
    cu=angleToradius(i)
    cur.append(cu)
    v = ve*cu/(cu-1.7/2)
    lenv.append(v)
plt.ylabel("路径上的曲率")
plt.xlabel("路径长度的变化率")
plt.plot(lenv,cur)
plt.show()
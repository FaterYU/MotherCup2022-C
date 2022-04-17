import numpy as np
import matplotlib.pyplot as plt
import csv
aa = 20
aat = []
# 20 -> 10: 2.739m     0.6129s
s21 = 2.739
t21 = 0.6129
# 0 -> 20: 5.146m    1.9268s
s02 = 5.146
t02 = 1.9268
# 10 -> 20: 4.0691m  1.0009s
s12 = 4.0691
t12 = 1.0009
# 20 -> 0: 2.31m  1.0759s
s20 = 2.31
t20 = 1.0759
# 10 -> 0: 1.0821m  0.6129s
s10 = 1.0821
t10 = 0.6129

vm = 20/3.6
s1 = (2000+8990.99+61576.16)/1000-5
s2 = 5+(2773.55+8165.47)/1000
s3 = (8523.29+8178.47)/1000

aat.append([aa,3/20])
aat.append([0, t02-3/20+aat[-1][1]])
aat.append([0,(s1-s02-s21)/vm+aat[-1][1]])
aat.append([-aa, 6/20+aat[-1][1]])
aat.append([0, t21-6/20+aat[-1][1]])
aat.append([0, (s2-s10)*2/vm+aat[-1][1]])
aat.append([-aa, 6/20+aat[-1][1]])
aat.append([0, t10-6/20+aat[-1][1]])

aat.append([aa, 3/20+aat[-1][1]])
aat.append([0, t02+aat[-1][1]-3/20])
aat.append([0, (s3-s20-s02)/vm+aat[-1][1]])
aat.append([-aa, 6/20+aat[-1][1]])
aat.append([0, t20-6/20+aat[-1][1]])

def fun1(x):
    if(x == 0 or x == aat[-1][1]):
        return 0
    for i in range(len(aat)):
        if(x<aat[i][1]):
            return aat[i][0]
def fun2(x,last,q):
    if((x >= aat[1][1]-q and x <= aat[1][1]+q) or (x >= aat[4][1]-q and x <= aat[4][1]+q) or (x >= aat[7][1]-q and x <= aat[7][1]+q) or (x >=aat[9][1]-q and x <= aat[9][1]+q) or x>=aat[-1][1]-q):
        return 0
    return fun1(x)*q+last

x1 = np.linspace(0, aat[-1][1], 10000)
y1 = []
y2 = []
y3 = []
y4 = []
w = []
y3cot = 0
y4cot = 0
for i in x1:
    y1.append(fun1(i))
    q=aat[-1][1]/10000
    y2val = fun2(i, y2[-1] if len(y2) else 0, q)
    y2.append(y2val)
    y3cot = y3cot+y2val*q
    y3.append(y3cot)
    y4cot = y4cot+y3cot*q
    y4.append(y4cot)
    
#保存csv
with open('31-data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['时间t(s)', '路程s(m)', '速度v(m/s)',
                    '加速度a(m/s^2)', '加加速度A(m/s^3)'])
    for i in range(len(x1)):
        writer.writerow([x1[i], y4[i], y3[i], y2[i], y1[i]])

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
#加加速度
plt.title("45°停车时加加速度关于时间的变化")
plt.ylabel("加加速度 A(m/s^3)")
plt.xlabel("时间 t(s)")
plt.plot(x1,y1)
plt.show()
#加速度
plt.title("45°停车时加速度关于时间的变化")
plt.ylabel("加速度 a(m/s^2)")
plt.xlabel("时间 t(s)")
plt.plot(x1, y2)
plt.show()
#速度
plt.title("45°停车时速度关于时间的变化")
plt.ylabel("速度 v(m/s)")
plt.xlabel("时间 t(s)")
plt.plot(x1, y3)
plt.show()
#路程
plt.title("45°停车时路程关于时间的变化")
plt.ylabel("路程 s(m)")
plt.xlabel("时间 t(s)")
plt.plot(x1, y4)
plt.show()
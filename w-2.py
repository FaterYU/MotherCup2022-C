import matplotlib.pyplot as plt
import numpy as np
def funw(x):
    return (20.0/3.6)/(2.8/np.tan(np.arctan(1/(1/np.tan((5*np.pi*x)/36) + 0.6071428571))/2 + (5*np.pi*x)/72) - 0.85)
x=[]
y=[]
x.append(1.23392144614461)
y.append(0)
a = np.linspace(0.001, 1.175, 1000)
for i in a:
    x.append(i+1.23392144614461)
    y.append(-1*funw(i))
x.append(3.00110739323932)
y.append(-1*funw(1.175))
x.append(3.00110739323933)
y.append(0)
x.append(16.4570685898589)
y.append(0)
a = np.linspace(0.001, 1.175, 1000)
for i in a:
    x.append(i+16.4570685898589)
    y.append(-1*funw(i))
x.append(20.2401378297829)
y.append(-1*funw(1.175))
a = np.linspace(0.001, 1.175, 1000)
for i in a:
    x.append(i+20.2401378297829)
    y.append(-1*funw(i))
x.append(22.0384109450945)
y.append(-1*funw(1.175))
x.append(22.0384109450946)
y.append(0)
x.append(23.8940757555755)
y.append(0)


plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

plt.title("45°停车时角速度关于时间的变化")
plt.ylabel("角速度 w(rad/s)")
plt.xlabel("时间 t(s)")
plt.plot(x,y)
plt.show()
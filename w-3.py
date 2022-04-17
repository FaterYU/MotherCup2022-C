import matplotlib.pyplot as plt
import numpy as np
def funw(x):
    return (20.0/3.6)/(2.8/np.tan(np.arctan(1/(1/np.tan((5*np.pi*x)/36) + 0.6071428571))/2 + (5*np.pi*x)/72) - 0.85)
x=[]
y=[]
x.append(1.1694569720972)
y.append(0)
a = np.linspace(0.001, 1.175, 1000)
for i in a:
    x.append(i+1.1694569720972)
    y.append(-1*funw(i))
x.append(2.943990125)
y.append(-1*funw(1.175))
x.append(2.943990126)
y.append(0)
x.append(13.7249444365236)
y.append(0)
a = np.linspace(0.001, 1.175, 1000)
for i in a:
    x.append(i+13.7249444365236)
    y.append(funw(i))
x.append(20.3218360290429)
y.append(funw(1.175))
x.append(20.3218360290430)
y.append(0)
x.append(28.5745080660066)
y.append(0)
a = np.linspace(0.001, 1.175, 1000)
for i in a:
    x.append(i+28.5745080660066)
    y.append(-1*funw(i))
x.append(30.4138998072607)
y.append(-1*funw(1.175))
a = np.linspace(0.001, 31.3713015691969-30.4138998072607, 1000)
for i in a:
    x.append(i+30.4138998072607)
    y.append(-1*funw(i))
a = np.linspace(0.001, 1.175, 1000)
for i in a:
    x.append(i+31.3713015691969)
    y.append(funw(i))
x.append(32.7451075221122)
y.append(funw(1.175))

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

plt.title("侧方停车时角速度关于时间的变化")
plt.ylabel("角速度 w(rad/s)")
plt.xlabel("时间 t(s)")
plt.plot(x,y)
plt.show()
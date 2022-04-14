import numpy as np
#地图TODO(n个停车位对象和其他类型构成)构建全局坐标系（用实际长度）
#停车位类
class Parking:
    id = 0
    location = []#坐标类似[[0,0],[0,1],[1,1],[1,0]]
    is_park = 0
    category = 0#停车位类型：0 1 2
    def __init__(self,id,location):
        self.id = id
        self.location = location
    #是否已经停车
    def isPark(self):
        return self.is_park
    #更改停车状态 TODO
#其他地标类TODO
#无人车类
class Car:
    velocity = 0#速度
    acceleration = 0#加速度
    aacceleration = 0#加加速度
    steering = 0#方向盘速度
    width = 1.8
    length = 4.9
    location = [0, 0]#后轴中心
    direction = np.deg2rad(90)#当前方向（弧度）
    frame = [[0.9,3.85],[-0.9,3.85],[-0.9,-1.05],[0.9,-1.05]]#矩形边框 相对于location的坐标
    t = 0#当前任务计时器
    pathlen = 0#当前任务路径长度
    
    def __init__(self, velocity, acceleration, aacceleration, steering, location, direction):
        self.velocity = velocity
        self.acceleration = acceleration
        self.aacceleration = aacceleration
        self.steering = steering
        self.location = location
        self.direction = direction
    #方向盘转向计算转向半径
    def turnRadius(self):
        si=np.deg2rad(np.abs(self.steering)/16)
        cotsi=1/np.tan(si)
        cots0=17/28+cotsi
        tans0=1/cots0
        s0=np.arctan(tans0)
        undernum=np.tan((si+s0)/2)
        radius=2.8/undernum
        return radius
    #转向
    def turn(self,steering):
        self.steering=steering
    #执行指令的循环节
    def _loop(self,deltaT):
        #TODO
        #例：
        self.velocity+=self.acceleration*deltaT
        self.pathlen+=self.velocity*deltaT
        self.t-=deltaT#递减计时器
    #直行(要加形参，例如加速度等，deltaT是精度)
    def forward(self,t,deltaT):
        self.t = t
        while(self.t>0):
            self._loop(deltaT)
        t = 0
        return self.pathlen
    #后退TODO
    #转弯TODO(转向的路径长度被deltaT微分了可以在loop中当直线算，用deltaT去控制精度)
    #判断碰撞TODO（车辆矩形中是否有其他地表类型的顶点）
#路径规划算法TODO
#泊车算法TODO（包括两段，正向段+逆向段）
#全局控制
car=Car(20/3.6,0,0,0,[0,0],0)
car.turn(470)
print(car.turnRadius())
print(car.forward(2,0.01))
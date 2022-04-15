from mimetypes import init
from pickle import FALSE, TRUE
from time import sleep
import numpy as np
#地图TODO(n个停车位对象和其他类型构成)构建全局坐标系（用实际长度）
lotList=[]
banArea=[[(0,10.8),(5.8,10.8),(0,16),(5.8,16)],[(75.4,10.8),(77.8,13.2)],[(75.4,19.1),()]]
wall=[[(69.4,10.8),(69.9,10.8),(69.4,16),(69.9,16)],[]]
#停车位类
class Parking:
    id = 0
    location = []#坐标类似[[0,0],[0,1],[1,1],[1,0]]
    is_park = 0
    direction=0    # 车头朝向
    category = 0#停车位类型：0 1 2
    def __init__(self,id,location,direction,category):
        self.id = id
        self.location = location
        self.direction=direction
        self.category=category
    #是否已经停车
    def isPark(self):
        return self.is_park
    #更改停车状态为已占用
    def isParkOccupied(self):
        self.is_park=1
    # 更改停车状态为空置
    def isParkRelease(self):
        self.is_park=0
    # 是否方向正确
    def isRightDirection(self,car):
        if car.direction==self.direction:
            return TRUE
        return False
#其他地标类 TODO
# 出口    第四题用
# 上方的出口
class ExitUP:
    location=[]

    def isExit(self,car):
        if car.location[0]<=self.location[0] and car.location[1]>=self.location[1]:
            return TRUE
        return False

# 下方的出口
class ExitBottom:
    location=[]

    def isExit(self,car):
        if car.location[0]>=self.location[0] and car.location[1]<=self.location[1]:
            return TRUE
        return FALSE

# 减速带
class SpeedBump:
    area=[]

# 墙
class Wall:
    pass
    
# 道路
class Road:
    width=5.5
    def __init__(self,length,direction,turningPointList) -> None:
        self.length=length
        self.direction=direction
        self.turningPoints=turningPointList
    
    def isRightDirection(self,car):
        if car.direction==self.direction:
            return TRUE
        return FALSE
    
    def isTruningPoint(self,car):
        # TODO 优化算法，找到合适的判断依据
        for i in range(len(self.turningPointList)):
            if car.location[0]==self.turnPoint[i][0] and car.location[1]==self.turningPointList[i][1]:
                return TRUE
        return FALSE   

class TurningPoint:
    def __init__(self,location) -> None:
        self.location=location
    
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
    target=None
    
    def __init__(self, velocity, acceleration, aacceleration, steering, location, direction,target):
        self.velocity = velocity
        self.acceleration = acceleration
        self.aacceleration = aacceleration
        self.steering = steering
        self.location = location
        self.direction = direction
        self.target=target
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



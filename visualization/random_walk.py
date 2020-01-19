# 随机漫步的图表
from random import choice
from matplotlib import pyplot

class RandomWalk:
    
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    
    def free_walk(self):
        while len(self.x_values) < self.num_points:
            
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0 ,1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
        
            self.x_values.append(next_x)
            self.y_values.append(next_y)

while True:
    rw = RandomWalk()
    rw.free_walk()

    # pyplot.scatter(rw.x_values, rw.y_values, s=2)
    pyplot.plot(rw.x_values, rw.y_values)

    # 突出起点和终点
    pyplot.scatter(0, 0, c="green", s=50)
    pyplot.scatter(rw.x_values[-1], rw.y_values[-1], c="red", s=50)

    # 隐藏坐标轴
    pyplot.axes().get_xaxis().set_visible(False)
    pyplot.axes().get_yaxis().set_visible(False)

    # 调整图像大小
    # pyplot.figure(dpi=128, figsize=(100,60))
    
    pyplot.show()
    
    keep_running = input('Make another walk?(y/n)')
    if keep_running != 'y':
        break
import json
import copy
import math

with open('./classes.json') as f:
    content = json.load(f)


# 定义路由器的类
class Router:
    def __init__(self, name):
        # 存邻居距离的地方
        self.neighbors = {}
        # 存路由网上所有的路由
        self.name = name
        # 初始的路径
        self.bestPath = {}
        # 所有的路由
        self.allRouters = ()
    
    # 初始化的函数
    def setNeighbor(self,neighbor, dis):
        if not neighbor.name in self.neighbors:
            self.neighbors[neighbor.name] = dis
        else:
            if self.neighbors[neighbor.name] != dis:
                raise('怎么会这样')
    def connect(self, router, distance):
        self.setNeighbor(router, distance)
        router.setNeighbor(self, distance)

    # 获取路由的最短路径
    # LS方法
    # 初始化，分析出所有其他路由的距离
    def init(self, allRouters):
        self.allRouters = allRouters
        for r in allRouters:
            if r != self.name:
                if r in self.neighbors:
                    self.bestPath[r] = {
                        'dis': self.neighbors[r],   # 距离
                        'previous': self    # 上一个路由
                    }
                else:
                    self.bestPath[r] = {
                        'dis': float('inf'),   # 距离
                        'previous': None    # 上一个路由
                    }
            # else:
            #     self.bestPath[r] = {
            #             'dis': 0,   # 距离
            #             'previous': None    # 上一个路由
            #         }


    def analysePath(self):
        if not len(self.allRouters):
            raise('没有进行初始化')     
        allRouters = self.allRouters.values()
        # 已经走过的路由器
        goby = [self]

        leftRouters = [x for x in allRouters if x not in goby]
        print(leftRouters)
        while len(leftRouters):
            pick = sorted(leftRouters,key=lambda item: self.bestPath[item.name]['dis'])[0]
            goby.append(pick)
            for name, dis in pick.neighbors.items():
                router = self.allRouters[name]
                if not router in goby:
                    print('-' * 10)
                    print('开始计算%s的距离' % name)
                    oldDis = self.bestPath[name]['dis']
                    print('原来的距离')
                    print(oldDis)
                    newDis = self.bestPath[pick.name]['dis'] + dis
                    print('新的距离')
                    print(newDis)
                    if newDis < oldDis:
                        self.bestPath[name]['dis'] = newDis
                        self.bestPath[name]['previous'] = pick
                    print('最终的距离')
                    print(self.bestPath[name]['dis'])
            leftRouters = [x for x in allRouters if x not in goby]
    # 打印最佳路线的信息
    def printBest(self):
        for name, v in self.bestPath.items():
            print('-'*10)
            print('%s路由的信息开始打印' % name)
            print('距离为：', v['dis'])
            print('前一个路由为', v['previous'].name)

    # 获取到某个目标路由的路径，已经最终的距离
    def getPath(self, target):
        self.analysePath()

        target_best = self.bestPath[target.name]
        path_info = [(
            target,
            0
        )]
        while target_best['previous'].name != self.name:
            router = self.allRouters[target_best['previous'].name]
            path_info.append((
                router,
                router.neighbors[target.name]
            ))
            
            target = router
            target_best = self.bestPath[target.name]
        
        # 加上自己本身
        path_info.append((
            self,
            self.neighbors[target.name]
        ))
        
        path_info.reverse()
        return path_info



# 生成一个路由器网络
routers = {}
# 初始化路由器
for key in content:
    routers[key] = Router(key)
# 连接路由器
for key in content:
    for neighbor in content[key]:
        dis = content[key][neighbor]
        # 开始链接吧！我的兄弟们！！
        routers[key].connect(routers[neighbor], dis)


# LS方法，获取路由u到所有其他路由的最佳路径
routers['u'].init(routers)
routers['u'].analysePath()
routers['u'].printBest()
path = routers['u'].getPath(routers['z'])
print('u到z的路径为')
for index, (r, dis) in enumerate(path):
    if index + 1 < len(path):
        print('第%d步：%s -> %s，距离为: %d' % (
            index + 1,
            r.name,
            path[index + 1][0].name,
            dis
        ))


routers['y'].init(routers)
routers['y'].analysePath()
print('hahah')
routers['y'].printBest()

# for r in routers:
#     if r != 'u':
#         routers['u'].getBestPath(routers[r], routers)

'''
奥特曼打怪兽
'''
from abc import abstractmethod, ABCMeta
from random import randint, randrange

class Fighter(object,metaclass=ABCMeta):
    '''
    战斗者
    '''
    __slots__ = ['_hp','_name']

    def __init__(self,name,hp):
        '''
        初始化方法

        :param name: 名字
        :param hp: 生命值
        '''
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0
    
    @abstractmethod
    def attack(self, target):
        '''
        攻击
        
        :param other: 被攻击的对象
        '''
        pass

class Ultraman(Fighter):
    '''
    奥特曼
    '''
    __slots__ = ['_name','_hp','_mp']
    
    def __init__(self, name, hp, mp):
        '''
        初始化方法
        
        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        '''
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, target):
        target.hp -= randint(15, 25)
        
    def ultimate_attck(self, target):
        '''
        必杀技(打掉对方至少50点或四分之三的血)
        
        :param target: 被攻击的对象
        :return: 使用成功就返回True
        '''
        
        if self._mp >= 50:
            self._mp -= 50
            injury = target.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            target.hp -= injury
            return True
        else:
            self.attack(target)
            return False
        
    def magic_attack(self, targets):
        '''
        魔法攻击
        
        :param targets: 被攻击的群体
        :return: 使用魔法成功返回True否则返回False
        '''

        if self._mp >= 20:
            self._mp -= 20
            for t in targets:
                if t.alive:
                    t.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        '''
        回复魔法值
        '''
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp


class Monster(Fighter):
    '''
    小怪兽
    '''
    __slots__ = ('_name', '_hp')

    def attack(self, target):
        target.hp -= randint(10, 20)
        
    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for m in monsters:
        if m.hp > 0:
            return True
    else:
        return False

def select_alive_one(monsters):
    '''
    选择一个活着的怪兽
    '''
    m_len = len(monsters)
    while True:
        index = randrange(m_len)
        monster = monsters[index]
        if monster.hp > 0:
            return monster

def display_info(ultraman, monsters):
    '''
    显示奥特曼和小怪兽的信息
    '''

    print(ultraman)
    for monster in monsters:
        print(monster)


def main():
    u = Ultraman('猪奥特',1000,120)
    monsters = [
        Monster('猪儒',250),
        Monster('石化鸡蛇',500),
        Monster('麒麟兽',600)
    ]
    fight_round = 1
    while u.alive and is_any_alive(monsters):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(monsters)  # 选中一只小怪兽
        skill = randint(1,10)
        if skill <= 6:  # 50%普通攻击
            print('%s使用普通攻击打了%s' % (u.name,m.name))
            u.attack(m)
            print('%s的魔法值回复了%s点' % (u.name, u.resume()))
        elif skill <= 9: # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(monsters):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else: # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.ultimate_attck(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))

        # 如果挂售没有死，就回击奥特曼
        if m.alive:
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, monsters)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')

    if u.alive:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()
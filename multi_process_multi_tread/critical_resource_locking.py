'''
多线程共用的变量叫做临界资源
    - 给临界资源上锁，保证逻辑的准确性
'''

from time import sleep
from threading import Thread, Lock

class Account:
    
    def __init__(self):
        self._balance = 0
        self._lock = Lock()
    
    def desposit(self, money):
        # 先获取锁之后才能执行后续的代码
        self._lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟受理存款业务需要0.01秒的时间
            sleep(0.01)
            # 修改账户余额
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.desposit(self._money)

def main():
    account = Account()
    threads = []
    # 创建100个线程向同一个账户存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等待所有线程完成转账
    for t in threads:
        t.join()
    print('账户的余额为：￥%d元' % account.balance)

if __name__ == "__main__":
    main()
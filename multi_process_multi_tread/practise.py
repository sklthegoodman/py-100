'''
耗时间的任务放到线程中以获得更好的用户体验。
'''
import time
import tkinter
import tkinter.messagebox
from threading import Thread, Timer

class DownloadTask(Thread):
    def __init__(self, button_instance):
        super().__init__()
        self._button = button_instance

    def run(self):
        # 模拟下载任务需要花费3s的时间
        time.sleep(3)
        tkinter.messagebox.showinfo('提示', '下载完成')
        # 重新启用下载按钮
        self._button.config(state=tkinter.NORMAL)



def show_about():
    tkinter.messagebox.showinfo('关于', '作者：好儒')

def download():
    # 禁用下载按钮
    pass

def time_consuming_task():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    pannel = tkinter.Frame(top)
    button1 = tkinter.Button(pannel, text="下载", command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(pannel, text="关于", command=show_about)
    button2.pack(side='right')
    pannel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == "__main__":
    # time_consuming_task()
    def func(arg):
        print(arg)

    def wrap():
        '''
        因为python不支持匿名函数，所以只能用一层wrap来包装
        '''
        func(t)

    t = Timer(1,wrap)
    t.start()
'''
耗时间的任务放到线程中以获得更好的用户体验。
'''
import time
import tkinter
import tkinter.messagebox
from threading import Thread, Timer

class DownloadTask(Thread):

    def run(self):
        # 模拟下载任务需要花费3s的时间
        time.sleep(3)
        tkinter.messagebox.showinfo('提示', '下载完成')
        # 重新启用下载按钮
        button1.config(state=tkinter.NORMAL)



def show_about():
    tkinter.messagebox.showinfo('关于', '作者：好儒')

def download():
    # 禁用下载按钮
    button1.config(state=tkinter.DISABLED)
    # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
    # 在线程中处理耗时间的下载任务
    DownloadTask(daemon=True).start()

def time_consuming_task():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)


    pannel = tkinter.Frame(top)
    global button1
    button1 = tkinter.Button(pannel, text="下载", command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(pannel, text="关于", command=show_about)
    button2.pack(side='right')
    pannel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == "__main__":
    time_consuming_task()
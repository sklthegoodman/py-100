'''
多线程
    - 耗时间的任务放到线程中以获得更好的用户体验。
'''
import time
import tkinter
import tkinter.messagebox
from threading import Thread, Timer
from multiprocessing import Process, Queue

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


'''
多进程
    - 使用多进程对复杂任务进行“分而治之”。
'''
def calculate_child_task(cal, queue):
    total = 0
    for num in cal:
        total += num
    print('子继承计算完毕，结果为：')
    print(total)
    queue.put(total)

def calculate(to_be_cal):
    processes = []
    result_queue = Queue()
    step = to_be_cal // 8 # 分成8个
    start_time = time.time()
    print(start_time)
    for number in range(1,9):
        # 计算出生成器的前和后
        start = (number - 1) * step
        end = number * step
        # 生成器
        if number == 8:
            num_list = (n for n in range(start, (to_be_cal + 1)))
        else:
            num_list = (n for n in range(start, end))

        # 子进程
        p = Process(target=calculate_child_task, args=(num_list, result_queue))
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print('最终的计算结果为：%d' % total)
    print(time.time())
    print('耗费的时间为：%s' % (time.time() - start_time))

if __name__ == "__main__":
    # time_consuming_task()
    calculate(100000000)
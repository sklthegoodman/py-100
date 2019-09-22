'''
基本上使用tkinter来开发GUI应用需要以下5个步骤：

导入tkinter模块中我们需要的东西。
创建一个顶层窗口对象并用它来承载整个GUI应用。
在顶层窗口对象上添加GUI组件。
通过代码将这些GUI组件的功能组织起来。
进入主事件循环(main loop)。
'''

import tkinter
import tkinter.messagebox

def main():
    flag = True
    
    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world') if flag else ('blue', 'Goobye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('猪儒提示','你要退出？是想挨打吗？'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('傻猪游戏')
    
    # 创建标签对象并添加到到顶层窗口
    label = tkinter.Label(top,text="Hello, world!", font="Arial -32", fg="red")
    label.pack(expand=1)
    # 创建一个装容器的按钮
    panel = tkinter.Frame(top)
    # 创建按钮对象，指定添加到哪个容器中，通过command参数绑定回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()

    

if __name__ == "__main__":
    main()
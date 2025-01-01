import event.key as k
import tkinter as tk
from tkinter import messagebox
import time
import os
os.system('mkdir .\\mirror')
with open('.\\mirror\\使用说明.txt','w') as file:
    file.write('''
--------------------------使用说明--------------------------\n
本程序功能：
    用于无法粘贴的纯文本粘贴，如：某某打字通
    （隐藏功能：键盘宏）
使用说明：
    将需要粘贴的内容复制到输入框里，然后点开始映射就可以了
    卍为换行符，可以使用[添加换行符]键添加到内容末尾
    当然，如果你打得出来的话，手写也是可以的
    ''')
messagebox.showinfo('映射 by 91工作室','此程序仅支持英文映射\n当然，我们会继续改进！')
messagebox.showinfo('映射 by 91工作室','使用说明存放于此程序路径下的mirror文件夹内')
root=tk.Tk()
inp=tk.Entry(bd=5,width=40)
inp.pack()
lab1=tk.Label(master=root,text='请先检查好是否为英文输入法',fg='red')
lab1.pack()
root.geometry('250x120')
root.title('卐91工作室卍')
def mirror():
    '映射的主体程序'
    time.sleep(3)
    global inp
    dic={'?':'/','!':'1','@':'2','#':'3','$':'4','%':'5','^':'6','&':'7','*':'8','(':'9',')':'0',';':';','"':"'"}
    try:
        a=inp.get()
    except:
        pass
    b=list(a)
    for i in b:
        if i=='卍':
            k.press('enter')
        elif i in dic:
            k.keydown('shift')
            k.press(dic[i])
            k.keyup('shift')
        else:
            k.press(i)
def entryEnter():
    '回车键'
    inp.insert(tk.END,'卍')
but1=tk.Button(master=root,text='开始映射',command=mirror,bd=3)
but2=tk.Button(master=root,text='添加回车符（可手动添加）',command=entryEnter,bd=3)
but1.pack()
but2.pack()
root.mainloop()
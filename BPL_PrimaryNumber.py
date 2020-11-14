#!/usr/bin/env python
# coding: utf-8

# In[31]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# In[3]:


title = "BPL - Primary Number Finder"

def straight_output(x) :
    return "result is" + str(x)


# In[38]:


root = tk.Tk()     # 루트(가장 상위의 부모위젯) 지정
root.title(title)
root.geometry("300x200+100+100")

lbl = tk.Label(root, text="Select how to find primary number")   # (부모위젯, 성분)
lbl.grid(column=0, row=0)      # .grid : 위젯을 위치지정해서 부모위젯에 패킹한다

def run_model() :
    if strv.get()=='model_1' :
        result = straight_output(1)
    tk.messagebox.showinfo("result", result)
strv = tk.StringVar()

search_engines = ttk.Combobox(root, width=17, textvariable=strv)    # 콤보박스로 어떤 모델로 소수를 찾을지 선택
# 선택한 사항을 strv에 저장하여 반환한다.
search_engines['values'] = ('model_1', 'model_2', 'model_3')
search_engines.grid(column=0, row=1)
search_engines.current(0)     # 초기 선택값

btn = tk.Button(root, text="Search", command=run_model)
btn.grid(column=0, row=2)

root.mainloop()


# In[34]:


strv


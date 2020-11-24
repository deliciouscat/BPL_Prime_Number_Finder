import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

title = "BPL - Primary Number Finder"

def straight_output(x) :
    return "result : " + str(x)

root = tk.Tk()     # 루트(가장 상위의 부모위젯) 지정
root.title(title)
root.geometry("195x210")

lbl = tk.Label(root, text="Select how to find primary number")   # (부모위젯, 성분)
lbl.grid(column=0, row=0)      # .grid : 위젯을 위치지정해서 부모위젯에 패킹한다


output = tk.Text(root, width=25, height=10)
output.grid(column=0, row=4)

num = tk.IntVar()
numin = tk.Entry(root, textvariable=num)
numin.grid(column=0,row=2)

model_select = tk.StringVar()
def run_model() :
    if model_select.get()=='model_1' :
        result = straight_output(num.get())
    output.insert(tk.CURRENT,"Input number : "+ str(num.get()) +"\n")
    output.insert(tk.CURRENT,result)

search_engines = ttk.Combobox(root, width=17, textvariable=model_select)    # 콤보박스로 어떤 모델로 소수를 찾을지 선택
# 선택한 사항을 strv에 저장하여 반환한다.
search_engines['values'] = ('model_1', 'model_2', 'model_3')
search_engines.grid(column=0, row=1)
search_engines.current(0)     # 초기 선택값

btn = tk.Button(root, text="Search", command=run_model)
btn.grid(column=0, row=3)


root.mainloop()
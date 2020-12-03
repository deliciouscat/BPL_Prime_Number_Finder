import tkinter as tk
from tkinter import ttk

title = "BPL - Primary Number Finder"

def straight_output(x) :
    return "result : " + str(x)


root = tk.Tk()     # 루트(가장 상위의 부모위젯) 지정
root.title(title)
root.geometry("195x230")

lbl = tk.Label(root, text="Select how to find primary number")   # (부모위젯, 성분)
lbl.grid(column=0, row=0)      # .grid : 위젯을 위치지정해서 부모위젯에 패킹한다


output = tk.Text(root, width=25, height=10)       # 출력창
output.grid(column=0, row=4)

num = tk.IntVar()
numin = tk.Entry(root, textvariable=num)          # 입력창
numin.grid(column=0,row=2)

model_select = tk.StringVar()         # 사용하고자 하는 기능을 tkinter String으로 받는다.
def run_model() :
    if model_select.get()=='Output test' :        # ~.get : tkinter string의 값을 python string으로 변환
        result = straight_output(num.get())         # 받아들인 수를 모델에 대입.
    elif model_select.get()=='Prime finder' :
        result = primefinder(range(num.get()))    # primefinder함수는 자료형 형태로 받기 때문에 range형태로 변환
        result = str(result)
    elif model_select.get()=='Adjoined number prime' :
        combi = combination(str(num.get()))
        result = primefinder(combi)
        result = str(result)
    
    output.delete('1.0','end')      #출력창의 기존 내용 제거
    output.insert(tk.CURRENT,"Input number : "+ str(num.get()) +"\n")  # input에 대한 정보
    output.insert(tk.CURRENT,result + "\n")   # 제시한 답.

search_engines = ttk.Combobox(root, width=17, textvariable=model_select)    # 콤보박스로 어떤 모델로 소수를 찾을지 선택
# 선택한 사항을 textvariable에 저장하여 반환한다.
search_engines['values'] = ('Output test', 'Prime finder', 'Adjoined number prime')
search_engines.grid(column=0, row=1)
search_engines.current(0)     # 초기 선택값

btn = tk.Button(root, text="Search", command=run_model)    # 검색버튼
btn.grid(column=0, row=3)


root.mainloop()    # 창 열기
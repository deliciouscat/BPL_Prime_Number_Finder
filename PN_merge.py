import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

title = "BPL - Primary Number Finder"

def straight_output(x) :
    return "result : " + str(x)

def primefinder(numbers) :
    is_primes=[] #소수를 담을 리스트
    isnt_primes=[] #소수가 아닌 수를 담을 리스트

    for n in numbers:
        if n<=1:
            isnt_primes.append(n)
        elif n>=2:
            for i in range(2,n):
                if n%i==0:
                    isnt_primes.append(n)
                    break

    for n in numbers:
        if not n in isnt_primes:
            is_primes.append(n)
    return is_primes


def combination(a) : #사용자가 숫자(문자열)을 입력한다.
    number=[] #숫자를 담을 그릇을 만든다.
    memory_n=len(a) #숫자를 세서 그 자릿수를 기억한다.
    h=int((memory_n*(memory_n+1))/2) #숫자들의 자릿 수를 조합한 수들의 숫자의 수
    b=0 #조합하기 위한 범위값의 최소값의 기본값
    c=1 #조합하기 위한 범위값의 최대값의 기본값
    g=1 #조합하기 위한 몇 자리 숫자의 범위를 넓히는 값

    for i in range(memory_n) : #입력한 숫자의 자릿수대로 반복한다.
        for i in range(memory_n) : #입력한 숫자의 자릿수대로 반복한다.(입력한 숫자의 자릿 수가 처음에 1개씩 묶을 때의 반복 수이다.)
            k=a[b:c] #범위 안의 숫자들을 k로 저장한다.
            number.append(int(k)) #k를 정수로 변환해 number 안에 저장한다.
            b=b+1 #범위값의 최솟값에 1을 더한다.ex(123이 입력이면 12, 23 십의 자리를  1에서 2로 옮긴다)
            c=c+1 #범위값의 최솟값에 1을 더한다.ex(123이 입력이면 12, 23 일의 자리를  2에서 3으로 옮긴다)
        b=0 #처음 자릿수로 다시 돌아간다.ex(1234가 입력이면 12, 23 , 34 이때 b값이 2. b=0으로 만듦)
        c=1 #처음 자릿수로 다시 돌아간다. ex) 1234가 입력이면 12, 23, 34, 이때 c값이 3, c=1 로만듦. 
        c=c+g #c값에 1을 더해 계산하고 난뒤 자릿수를 바꾸기 위한 변수다.
        g=g+1 # 그 변수를 1씩 더해 계속해서 자릿 수를 바꾼다. ex) 1234가 입력일때 1, 2, 3,4 에 g가 c에 더해지면 12, 23, 34로 두 자릿 수를 만든다. 
        memory_n=memory_n-1  # ex) 1, 2, 3, 4 는 4번 반복하는 것. 12 23 34 는 3번 반복하는 것이다. 그러므로 시행 수를 줄이기 위해 memory_n값을 하나씩 줄인다.

    return number


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
        result = primefinder(range(num.get()))
        result = str(result)
    elif model_select.get()=='Adjoined number prime' :
        combi = combination(str(num.get()))
        result = primefinder(combi)
        result = str(result)
    
    output.delete('1.0','end')      #출력창의 기존 내용 제거
    output.insert(tk.CURRENT,"Input number : "+ str(num.get()) +"\n")  # input에 대한 정보
    output.insert(tk.CURRENT,result + "\n")   # 제시한 답.

search_engines = ttk.Combobox(root, width=17, textvariable=model_select)    # 콤보박스로 어떤 모델로 소수를 찾을지 선택
# 선택한 사항을 strv에 저장하여 반환한다.
search_engines['values'] = ('Output test', 'Prime finder', 'Adjoined number prime')
search_engines.grid(column=0, row=1)
search_engines.current(0)     # 초기 선택값

btn = tk.Button(root, text="Search", command=run_model)    # 검색버튼
btn.grid(column=0, row=3)


root.mainloop()    # 창 열기
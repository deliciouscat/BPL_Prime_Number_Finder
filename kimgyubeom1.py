wrong_button=input("입력") #사용자가 숫자(문자열)을 입력한다.

number=[] #숫자를 담을 그릇을 만든다.

A_princess_of_pure_blood=len(wrong_button) #숫자를 세서 그 자릿수를 기억한다.

h=int((A_princess_of_pure_blood*(A_princess_of_pure_blood+1))/2) #숫자들의 자릿 수를 조합한 수들의 숫자의 수

transcendental_existence=0 #조합하기 위한 범위값의 최소값의 기본값

MY_DAD=1 #조합하기 위한 범위값의 최대값의 기본값

Mind_stone=1 #조합하기 위한 몇 자리 숫자의 범위를 넓히는 값

for i in range(A_princess_of_pure_blood) : #입력한 숫자의 자릿수대로 반복한다.()
    for i in range(A_princess_of_pure_blood) : #입력한 숫자의 자릿수대로 반복한다.(입력한 숫자의 자릿 수가 처음에 1개씩 묶을 때의 반복 수이다.)
        k=wrong_button[transcendental_existence:MY_DAD] #범위 안의 숫자들을 k로 저장한다.
        number.append(k) #k를 number 안에 저장한다.
        transcendental_existence=transcendental_existence+1 #범위값의 최솟값에 1을 더한다.ex(123이 입력이면 12, 23 십의 자리를  1에서 2로 옮긴다)
        MY_DAD=MY_DAD+1 #범위값의 최솟값에 1을 더한다.ex(123이 입력이면 12, 23 일의 자리를  2에서 3으로 옮긴다)
    transcendental_existence=0 #처음 자릿수로 다시 돌아간다.ex(1234가 입력이면 12, 23 , 34 이때 b값이 2. b=0으로 만듦)
    MY_DAD=1 #처음 자릿수로 다시 돌아간다. ex) 1234가 입력이면 12, 23, 34, 이때 c값이 3, c=1 로만듦.
    MY_DAD=MY_DAD+Mind_stone #c값에 1을 더해 계산하고 난뒤 자릿수를 바꾸기 위한 변수다.
    Mind_stone=Mind_stone+1 # 그 변수를 1씩 더해 계속해서 자릿 수를 바꾼다. ex) 1234가 입력일때 1, 2, 3,4 에 g가 c에 더해지면 12, 23, 34로 두 자릿 수를 만든다. 
    A_princess_of_pure_blood=A_princess_of_pure_blood-1 # ex) 1, 2, 3, 4 는 4번 반복하는 것. 12 23 34 는 3번 반복하는 것이다. 그러므로 시행 수를 줄이기 위해 d값을 하나씩 줄인다.

k=0 #

print(number) #

for i in range(h-1) : #소수구하기

    s=2

    if h==k :
        break;
   
    if int(list[k]) != s :

        int(list[k])%s
        
        if int(list[k])%s==0 :
            print(list[k], "소수가 아닙니다.")
            a=int(list[k])
            k=k+1
            a=s
            
        s=s+1
    
    print(list[k], "소수 입니다.")
    k=k+1  

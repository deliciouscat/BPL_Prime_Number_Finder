numbers = range(100) #윗단계에서 받아낸 숫자를 primes라는 리스트에 담아두자.
is_primes=[] #소수를 담을 리스트
isnt_primes=[] #소수가 아닌 수를 담을 리스트
#여기서 받아온 primes 리스트를 아래 식에 하나씩 대입하는 방법을 잘 모르겠네요.

for n in numbers:
    if n<=1:
        isnt_primes.append(n)
    elif n>=2:
        for i in range(2,n):
            if n%i==0:
                isnt_primes.append(n)
                break

print(numbers, "중 소수:")
for n in numbers:
    if not n in isnt_primes:
        print(n, end=",")

def primefinder(number): #윗단계에서 받아낸 숫자를 numbers라는 리스트에 담아두자   
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

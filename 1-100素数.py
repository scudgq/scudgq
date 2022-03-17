'''
嵌套，标签的一种用法
'''
primes = []
for i in range(2,101):
    is_prime_num = True
    for j in range(2,i):
        if i % j ==0:
            is_prime_num = False
    if is_prime_num:
        primes.append(i)
print(primes)
print(len(primes))
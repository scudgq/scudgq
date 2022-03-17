def is_prime(number):
    if number==1:
        return False
    for idx in range(2,number):
        if number%idx ==0:
            return False
    return True
def get_primes(begin,end):
    primes_list = []
    for number in range(begin,end+1):
        if is_prime(number):
            primes_list.append(number)
        else:
            continue
    return primes_list

print(get_primes(1,100))
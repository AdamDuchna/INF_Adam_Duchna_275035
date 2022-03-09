import math

def prime(number):
    root_num=math.floor(math.sqrt(number))+1
    for i in range(2,root_num):
        if number % i == 0:
            return False
    return True

def select_primes(list):
    primes=[]
    for el in list:
        if prime(el):
            primes.append(el)
    return primes

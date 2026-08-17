def prime_check(num):
    num1 = True
    for i in  range(2,num):
        if num1 % i == 0:
            num1 = False
            return False
    return True
print(prime_check(4))

    
    

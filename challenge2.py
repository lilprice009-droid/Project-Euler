num = 0
fib = 1
total = 0
while num < 4000000:
    if fib % 2 == 0:
        total = total + fib 
        num = num + fib 
        fib = num - fib 

print(total)
    

    


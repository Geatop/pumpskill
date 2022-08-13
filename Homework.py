def fizz_buzz(a,b):
    sum_fizz_buzz = 0
    for i in range(a,b+1):
        if i % 3 == 0 and i % 5 == 0:
            sum_fizz_buzz += i 
    return sum_fizz_buzz        
    

print('0-3:', fizz_buzz(0, 3))
print('0-5:', fizz_buzz(0, 5))
print('15-15:', fizz_buzz(15, 15))
print('1000-20000:', fizz_buzz(1000, 20000))
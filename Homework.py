# def fizz_buzz(a,b):
#     sum_fizz_buzz = 0
#     for i in range(a,b+1):
#         if i % 3 == 0 and i % 5 == 0:
#             sum_fizz_buzz += i 
#     return sum_fizz_buzz        
    

# print('0-3:', fizz_buzz(0, 3))
# print('0-5:', fizz_buzz(0, 5))
# print('15-15:', fizz_buzz(15, 15))
# print('1000-20000:', fizz_buzz(1000, 20000))

def plural_form(number, form_1, form_2, form_3):
    final_form = ''
    numbers = list(str(number))
    numbers_for_form1 = [1]
    numbers_for_form2 = [2,3,4]
    numbers_for_form3 = [0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    #Может быть попробовать через словарь типо форм 1: цифры такие то
    
    if int(numbers[-1]) in numbers_for_form1:
        final_form = form_1
    elif int(numbers[-1]) in numbers_for_form2:
        final_form = form_2
    elif int(numbers[-1]) in numbers_for_form3:
        final_form = form_3
    return final_form


print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))

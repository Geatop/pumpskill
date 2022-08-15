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

def plural_form(number, form_1, form_2, form_3):
    final_form = ''
    numbers = list(str(number))
    numbers_for_form1 = [1]
    numbers_for_form2 = [2,3,4]
    numbers_for_form3 = [0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    try:
        if int(numbers[-2]) and int(numbers[-2]) == 1:
            final_form = form_3
        elif int(numbers[-2]) and int(numbers[-2]) != 1:
            if int(numbers[-1]) in numbers_for_form1:
                final_form = form_1
            elif int(numbers[-1]) in numbers_for_form2:
                final_form = form_2
            elif int(numbers[-1]) in numbers_for_form3:
                final_form = form_3
    except Exception as E:
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


def html(nametag,**kwargs):
    if kwargs:
        final_par_parse = ''    
        for ar in kwargs.items():
            arlist = list(ar)
            parametry = arlist[0] + '='+ f'"{str(arlist[1])}"' 
            final_par_parse += parametry + ' '
        final_par_parse = final_par_parse[:-1]
        tag_with_kwargs = '<' + nametag + final_par_parse+ '>'

    else:
        return "<"+nametag+">"
        # tag_with_kwargs = '<' + nametag + str(kwargs)+ '>'
    return tag_with_kwargs
# print (html('za', width=21, heyda=32))

@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))
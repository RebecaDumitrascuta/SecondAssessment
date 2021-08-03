
# Sa se scrie o functie care primeste un numar nedefinit de parametrii
# si sa se calculeze suma parametrilor care reprezinta numere intregi sau reale

print('-> This is the first exercise: ')


def test_is_number(param):
    if not isinstance(param, bool):  #am inceput prin a exclude variabilele de tip bool (pentru ca am obsetrvat ca sunt traduse cu 0 si 1)
        if isinstance(param, int) or isinstance(param, float):
            return True


def my_function(*args, **kwargs):
    my_sum = 0

    if len(args) == 0:
        return my_sum

    else:# extra: am continuat functia ca sa fie pretabila pt numere din interiorul unor eventuale liste sau tupluri
        for param in args:
            if test_is_number(param):
                my_sum += param

        for param in args:  # iteram args pentru a identifica eventuale liste sau tuple
            if isinstance(param, list) or isinstance(param, tuple):
                for list_item in param:
                    if test_is_number(list_item):
                        my_sum += list_item
        for key, value in kwargs.items():  # iteram kwargs pentru a evalua valorile cheilor
            if test_is_number(value):
                my_sum += value
    return my_sum

print(my_function(1.5, 5, (1.5, 2, 'a', 3), -3, 'abc', [12, 56, 'cad'],abc=True, a=1, c=10.5))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2, param_2=-10))

# Sa se scrie o functie recursiva care primeste ca parametru un numar intreg si returneaza:
    # suma tuturor numerelor de la [0, n]
    # suma numerelor pare de la [0, n]
    # suma numerelor impare de la [0, n]

print('-> This is the second exercise: ')

sum_odd = 0
sum_even = 0
sum_all = 0


def recursive_sum(n):
    global sum_odd
    global sum_even
    global sum_all

    if n > 0:

        sum_all = sum_all + n
        if n % 2 == 1:
            sum_odd = sum_odd + n
        elif n % 2 == 0:
            sum_even = sum_even + n
        recursive_sum(n - 1)

    return sum_odd, sum_even, sum_all


v_odd, v_even, v_all = recursive_sum(n=5)  ## I  unpacked this tuple, to access each variable of function return
print(f'''sum of Odd Elements is: {v_odd}, 
Sum of Even Elements is: {v_even}, 
Sum of All Elements is: {v_all}''')

# Sa se scrie o functie care citste de la tastatura si returneaza valoarea  daca aceasta este un numar intreg,
# altfel returneaza valoarea 0

print('-> This is the third exercise:')

def ask_number():
    user_input = input('Give me a number: ')

    try:
        user_input = int(user_input)
        print('your number', user_input, 'is what we have asked!')
        return True

    except ValueError as e:
        print('Please try again, as the input is not a number (integer) : ', e)
        return False
    finally:
        print('Thank you!')


is_number = False
while not is_number:
    is_number = ask_number()

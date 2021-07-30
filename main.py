
# Sa se scrie o functie care primeste un numar nedefinit de parametrii
# si sa se calculeze suma parametrilor care reprezinta numere intregi sau reale

print("-> This is the first exercise: ")


def test_is_number(param):
    if isinstance(param, int) or isinstance(param, float):
        return True


def my_function(*args, **kwargs):
    my_sum = 0
    other_struct = kwargs.pop("add_other_struct", False)

    if len(args) == 0:
        return my_sum

    else:# extra: am continuat functia ca sa fie pretabila pt numere din interiorul unor eventuale liste sau tupluri
        for param in args:
            if test_is_number(param):
                my_sum += param

    if other_struct:
        for param in args:  # iteram args pentru a identifica eventuale liste sau tuple
            if isinstance(param, list) or isinstance(param, tuple):
                for list_item in param:
                    if test_is_number(list_item):
                        my_sum += list_item
        for key, value in kwargs.items():  # iteram kwargs pentru a evalua valorile cheilor
            if test_is_number(value):
                my_sum += value
    return my_sum


print(my_function(1.5, 5, (1.5, 2, 'a', 3), -3, "abc", [12, 56, "cad"], a=1, add_other_struct=True, c=10.5))
print(my_function())
print(my_function(2, 4, "abc", param_1=2, param_2=-10, add_other_struct=True))

# Sa se scrie o functie recursiva care primeste ca parametru un numar intreg si returneaza:
    # suma tuturor numerelor de la [0, n]
    # suma numerelor pare de la [0, n]
    # suma numerelor impare de la [0, n]

print("-> This is the second exercise: ")

def add_odd_even_all_w_clear(n):
    if isinstance(n,int):
        try:
            l_all = []
            l_odd = []
            l_even = []
            def add_odd_even_all(n):
                if(n>0):
                    l_all.append(n)
                    if(n%2==1):
                        l_odd.append(n)
                    elif (n%2==0):
                        l_even.append(n)
                    add_odd_even_all(n-1)

                return sum(l_all),sum(l_odd), sum(l_even)
            return add_odd_even_all(n)
        finally:
            l_all.clear(),l_odd.clear(),l_even.clear()
    else:
        print(f'{n} is not an interger')
        return 'Invalid','Invalid','Invalid'

summ_all,sum_odd,sum_even = add_odd_even_all_w_clear('a') ## tuple unpack as variables
print(f'This is the sum of all elements: {summ_all}, sum of odd elements: {sum_odd}, sum of even elements: {sum_even}')
summ_all,sum_odd,sum_even = add_odd_even_all_w_clear(3)
print(f'This is the sum of all elements: {summ_all}, sum of odd elements: {sum_odd}, sum of even elements: {sum_even}')


# Sa se scrie o functie care citste de la tastatura si returneaza valoarea  daca aceasta este un numar intreg,
# altfel returneaza valoarea 0

print("-> This is the third exercise:")

def ask_number():
    user_input = input("Give me a number: ")

    try:
        user_input = int(user_input)
        print("your number", user_input, "is what we have asked!")
        return True

    except ValueError as e:
        print("Please try again, as the input is not a number : ", e)
        return False
    except NameError as e:
        print("Please try again, as the input is containing a Name Error: ", e)
        return False
    except IndexError as e:
        print("please try again, as the input is containing an index error: ", e)
        return False
    finally:
        print("Thank you!")


is_number = False
while not is_number:
    is_number = ask_number()

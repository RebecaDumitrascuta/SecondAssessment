
def my_function(*args, **kwargs):
    my_sum = 0
    if len(args) == 0:
        return my_sum
    else:
        for param in args:
            if isinstance(param, int) or isinstance(param, float):
                my_sum += param
    return my_sum


print(my_function (1, 5, -3, "abc", [12, 56, "cad"]))
print(my_function())
print(my_function (2, 4, "abc", param_1=2))

#########we use global variable to take the odd,even,alls from the global scope when entering the function addition######

odd=0
even=0
alls=0

def add_odd_even_all(n):

    global odd
    global even
    global alls

    arr = list(range(0,n+1))
    if(n>0):
        alls = alls + arr[n]
        if(arr[n]%2==1):
            odd=odd+arr[n]
        elif (arr[n]%2==0):
            even=even+arr[n]
        add_odd_even_all(n-1)

    return odd,even, alls

v_odd, v_even, v_alls = add_odd_even_all(5) ## tuple unpack as variables
print(f"Sum of Odd Elements is: {v_odd}, Sum of Even Elements is: {v_even}, Sum of All Elements is: {v_alls}")

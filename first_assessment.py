#Creați un script Python care îndeplinește următoarele funcții:
#○ declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
#○ afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
#○ afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
#○ afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
#○ afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
#○ afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).



my_initial_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("My initial list:", my_initial_list)

my_asc_list = sorted(my_initial_list, reverse=False)
print("My ascending list:", my_asc_list )

my_desc_list = sorted(my_initial_list, reverse=True)
print("My descending list:", my_desc_list)

print("My even list:", my_asc_list[1::2])

# am gasit si variantele de mai jos, pe care am vrut sa le incerc:
#    [ returned value; iteration; condition ]
even_list = [x for x in my_asc_list if x % 2 == 0]
print(even_list)
new_even_list = []
for x in my_asc_list:
    if x % 2 == 0:
        new_even_list.append(x)
print(new_even_list)

my_odd_list = my_asc_list[::2]
print("My odd list:", my_odd_list)
odd_list = [x for x in my_asc_list if x % 2 != 0]
print(odd_list)
new_odd_list = []
for x in my_asc_list:
    if x % 2 != 0:
        new_odd_list.append(x)
print(new_odd_list)


multiple_of_three = my_asc_list[2::3]
print("My multiple of three list:", multiple_of_three)

#for integers;
A = 5
B = 10
print(f"id of A : {id(A)} ")
print(f"id of B : {id(B)} ")
print(f"does both are same ? : {A is B }")
print(" - " *20)

#  for list 
list_1 = [1,2,3]
list_2 = [1,2,3]
print(f" address of list_1 = {id(list_1)}")
print(f" address of list_2 = {id(list_2)}")
print(f" are they same? = {list_1 is list_2}")
print("-" *20)


#for mutable 
list_3 = list_1
list_3.append(99)
print(f" list_3 address : {id(list_3)}, list_1 address: {id(list_1)}")
print(f" list_1 values : {list_1}, list2 values :{list_2} ")
print(f" are they same? = {list_3 is list_1}")





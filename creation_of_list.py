my_list=["narsimha","you",3522,True,18.67]
my_list.append(11)
my_list.insert(1,"me")
for i in range(0,7):
    print(my_list[i])
for i in my_list:
    print(i)
print(my_list[:4])
print(my_list[2:6])
print(my_list[:-1])
print(my_list[4: :-1])
print(my_list[:])
print(my_list[1])
my_list[1]=22
print(my_list[1])

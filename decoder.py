import string
txt=input("enter a string")
x=txt.split()
my_list=[]
# print(x)
for i in x:

    if len(i) <= 3:
        i=i[::-1]
        z=[i]

        my_list = my_list+z
        # print(my_list)
    else:
        i=i[3:]
        i=i[:-3]
        i=i[-1]+i
        i = i[:-1]
        z = [i]

        my_list = my_list + z
        # print(my_list)
resulting_string = " ".join(my_list)

print(resulting_string)
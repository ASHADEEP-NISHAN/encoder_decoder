import random as r
import string
c=string.ascii_letters
d=c.lower()

letters1 = ''.join(r.choice(d) for k in range(3))
letters2=''.join(r.choice(d) for l in range(3))
txt=input("enter a string")
x=txt.split()
# print(x)
my_list=[]
for i in x:

    if len(i) <= 3:
        i=i[::-1]
        z=[i]
        # z=z.append(i)
        my_list = my_list+z
        # print(my_list)
    else :
        i=letters1+i[1:]+i[:1]+letters2
        z=[i]
        my_list = my_list + z
        # print(my_list)




resulting_string = " ".join(my_list)

print(resulting_string)

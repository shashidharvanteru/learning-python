items= ["shashi", 319, "santhu",219, "maddy", 122, "venkat", 1, "swaroopa", 2, 3, "malla"]

num_items = []
str_items = []

for i in items:
    if isinstance(i,int) or isinstance(i,float):
        num_items.append(i)
    else:
        str_items.append(i)

print(num_items)
print(str_items)

def func(abc):
    str_items2=[]
    num_items2=[]
    for j in abc:
        if isinstance(j,int) or isinstance(j,float):
            num_items2.append(j)
        else:
            str_items2.append(j)
    return str_items2,num_items2
print(func(items))





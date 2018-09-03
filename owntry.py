import datetime
today=datetime.date.today()
text="{today1.month}/{today1.year}/{today1.day}".format(today1=today)

names= ["shashi", "santhu", "venkat","maddy","swaroopa", "malla"]
amount= [1000,2223,2354.67,56721.23,9873,7640]
my_msg = """ Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""
def some_func(n,a):
    if len(n)==len(a):
       i = 0
       for name in n:
           name=name[0].upper()+name[1:].lower()
           new_amount="%.2f"%(a[i])
           msg=my_msg.format(name = name,date=text,total=new_amount)
           print(msg)
           i+=1


some_func(names,amount)





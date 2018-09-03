import datetime
today = datetime.date.today()
text = '{today.month}/{today}/{today}'.format(today=today)
print(text)
import datetime, bday_message

today = datetime.date.today()
next_birthday = datetime.date(2025,12,7)

time_difference = next_birthday - today

if today == next_birthday:
    print(bday_message.random_message)
else:
    print(f'My next birthday is {time_difference.days} days away!')
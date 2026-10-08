import datetime

now = datetime.datetime.now()

print(now.year) #kuvab praeguse aasta
print(now.month) #kuvab praeguse kuu (1-12)
print(now.day) #kuvab praeguse kuupäeva (1-31)
print(now.hour) #kuvab praeguse kellaaja (0-23)

weekday = now.strftime("%A")
print(weekday)

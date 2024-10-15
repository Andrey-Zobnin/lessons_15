
month_number = int(input())

if month_number == 1:  # Январь
    days_in_month = 31
elif month_number == 2:  # Февраль 
    days_in_month = 28
elif month_number == 3:  # Март
    days_in_month = 31
elif month_number == 4:  # Апрель
    days_in_month = 30
elif month_number == 5:  # Май
    days_in_month = 31
elif month_number == 6:  # Июнь
    days_in_month = 30
elif month_number == 7:  # Июль
    days_in_month = 31
elif month_number == 8:  # Август
    days_in_month = 31
elif month_number == 9:  # Сентябрь
    days_in_month = 30
elif month_number == 10:  # Октябрь
    days_in_month = 31
elif month_number == 11:  # Ноябрь
    days_in_month = 30
elif month_number == 12:  # Декабрь
    days_in_month = 31
else:
    days_in_month = 0  
print(days_in_month)

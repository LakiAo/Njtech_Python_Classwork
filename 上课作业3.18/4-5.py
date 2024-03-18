def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    
year = int(input())

if is_leap_year(year):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")

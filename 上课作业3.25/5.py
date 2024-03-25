def print_leap_years(start_year, end_year):
    count = 0
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year, end=' ')
            count += 1
            if count % 10 == 0:
                print()
                
start_year = int(input())
end_year = int(input())
print_leap_years(start_year, end_year)

def calc(years):
    return int(years / 100) if years % 2 == 0 else int(years/100) + 1


print(calc(1705))
print(calc(2000))
print(calc(1601))
print(calc(1900))

import ru_local as ru

name = input(ru.HELLO)
print(f'{ru.NICE}, {name}! {ru.MARK}')
age = int(input(ru.AGE))

difference = 80 - age
if 2 <= abs(difference) % 10 <= 4 and not (11 <= abs(difference) % 100 <= 14):
    years = ru.YEARS_1
elif abs(difference) % 10 == 1 and not (abs(difference) % 100 == 11):
    years = ru.YEARS_2
else:
    years = ru.YEARS_3

if difference > 0:
    print(f'{ru.YES.capitalize()}, {name}, {ru.OLDER} {difference} {years}.')
elif difference < 0:
    print(f'{ru.YES.capitalize()}, {name}, {ru.YOUNGER} {abs(difference)} {years}.')
else:
    print(f'{ru.YES.capitalize()}, {name}, {ru.SAME}.')

program = input(ru.PROGRAM)
if program == ru.YES:
    print(ru.PROGRAM_YES)
if program == ru.NO:
    print(ru.PROGRAM_NO)

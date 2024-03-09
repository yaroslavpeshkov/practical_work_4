import ru_local as ru

password = input(ru.PASSWORD)
if password == ru.RIGHT_PASSWORD:
    print(ru.GO)
else:
    print(ru.DENY)

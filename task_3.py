import ru_local as ru

print(ru.WHAT_IS_NAME)
name = input(ru.NAME).lower()
if name == ru.JAMES_BOND or name == ru.AGENT_007:
    print(ru.RIGHT)
else:
    print(ru.WRONG)

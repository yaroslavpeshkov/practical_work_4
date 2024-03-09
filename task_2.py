import ru_local as ru

print(ru.WHAT_TWO_WORDS)
first_word = input(ru.FIRST_WORD)
second_word = input(ru.SECOND_WORD)
if first_word == ru.RIGHT_FIRST_WORD and second_word == ru.RIGHT_SECOND_WORD:
    print(ru.RIGHT)
else:
    print(ru.WRONG)

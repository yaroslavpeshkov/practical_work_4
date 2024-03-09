import ru_local as ru

print(ru.WILL_YOU_GO)
answer_1 = input(ru.ANSWER)
answer_2 = answer_1.split()
print(answer_2)
if not (ru.YES in answer_2 or ru.NO in answer_2):
    print(ru.RIGHT)
else:
    print(ru.WRONG)

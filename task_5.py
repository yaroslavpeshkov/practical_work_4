import ru_local as ru

fish_n = int(input())
fish_k = int(input())
if fish_n > fish_k:
    print(fish_k)
elif fish_k > fish_n:
    print(fish_n)
else:
    print(f'{ru.EQUALITY}: {fish_n}')

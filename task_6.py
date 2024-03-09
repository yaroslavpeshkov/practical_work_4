team_1, team_2 = map(int, input().split(':'))
if team_1 > team_2:
    print('1')
elif team_2 > team_1:
    print('2')
else:
    print('0')

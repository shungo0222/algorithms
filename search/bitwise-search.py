# https://atcoder.jp/contests/abc079/tasks/abc079_c
# O(n*(2**n))


num = input()
op_num = len(num) - 1

for i in range(2 ** op_num):
    ops = ['+'] * op_num
    for j in range(op_num):
        if (i >> j) & 1:
            ops[j] = '-'

    formula = []
    for k in range(op_num):
        formula.append(num[k] + ops[k])
    formula.append(num[op_num])
    
    if eval(''.join(formula)) == 7:
        print(''.join(formula) + '=7')
        break
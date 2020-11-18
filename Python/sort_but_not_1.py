l1 =[-1,20,321,24,-1,-1,234,34,9203,-1]

new_list = [i for i in l1 if i != -1]
new_list.sort()

op_l1 = []
for l in l1:
    if l == -1:
        op_l1.append(-1)
    else:
        op_l1.append(new_list.pop(0))
print(op_l1)
lis = ['again', 'and', 'and', 'hello', 'hello', 'makes', 'perfect', 'practice', 'world', 'world']
n = 0
final_list = []
for item in lis:
    if n == len(lis):
        continue
    if item != lis[n + 1]:
        final_list.append(item)
        n += 1
    else:
        n += 1

print(final_list)
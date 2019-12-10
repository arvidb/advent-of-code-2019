'''input
367479
893698
'''
from collections import Counter

A = int(input())
B = int(input())

result = []
for x in range(A, B):
    X = [int(x) for x in str(x)]
    valid = True
    cnt = 10*[0]
    for i in range(len(X)):
        if i > 0 and X[i-1] > X[i]:
            valid = False
            break
        cnt[X[i]] += 1
    if valid:
        for i in cnt:
            if i == 2:
                result.append(x)
                break

print(len(result))


result = set()
def find_next_sequence(start, out, n):
    if (n == 0): 
        global result
        result.add(out)
        return

    for i in range(start, 10): 
        str1 = out + str(i)
        find_next_sequence(i, str1, n - 1)
        find_next_sequence(i + 1, str1, n - 1)

find_next_sequence(0, "", len(str(A)))

def has_pair(a):
    return any([a[i] == a[i-1] for i in range(1, len(a))])

def has_double(a):
    return any([i == 2 for _,i in Counter(a).items()])

valid_result = []
for x in result:
    if int(x) < A or int(x) > B:
        pass
    elif not has_double(x):
        pass
    else:
        valid_result.append(x)

print(len(valid_result))
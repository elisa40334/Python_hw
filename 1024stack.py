from itertools import permutations
def stackperm(x):
    return permutations(x,len(x))


print(stackperm([1,2,3]))
for idx,i in enumerate(stackperm([1,2,3])):
    print(idx,i)
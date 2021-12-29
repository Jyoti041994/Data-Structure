# obj = {
# "a": 2,
# "b": {"x": 2, "y": {"foo": 3, "z": {"bar": 2}}},
# "c": {"p": {"h": 2, "r": 5}, "q": 'ball', "r": 5},
# "d": 1,
# "e": {"nn": {"lil": 2}, "mm": 'car'}
# Retrun some of all even numbers

def recursiveSum(obj,sum=0):
    for k in obj.values():
        if type(k)==int and k%2==0:
            sum+=k
        elif isinstance(k,dict):
            sum+=recursiveSum(k,sum=0)
    return sum

obj = {
"a": 2,
"b": {"x": 2, "y": {"foo": 3, "z": {"bar": 2}}},
"c": {"p": {"h": 2, "r": 5}, "q": 'ball', "r": 5},
"d": 1,
"e": {"nn": {"lil": 2}, "mm": 'car'}

# c = recursiveSum(obj,sum=0)
print("result is here ",c)


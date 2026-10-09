k=0
def f(start, end,):
    if start == end :
        return 1
    if start > end :
        return 0
    if start < end:
        return f(start+ 1, end) + f(start + 3, end) + f(start +5 , end)
    if start %2 ==0:
        k+=1

print(f(3, 25))
print(k)
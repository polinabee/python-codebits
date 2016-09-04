def SimpleMode(arr):
    a = []
    for n in arr:
        a.append(arr.count(n))
    if max(a) > 1:
        return arr[a.index(max(a))]
    else:
        return -1
    
# keep this function call here  
print SimpleMode(raw_input())

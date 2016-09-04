def LetterCount(str):
    str = str.split(' ')
    r = []
    for w in str:
        r_w = 0
        for l in w:
            if w.count(l) > 1:
                r_w += 1
        r.append(r_w)
    if max(r) != 0:
        return str[r.index(max(r))]
    else:
        return -1
print LetterCount(raw_input())

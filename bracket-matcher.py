def BracketMatcher(str): 
    p = ''
    for s in str:
        if s in '()':
            p += s
    if len(p.replace('()', '')) > 0:
        return 0
    else:
        return 1

print BracketMatcher(raw_input())

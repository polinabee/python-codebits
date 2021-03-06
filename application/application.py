def repeated_letter_count(str):
    max_reps_in_str = 0
    for word in str.split(' '):
        repeats_per_word = 0
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                repeats_per_word += 1
    max_reps_in_str = repeats_per_word if repeats_per_word > max_reps_in_str else max_reps_in_str
    return max_reps_in_str


def dash_insert(str):
    inserted_str = ''
    for x in range(len(str) - 1):
        inserted_str += str[x]
        if int(str[x]) % 2 != 0 and int(str[x + 1]) % 2 != 0:
            inserted_str += '-'
    inserted_str += str[-1]
    return inserted_str


def mode(arr):
    a = [arr.count(n) for n in arr]
    return arr[a.index(max(a))] if max(a) > 1 else -1


def super_increasing(arr):
    ans = 0
    for i in range(len(arr)):
        ans = 0 if arr[i] > sum(arr[:i]) else 1
    return False if ans > 0 else True


def multiplicative_persistence(num):
    n = str(num)
    a = 0

    def mult(x):
        s = 1
        for i in range(0, len(x)):
            s *= int(x[i])
        return s

    while len(n) > 1:
        n = str(mult(n))
        a += 1

    return a


def matched_brackets(str):
    p = ''
    for s in str:
        if s in '()':
            p += s
    while '()' in p:
        p = p.replace('()', '')

    return False if len(p) > 0 else True

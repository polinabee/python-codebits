from random import randrange


def repeated_letter_count(str):
    max_reps_in_str = 0
    for word in str.split(' '):
        repeats_per_word = 0
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                repeats_per_word += 1
    max_reps_in_str = repeats_per_word if repeats_per_word > max_reps_in_str else max_reps_in_str
    return max_reps_in_str


def randomIntString(N):
    return str(randrange(N))


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


# let's say I want to run dash_insert...
def main1():
    randomIntString()
    return dash_insert()


def main2():
    randomIntString(100)
    return dash_insert()


def main2():
    randomIntString(100)
    return dash_insert()


def main3():
    randomIntString(100)
    return dash_insert("idklol")

def main4():
    randomIntString(100)
    return dash_insert("123098")

def final_main():
    return dash_insert(randomIntString(6))

if __name__ == "__main__":
    # put "normal" dev process here:
    # main1()  # oops needs an N!
    # main2() # oops needs a str!
    # main3()  # ValueError: invalid literal for int() with base 10: 'w'. hmmm what input do we want????
    # main4()  # No errors... but we have no idea if what we did is right! if part of bigger pipeline it would fail in prod
    final_main() # how it was intended to be used but you don't know if it ran as expected

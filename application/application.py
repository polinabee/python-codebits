def repeated_letter_count(str):
    max_reps_in_str = 0
    for word in str.split(' '):
        repeats_per_word = 0
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                repeats_per_word += 1
    max_reps_in_str = repeats_per_word if repeats_per_word > max_reps_in_str else max_reps_in_str
    return max_reps_in_str


class Application:
    pass


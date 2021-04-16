import sys


def read_input():
    my_input = [x.rstrip() for x in sys.stdin.readlines()]
    return my_input


def find_all_matches(number, words, findings=""):
    match_words = [word
                   for word in words
                   if is_word_match_number(word, number)]
    # print(match_words)
    if len(match_words) == 0:
        return None

    for word in match_words:
        # print(word)
        fin = findings + " " + word if findings else word
        num = number[len(word):]
        if len(num) == 0:
            return fin
        f = find_all_matches(num, words, fin)
        # print(f"call {num}, {words}, {findings} | return {f}")
        if f:
            output.append(f)


def is_word_match_number(word, number):
    if len(number) < len(word):
        return False
    for x in range(len(word)):
        if num[number[x]].find(word[x]) == -1:
            return False
    return True


def find_best_matches():
    if not len(output):
        return "No solution."
    a = {}
    for h in output:
        number_of_words = len(h.split())
        a[h] = number_of_words
    a = sorted(a.items(),
               key=lambda kv: kv[1])
    return a[0][0]


num = {"0": "oqz",
       "1": "ij",
       "2": "abc",
       "3": "def",
       "4": "gh",
       "5": "kl",
       "6": "mn",
       "7": "prs",
       "8": "tuv",
       "9": "wxy"}

output = []
test_series = read_input()
is_end_of_series = True
t = 0
while(is_end_of_series):
    number_of_input = int(test_series[t + 1])
    start = t + 2
    end = t + number_of_input + 2
    find_all_matches(test_series[t], test_series[start:end])
    # print(output)
    print(find_best_matches())
    output = []
    t = end
    if test_series[t] == "-1":
        is_end_of_series = False

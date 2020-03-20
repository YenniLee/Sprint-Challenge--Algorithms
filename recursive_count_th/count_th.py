'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case 
    if len(word) < 2:
        return 0
    else:
        has_th = 0
        if word[0:2] == 'th':
            has_th = 1
        return has_th + count_th(word[1:])

print(count_th('that'))


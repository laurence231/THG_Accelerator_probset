input_word = 'letsgooffpiste'

def find_perms(input_word):
    if len(input_word) == 1:
        return input_word
    else:
        initial_letter = find_perms(input_word[0])
        remainder = find_perms(input_word[1:])
        return string_appender(initial_letter, remainder)

def string_appender(initial_letter, remainder):
    permutation_list = []
    #print(initial_letter, remainder)
    for element in remainder:
        for i in range(len(remainder)+1):
            a = element[0:i] + initial_letter + element[i:]
            #print(a)
            permutation_list.append(a)
    return permutation_list

print(find_perms(input_word))

# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(input_word):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''


    if len(input_word) == 1:
        return input_word
    else:
        initial_letter = get_permutations(input_word[0])
        remainder = get_permutations(input_word[1:])
        return string_appender(initial_letter, remainder)

def string_appender(initial_letter, remainder):
    permutation_list = []
    for element in remainder:
        for i in range(len(remainder) + 1):
            a = element[0:i] + initial_letter + element[i:]
            permutation_list.append(a)
    return permutation_list

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input = 'bust'
    print('Input: ', example_input)
    print("Expected Output: 'bust', 'ubst', 'usbt', 'ustb', 'ustb', 'ustb', 'ustb', 'bsut', 'sbut', 'subt', 'sutb', 'sutb', 'sutb', 'sutb', 'bstu', 'sbtu', 'stbu', 'stub', 'stub', 'stub', 'stub', 'buts', 'ubts', 'utbs', 'utsb', 'utsb', 'utsb', 'utsb', 'btus', 'tbus', 'tubs', 'tusb', 'tusb', 'tusb', 'tusb', 'btsu', 'tbsu', 'tsbu', 'tsub', 'tsub', 'tsub', 'tsub'")
    print("Actual Output: ", get_permutations(example_input))

print(get_permutations('bust'))



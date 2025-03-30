# Let S be a long string (many lines).
#
# Find the number of black characters in S [not whitespace, see the method S.isspace()].
#
# Find the number of words in S (a word is a sequence of black characters).
#
# Find the longest word in S.
#
# Sort words from S according to (1) the lexicographic order, (2) the length.

long_string = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'

def count_black_space(a):
    count = 0
    for char in long_string:
        if not char.isspace():
            count += 1
    return count

def sort_by_len(words):
    return sorted(words, key=len)

def sort_lexicographically(words):
    return sorted(words, key=str.lower)

def find_longest_word(sentence):
    return sort_by_len(sentence.split(' '))[-1]

print(f"Sample long string: {long_string}")
print(f"Number of black characters: {count_black_space(long_string)}")
print(f"Longest word: {find_longest_word(long_string)}")
print(f"Sorted by length: {sort_by_len(long_string.split(' '))}")
print(f"Sorted lexicographically: {sort_lexicographically(long_string.split(' '))}")

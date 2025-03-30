# For a given word (you may use your name), print it in squares.
# If word = "Python", then the result is
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+

word = "Anastasiya"

word_len = len(word)
x_border = ''.join(['+---' for char in range(word_len)]) + '+'
y_border = '|'

body = ''
for char in word:
    body += y_border + ' ' + char + ' '
body += y_border


print(x_border)
print(body)
print(x_border)

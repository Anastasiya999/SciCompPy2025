# (a) Find Unicode code points (int) for all characters of your name.
# Example: "Andrzej" --> [65, 110, 100, 114, 122, 101, 106]

# (b) Prepare the periodic table (ten elements) as a list
# pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), ...].
# Use pt to print a table (3 right + 20 left + 6 center + 10 right)
# +---+--------------------+------+----------+
# |No.|Name (en)           |Symbol|Weight (u)|
# +---+--------------------+------+----------+
# |  1|Hydrogen            |  H   |         1|
# |  2|Helium              |  He  |         4|
# |   | ...                |      |          |
# +---+--------------------+------+----------+
# Hint: use the for loop:
# for (n, name, symbol, weight) in pt:
#     # use variables (n, name, symbol, weight) to create a proper line
name = 'Anastasiya'

periodic_table = [
    (1, "Hydrogen", "H", 1),
    (2, "Helium", "He", 4),
    (3, "Lithium", "Li", 7),
    (4, "Beryllium", "Be", 9),
    (5, "Boron", "B", 11),
    (6, "Carbon", "C", 12),
    (7, "Nitrogen", "N", 14),
    (8, "Oxygen", "O", 16),
    (9, "Fluorine", "F", 19),
    (10, "Neon", "Ne", 20)
]

def get_name_unicode_points(value):
    return [ord(char) for char in value]

def print_periodic_table(pt):
    # Table header
    print("+---+--------------------+------+----------+")
    print("|No.|Name (en)           |Symbol|Weight (u)|")
    print("+---+--------------------+------+----------+")

    # Body
    for (n, name, symbol, weight) in pt:
        print(f"|{n:>3}|{name:<20}|{symbol:^6}|{weight:>10}|")

    # Footer
    print("+---+--------------------+------+----------+")

print(get_name_unicode_points(name))
print_periodic_table(periodic_table)
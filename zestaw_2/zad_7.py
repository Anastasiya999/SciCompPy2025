# Create a dict for conversion of roman numerals/strings (I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M) to arabic numbers.
# Use different methods.

# 1. using dict() constructor
roman_to_arabic_conversion = dict([
    ("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10),
    ("XL", 40), ("L", 50), ("XC", 90), ("C", 100),
    ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)
])

# 2. using basic static approach
roman_to_arabic_conversion_v2 ={
    "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
    "XL": 40, "L": 50, "XC": 90, "C": 100,
    "CD": 400, "D": 500, "CM": 900, "M": 1000
}

# 3. using DICT COMPREHENSION
roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

roman_to_arabic_conversion_v3 = {roman: arabic for roman, arabic in zip(roman, arabic)}

print(f"v1: {roman_to_arabic_conversion}")
print(f"v2: {roman_to_arabic_conversion_v2}")
print(f"v3: {roman_to_arabic_conversion_v3}")

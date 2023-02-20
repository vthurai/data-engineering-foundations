# Regular Expressions
# A regular expression (regex) is a pattern that is used to search for a string.

import re

# 1. Search
# > re.search(regex_pattern, string)
# Search checks if a regex pattern occurs inside a string.
text = "The quick brown fox jumps over the lazy dog."
regex_pattern = r"brown"
search_result = re.search(regex_pattern, text)
# It is recommended to prefix a regex pattern with 'r'. This tells Python we have a 'raw' string.
# Simply put, doing this will allow Python to read your pattern literally and avoid some potential problems when processing special characters.

# Search returns a "match" object if the regex is found, and "None" if it isn't.
print(search_result)

# To get a boolean, either use bool() or any conditional statement.
print(bool(search_result))


# 2. Sub
# > re.sub(regex_pattern, replacement, string)
# Similar to replace(), sub will return a string with all occurring patterns substituted with the replacement string.
# Sub returns the string unchanged if the pattern is not found.
sub_result = re.sub(regex_pattern, "red", text)
print(sub_result)


# 3. Findall
# > re.findall(regex_pattern, string)
# Findall returns a list of substrings which match the given pattern.
findall_result = re.findall(r"he", text)
print(findall_result)


###########################################################################

# 4. Regex rules
# Some characters are reserved for special use when inside of a regex pattern.
# Here are some of the basic pattern rules. There are many others not listed here.
# https://regex101.com/ is a great resource for testing regex patterns.

# . (Dot)
# The dot will match any character (except for a newline).
print("Example #1:", re.findall(r".", "Hello there."))

# * 
# Will match the previous character zero or multiple times, repeating as many as possible.
print("Example #2:", re.findall(r"el*", "Hello there."))

# +
# Will match the previous character once or multiple times, repeating as many as possible.
print("Example #3:", re.findall(r"el+", "Hello there."))

# ?
# Will match the previous character exactly zero or once.
print("Example #4:", re.findall(r"el?", "Hello there."))

# {n}
# Matches the previous character exactly n number of times.
print("Example #5:", re.findall(r"a{3}", "bad baad baaad baaaad"))

# {m,n}
# Matches the previous character from m to n number of times.
print("Example #6:", re.findall(r"a{2,3}", "bad baad baaad baaaad"))

# |
# Matches the pattern either before or after the '|'.
print("Example #7:", re.findall(r"is|test", "This is a test."))

# ^
# Matches the start of the string.
print("Example #8:", re.findall(r"^math.", "math science mathematics chemistry biochemistry"))

# $
# Matches the end of the string.
print("Example #9:", re.findall(r".{3}chemistry$", "math science mathematics chemistry biochemistry"))

# []
# Matches a single character from a set of characters inside the [].
print("Example #10:", re.findall(r"[cde]", "abcdefg"))
# The '-' symbol can be used to denote ranges.
print("Example #11:", re.findall(r"[0-9]", "There are 6 dogs."))
# [a-z] will match all lowercase letters a to z.
# [a-zA-Z0-9] will match all alphanumeric characters.
# The '^' symbol means to match any character *not* listed inside [].
print("Example #12:", re.findall(r"[^cb]at", "mat cat bat car date Saturday"))
# Special characters used inside [] will be matched literally. [(+*)] will match any of the literal characters '(', '+', '*', or ')'.

# \d and \D
# Matches any (non) digit. Equivalent to [0-9] (or [^0-9]).
print("Example #13:", re.findall(r"\d", "There are 16 dogs."))
print("Example #14:", re.findall(r"\D", "There are 16 dogs."))

# \w and \W
# Matches any (non) word character: letter, digit or underscore. Equivalent to [a-zA-Z0-9_] (or [^a-zA-Z0-9_]).
print("Example #15:", re.findall(r"\w+", "Hello there."))
print("Example #16:", re.findall(r"\W", "Hello there."))

# \n
# Matches the newline character.
print("Example #17:", re.findall(r"\w+\n", "Roses are red\nViolets are blue\nYou better watch out\nI'm coming for you!"))

# \s and \S
# Matches any (non) space, tab or newline character.
print("Example #18:", re.findall(r"[a-zA-Z.']+\s", "Knock knock.\nWho's there?"))
print("Example #19:", re.findall(r"\S+", "Knock knock.\nWho's there?"))

# \
# Known as the escape character. Matches the next character literally as long as it is not part of any sequence mentioned above.
print("Example #20:", re.findall(r"\[\w+\]", "There are [seventy] dogs."))

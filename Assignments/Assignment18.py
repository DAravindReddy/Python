
"""Count number of vowels in a string."""

name = "aravind"

count = 0
i = 0

while i < len(name):
    if name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] == 'o' or name[i] == 'u':
        count += 1
    i += 1

print(count)


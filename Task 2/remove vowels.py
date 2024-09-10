string = "Guvi Geeks Network Private Limited"
vowels = "aeiouAEIOU"
new_string = ''.join([char for char in string if char not in vowels])

print(new_string)
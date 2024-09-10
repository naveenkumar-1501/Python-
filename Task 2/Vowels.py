string = "Guvi Geeks Network Private Limited"
vowels = "aeiouAEIOU"
vowel_count = {vowel: 0 for vowel in vowels}

for char in string:
    if char in vowel_count:
        vowel_count[char] += 1

print(vowel_count)
from collections import Counter
# Define the string
company_name = "naveen kumar"

# Create a Counter object to count the frequency of each character
char_count = Counter(company_name)

# Find the most common characters
most_common_chars = char_count.most_common()

# Print the most frequent characters
print("Most frequent characters:")
for char, count in most_common_chars:
    print(f"Character: '{char}' - Frequency: {count}")

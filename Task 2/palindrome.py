# Define the string
sentence = "Step on no pets"

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Check if the sentence is a palindrome
result = is_palindrome(sentence)

# Print the result
print("Is the sentence a palindrome?", result)
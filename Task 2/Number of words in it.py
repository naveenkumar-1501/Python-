def count_words(string):
    # Split the string into words using whitespace as the separator
    words = string.split()
    # Return the number of words
    return len(words)

string = "Guvi Geek Network private limited"
print(f"The number of words in the string is: {count_words(string)}")

def longest_common_substring(str1, str2):
    # Initialize variables to store the longest common substring
    longest_substr = ""
    len1, len2 = len(str1), len(str2)
    
    # Iterate through each character in the first string
    for i in range(len1):
        for j in range(len2):
            # Initialize a temporary substring
            temp_substr = ""
            # Check for matching characters and build the substring
            while (i < len1 and j < len2 and str1[i] == str2[j]):
                temp_substr += str1[i]
                i += 1
                j += 1
            # Update the longest substring if the current one is longer
            if len(temp_substr) > len(longest_substr):
                longest_substr = temp_substr
    
    return longest_substr

str1 = "Guvi Geeks Network Private Limited 1"
str2 = "Guvi Zen"
result = longest_common_substring(str1, str2)
print("Longest common substring:", result)

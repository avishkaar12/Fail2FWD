def length_of_longest_substring(s):
    seen = set()  # Letters we have seen in the current substring
    left = 0      # Start position of the current substring
    max_len = 0   # Longest length found so far

    # Go through each letter in the string
    for right in range(len(s)):
        # If we see a repeat, move the start forward
        while s[right] in seen:
            seen.remove(s[left])  # Remove the old letter
            left += 1             # Move start position forward
        seen.add(s[right])       # Add the new letter
        # Update the longest length if needed
        max_len = max(max_len, right - left + 1)
    
    return max_len  # Give back the answer

# Ask the user to type a string
s = input("Enter a string: ")
# Show the answer
print(length_of_longest_substring(s))

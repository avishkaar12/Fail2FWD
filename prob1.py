def group_anagrams(words):
    anagram_map = {}  # Dictionary to group words by their sorted letters
    for word in words:
        sorted_word = ''.join(sorted(word))  # Sort letters in the word
        # If this sorted version is not in the dictionary, add it
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = []
        # Add the word to the correct group
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())
user_input = input("Enter words separated by spaces: ")
words = user_input.strip().split() 
print(group_anagrams(words))

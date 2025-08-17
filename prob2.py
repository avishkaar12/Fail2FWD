def longest_consecutive(nums):
    num_set = set(nums)  # Make a set for fast lookup
    longest = 0          # Store the longest sequence found

    # Check each number in the set
    for num in num_set:
        # If num-1 is not in the set, this is the start of a sequence
        if num - 1 not in num_set:
            length = 1  # Start counting the length
            # Keep counting up as long as the next number is in the set
            while num + length in num_set:
                length += 1
            # Update the longest sequence if this one is longer
            longest = max(longest, length)
    return longest  # Give back the answer

# Ask the user to type numbers
user_input = input("Enter numbers separated by spaces: ")
nums = list(map(int, user_input.strip().split()))  # Make a list of numbers
# Show the answer
print(longest_consecutive(nums))

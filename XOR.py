# Given string
label = "LABEL"

# XOR each character with 13
xored_chars = [chr(ord(char) ^ 13) for char in label]

# Convert the list of characters back to a string
new_string = ''.join(xored_chars)

# Format the flag
flag = f"crypto{{{new_string}}}"

# Print the flag
print(flag)

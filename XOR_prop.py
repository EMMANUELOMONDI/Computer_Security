# Define the given values
K1 = int('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313', 16)
KEY2_KEY1_XOR = int('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e', 16)
KEY2_KEY3_XOR = int('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1', 16)
FLAG_KEY1_KEY3_KEY2_XOR = int('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf', 16)

# Calculate KEY2
K2 = KEY2_KEY1_XOR ^ K1

# Calculate KEY3
K3 = KEY2_KEY3_XOR ^ K2

# Calculate FLAG
FLAG = FLAG_KEY1_KEY3_KEY2_XOR ^ K1 ^ K3 ^ K2

# FLAG to a hex string
flag_hex = hex(FLAG)[2:]

# Hexto ASCII
flag_ascii = bytes.fromhex(flag_hex).decode('utf-8')


print(f"crypto{{{flag_ascii}}}")

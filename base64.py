import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Decode the hex string to bytes
hex_bytes = bytes.fromhex(hex_string)

# Encode the bytes to Base64
base64_encoded = base64.b64encode(hex_bytes)

# Convert the Base64 bytes to a string
base64_string = base64_encoded.decode('utf-8')

print(base64_string)

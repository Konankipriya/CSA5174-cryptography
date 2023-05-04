ciphertext = "560();*;8"
mapping={
    "†": "e",
    "¶": "i",
    "(": "l",
    ")": "m",
    "*": "n",
    ";": "o",
    ":": "r",
    "]": "s",
    "[": "t",
    "5": "h",
    "4": "s",
    "6": "t",
    "8": "w",
    "0": " "
}

plaintext = ""
for char in ciphertext:
    if char in mapping:
        plaintext += mapping[char]
    else:
        plaintext += char

print(plaintext)

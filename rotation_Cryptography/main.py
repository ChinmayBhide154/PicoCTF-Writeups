raw_str = "xqkwKBN{z0bib1wv_l3kzgxb3l_555957n3}"
decoded_str = ""

for item in raw_str:
    if item == '{' or item == '}':
        decoded_str += item
    else:
        if (ord(item) < 74 and ord(item) > 64) or (ord(item) < 104 and ord(item) > 96):
            decoded_str += chr(ord(item) + 18)
        else:
            decoded_str += chr(ord(item) - 8)

print(decoded_str)

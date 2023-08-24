raw_items = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']
decoded_items = ""

for item in raw_items:
    if item == '{' or item == '}':
        decoded_items += item
    else:
        decoded_items += chr(64 + item)

print(decoded_items)


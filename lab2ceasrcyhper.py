n = int(input())
message = [char for char in input()]
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
encrypted_message = []
for char in message:
    if char in alphabet_lower:
        i = alphabet_lower.find(char)
        i = (i - n)%26
        if i < 0:
            i = i + 26
        encrypted_message.append(alphabet_lower[i])
    elif char in alphabet_upper:
        i = alphabet_upper.find(char)
        i = (i - n)%26
        if i < 0:
            i = i + 26
        encrypted_message.append(alphabet_upper[i])
print(('').join(encrypted_message))
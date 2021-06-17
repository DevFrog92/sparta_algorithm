words = "hello my name is sparta"
alphabet = [0]*26

def alphabet_occurence(words):
    for i in words:
        if not i.isalpha():
            continue
        alphabet[ord(i)-ord('a')] += 1

    max_alpha = 0
    max_index = 0
    for j in range(len(alphabet)):
        if max_alpha < alphabet[j]:
            max_alpha = alphabet[j]
            max_index = j

    return chr(max_index+ord('a'))

result = alphabet_occurence(words)
print(result)

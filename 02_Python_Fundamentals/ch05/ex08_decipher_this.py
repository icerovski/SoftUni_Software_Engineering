'''
You are given a secret message you should decipher. To do that, you need to know that in each word:
•	the second and the last letter are switched (e.g., Holle means Hello)
•	the first letter is replaced by its character code (e.g., 72 means H)
'''

def strip_number(txt):
    digit = ''
    for char in txt:
        if char.isdigit():
            digit += char
        else:
            break
    return digit

def switch_letters(txt):
    txt_list = list(txt)
    txt_list[0], txt_list[-1] = txt_list[-1], txt_list[0]
    return ''.join(txt_list)

secret_message = input().split(' ')
deciphered_message = []
for word in secret_message:
    # numbers = [s for s in word.split() if s.isdigit()]
    secret_first_letter = strip_number(word)
    first_letter = chr(int(secret_first_letter))
    secret_other_letters = word[len(secret_first_letter):]
    other_letters = switch_letters(secret_other_letters)
    deciphered_word = first_letter + other_letters
    deciphered_message.append(deciphered_word)

print(' '.join(deciphered_message))

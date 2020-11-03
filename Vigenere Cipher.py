#Preparation
letters = 'abcdefghijklmnopqrstuvwxyz'
len_letters = len(letters)

#Step 1 - input an original code
plaintext = input('Please enter a message? ').lower()
print('Plaintext: ', plaintext)

#Step 2 - input a shift and check
shift = input('Please enter one shift word? ').lower()
if shift.isalpha():
    print('Shift: ', shift)
else:
    print('Invalid shift word format! Please try again.')

#Step 3 - encrypt
len_plain = len(plaintext)
len_shift = len(shift)
quotient = len_plain//len_shift
remainder = len_plain % len_shift

trans = shift*quotient
for i in range(0,remainder):
    trans += shift[i]
print("Transition: ", trans)

encrypt = ''
for i in range(0,len_plain):
    index_letter = letters.find(plaintext[i])
    index_trans = letters.find(trans[i])
    if index_letter > -1:
        encrypt += letters[(index_letter + index_trans) % len_letters]
    else:
        encrypt += plaintext[i]
print('Encrypted: ', encrypt)

# Step 4 Decrypt
decrypt = ''
for j in range(0,len_plain):
    index_dec = letters.find(encrypt[j])
    index_trans = letters.find(trans[j])
    if index_dec > -1:
        decrypt += letters[(index_dec - index_trans) % len_letters]
    else:
        decrypt += plaintext[i]
print("Decrypted: ", decrypt)

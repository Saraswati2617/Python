'''CAESAR CIPHER'''
'''sender messages are encrypted to other form then receiver wil have to decrypt it to read it'''
'''shift key=1---a->b b->c c->d....'''

'''encryption=(X(letter)+n(shift key)%26)
    decryption=(X(letter)-n(shift key)%26)
    if want in only one function then ,if decrypt:shift key=shift key*-1'''

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(plain_text,shift_key):
    ciphertext=""
    for i in plain_text:
        if i in alphabet:
            position=alphabet.index(i)
            newposition=(position+shift_key)%26
            ciphertext+=alphabet[newposition]
        else:
            ciphertext+=i
    print(f"the encrypted msg is:{ciphertext}")

def decrypt(cipher_text,shift_key):
    plaintext=""
    for i in cipher_text:
        if i in alphabet:
            position=alphabet.index(i)
            newposition=(position-shift_key)%26
            plaintext+=alphabet[newposition]
        else:
            plaintext+=i
    print(f"the decrypted msg is:{plaintext}")

want_to_restart=True
while  want_to_restart:
    message=input("Enter your message")
    shift=int(input("Type the shift nuumber:"))
    choice=input("encrypt for encryption and decrypt for decryption")
    if choice=="encrypt":
        encrypt(message.lower(),shift)
    if choice=="decrypt":
        decrypt(message.lower(),shift)
    ask=input("Type 'Yes' to restart:")
    if ask=='Yes':
        want_to_restart=True
    else:
        want_to_restart=False
        print("Thank you for using my project!")
    
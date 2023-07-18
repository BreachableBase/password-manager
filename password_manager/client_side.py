# imports
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES 
import random
 
# constants for userID generation  yes
user_id_wordlist=['alpha','bravo',
                'charlie','delta',
                'echo','foxtrot',
                'golf','hotel',
                'india','juliett',
                'kilo','lima',
                'mike','november',
                'oscar','papa',
                'quebec','romeo',
                'sierra','tango',
                'uniform','victor',
                'whiskey','xray',
                'yankee','zulu']

user_plaintext = b'password here'
user_key = get_random_bytes(32) 

# functions
# signup using rand.randint to generate a positional index of the range user_id_wordlist
def generate_user():
    selected_wordlists=[]
    for itr in range(4):
        #index = random.randint(0,len(user_id_wordlist)-1)
        user = random.choice(user_id_wordlist)
        #selected_wordlists.append(user_id_wordlist[index])
        selected_wordlists.append(user)
    user_id = '-'.join(selected_wordlists)
    return user_id

# sending data
def aes_encrypt(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext= pad_plaintext(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return(key, ciphertext, iv)


def pad_plaintext(plaintext, block_size): 
    global padding
    rand_bytes= 16*random.randint(0,7)
    padding_bytes = block_size - len(plaintext) % AES.block_size + rand_bytes
    padding=bytes([padding_bytes])*padding_bytes 
    return plaintext + padding


def rsa_encrypt(padded_ciphertext):
    pass
 

# receving data
def unpad_plaintext(padded_plaintext):
    unpadded_plantext = padded_plaintext[:-len(padding)].decode()
    return unpadded_plantext


def aes_decrypt(ukey, ciphertext, uiv):
    cipher = AES.new(ukey, AES.MODE_CBC, uiv)
    padded_plaintext = cipher.decrypt(ciphertext)
    return padded_plaintext

# calling 
print(generate_user())
encrypted = aes_encrypt(user_plaintext, user_key)
print(encrypted)
x = aes_decrypt(encrypted[0],encrypted[1],encrypted[2])
print(x)
y=unpad_plaintext(x)
print(y)
















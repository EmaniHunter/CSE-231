#############################################################
# Computer Project 4
#
#   Alogrithm
#       import modules
#       defined functions 
#           affine cipher encryption
#           affine cipher decryption
#           caesar cipher encryption
#           caesar cipher decryption
#           main()
#              asks for input for rotation number
#              asks for command for encryption,decryption 
#              asks for input for string to encrypt, decrypt
#              loops for characters in lowercase string
#              ALPHA_NUM assigned to affine ciphers
#              PUNCTUATION assigned to caesar ciphers
#              outputs cipher text, plain text
#############################################################
import math,string #imports math and string module
PUNCTUATION = string.punctuation #assigns punctuation
ALPHA_NUM = string.ascii_lowercase + string.digits #assigns ascii letters
                                                    #and digits

def multiplicative_inverse(A,M):
    '''Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.'''
       
    for x in range(M):
        if (A*x)%M == 1:
            return x
  
def check_co_prime(num, M):
    '''Returns true if num and M are co-primes,
    uses GCD and math module,otherwise returns 
    False if not co-primes'''
    
    if math.gcd(num, M) == 1:
        return True
    else:
        return False
        
def get_smallest_co_prime(M):
    '''Returns the smallest coprime of M thats
    greater than 1'''
    
    for A in range (2, M):
        if check_co_prime(A,M) == True:
            return A
        
        
def caesar_cipher_encryption(ch,N,alphabet):
    '''Takes ch, a character to encrypt, N, the 
    rotation number, and the alphabet (a string)
    returns cipher encryption character'''
    
    M = len(alphabet)
    x = alphabet.find(ch)
    N = int(N)
    caesar_encrypt = ((x + N) % M)
    caesar_character = alphabet[caesar_encrypt]
    
    for ch in alphabet:
            return caesar_character
    

def caesar_cipher_decryption(ch,N,alphabet):
    '''Takes ch, a character to decrypt, N,
    the rotation number, and the alphabet (a string)
    returns cipher decryption character'''
    
    M = len(alphabet)
    x = alphabet.find(ch)
    N = int(N)
    caesar_decrypt = ((x - N) % M)
    caesar_character_de = alphabet[caesar_decrypt]
    
    for ch in alphabet:
            return caesar_character_de
    
        
def affine_cipher_encryption(ch,N,alphabet):
    '''Takes ch, a character to encrypt, N,
    the rotation number, and the alphabet (a string)
    returns affine cipher encryption character'''
    M = len(alphabet)
    A = get_smallest_co_prime(M)
    x = alphabet.find(ch)
    N = int(N)
    affine_encrypt = (((A * x) + N) % M)
    affine_character = alphabet[affine_encrypt]
    
    for ch in alphabet:
        if alphabet.isalnum()== True:
            return affine_character

def affine_cipher_decryption(ch,N,alphabet):
    '''Takes ch, a character to decrypt, N,
    the rotation number, and the alphabet (a string)
    returns affine cipher decryption character'''
    M = len(alphabet)
    A = get_smallest_co_prime(M)
    x = alphabet.find(ch)
    N = int(N)
    inverse_A = multiplicative_inverse(A,M)
    affine_decrypt = ((inverse_A*(x - N)) % M)
    affine_character_de = alphabet[affine_decrypt]
    
    for ch in alphabet:
        if alphabet.isalnum()==True:
            return affine_character_de

    
def main():    
    '''Prompts for rotation, N. Prompts for 
    command ((d)ecrypt, (e)ncrypt, (q)uit),
    prompts for a string, then decrypts
    or encrypts the string depending on
    command using encryption and decryption
    functions described above. PUNCTUATION assigned
    to caesar cipher and ALPHA_NUM assigned to
    affine cipher.'''
    
    N = input("Input a rotation (int): ") #rotation N

    while N.isdigit()== False: #if N is not an integer
        print("Error; rotation must be an integer." )
        N = input("Input a rotation (int): ")
    
    #input for command to encrypt, decrypt or quit the loop 
    Command = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ") 
    while Command != 'q': #while loop for when the command is not quit
        if Command == 'e': #if command is e for encrypt
            Str = input("Input a string to encrypt: ")
            cipher = '' #empty string to add characters from encryption
            for ch in Str.lower(): 
                if ch in ALPHA_NUM:
                    N = int(N)
                    alphabet = ALPHA_NUM #assign alphabet to ALPHA_NUM
                    cipher += affine_cipher_encryption(ch,N,alphabet)
             
                elif ch in PUNCTUATION:
                    N = int(N)
                    alphabet = PUNCTUATION #assign alphabet to PUNCTUATION
                    cipher += caesar_cipher_encryption(ch,N,alphabet)
        
                else: #if characters in Str are not in ALPHA_NUM OR PUNCTUATION
                    print("Error with character:  ")
                    print("Cannot encrypt this string.")
                    break
            else: #prints plain text and cipher text 
                print("Plain text:", Str)
                print("Cipher text:", cipher)
            Command = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
        
        elif Command == 'd': #if command is d for decrypt
            Str = input("Input a string to decrypt: ")
            cipher = '' #empty string to add characters from decryption
            for ch in Str.lower():
                if ch in ALPHA_NUM:
                    alphabet = ALPHA_NUM #assign alphabet to ALPHA_NUM
                    cipher += affine_cipher_decryption(ch,N,alphabet)
                
                elif ch in PUNCTUATION:
                    alphabet = PUNCTUATION
                    cipher += caesar_cipher_decryption(ch,N,alphabet)
            else: #prints cipher text and plain text
                print("Cipher text:", Str)
                print("Plain text:", cipher)
            Command = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ") 
            
        else: #if the command is not (e)ncrypt, (d)ecrypt, (q)uit
            print("Command not recognized")
            Command = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
    
if __name__ == "__main__":
    main()



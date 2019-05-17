##############################################################################
#   Computer Project 9
#       Alogrithm
#           focus: lists, functions, dictionaries
#           defined functions
#               define an open file function to open a data file that is found
#               read data function to ask for correct input, read the data
#               read file line by line, store all quadgrams with found
#               frequencies
#               calculate log probability of each quadgram
#               display top 10 quadgrams to user with the quadgrams frequency
#                   and log probability
#               decrypt the shift cipher with all keys(letters enumerated in
#                   in alphabet)
#               main() for user input 
#                   choice one to decrypt a plaintext, ciphertext with a 
#                   bifurcation number, and give text to decrypt
#                   choice two to ask for file name, print log probability of
#                       of quadgrams, cipher text input to display key, 
#                           plaintext, fitness score
#                   shows decrypted ciphertext
#           fp.close() to close file
##############################################################################
from math import log10
import string

def open_file():
     ''' Prompts for a file name and opens it if
    the file can be correctly found, loops until
    correct file can be found '''
    
     while True: #loops until correct file can be found
        file = input("Input a file name: ")
        try:
            fp = open(file, "r")
            return fp
        except FileNotFoundError: #shows error if file cannot be found
            print("Unable to open the file. Please try again.")

def chosen_plaintext_attack(plaintext, ciphertext, bifurcation, texttodecrypt):
    '''Takes four parameters, plaintext, a string,
    ciphertext, corresponding ciphertext of plaintext, as a string,
    bifurcation being size of mapping between ciphertext
    and plaintext. Prints decrypted text if
    encode/key can be found in dictionary. Prints
    error message if key cannot be found.'''
    
    D = {}
    decoded_str = ''
    for i in range((len(plaintext))):
        encode = ciphertext[i * bifurcation : (i+1) * bifurcation] #Creates encode
                                                                    #key
        decode =  plaintext[i] #decode = all of plaintext at index within the 
                                #the plaintext's length
        D[encode] = decode #sets encode key to value decode
         
    try: #TRY statement to reverse key/value pair and add that reversed key/val
        #pair to empty decoded string for the newly decrypted text
        for i in range( int(len(texttodecrypt) // bifurcation )):
            encode = texttodecrypt[(i * bifurcation) : ((i+1) * bifurcation)]  
            decode = D[encode]
            decoded_str += decode
        print("\nDecrypted text:", decoded_str)
 
    except: #KEYERROR exception, if key is not found
        print("\nDecryption interrupted. Key not found: ", encode)

def log_probability_dictionary(fp):
    '''Reads file (fp), line by line and
    builds a dictionary containing key-value pairs,
    each key being a quadgram, value being a list
    containing frequency of quadgram and calculated
    log probability. Gets top ten values, sorts in
    descending order. Returns dictionary of quadgrams'''
    
    print("\n{:<8s}{:>13s}{:>22s}".format('Quadgram','Count','Log Probability'))
    print("-------------------------------------------")    
    quadgram_dictionary = {}
    new_list = []
    total_quad = 0
    
    for line_str in fp: #goes through each in the file
        line = line_str.split() 
        quadgram = line[0].strip() #strips quadgram of space from beginning and
                                    #end but not in between
        frequency = line[1]
        frequency = int(frequency)
        quadgram_dictionary[quadgram] = [frequency] #sets quadgram as key and 
                                                    #frequency of quadgram as a
                                                    #value (and list)

        total_quad += frequency #sums all frequency
        
    for key, values in quadgram_dictionary.items():
        prob = log10(values[0]/total_quad) #creates log probability
        values.append(prob)
        new_list.append((values[0],values[1], key))
        
    new_list.sort(reverse = True) #sorts in descending order, largest--smallest
    
    #for loop going through the dictionary updating the probability value using 
    #the formula
    for i in range(10):#prints the top ten 
        print("{:<8s}{:>13d}{:>22.6f}".format(new_list[i][2],new_list[i][0], \
              new_list[i][1])) 
    
    return quadgram_dictionary

def bruteforce_shift_cipher(ciphertext, ngrams_dictionary):
    '''Takes two parameters- ciphertext and quadgram
    dictionary (given by log probability dicionary function)
    runs through every key between 0 and 25, calculates overall
    log fitness of each decryption that occurs, returns top
    5 fitness values.'''
                                                                                 
    print("{:<5s}{:^35s}   {:>10s}".format("\nKey", "Plaintext", "Fitness")) 
    print("------------------------------------------------------") 
    alphabet = string.ascii_uppercase + string.ascii_uppercase
    ciphertext = ciphertext.upper()
    fitnesslist = []
    for i in range(26): #runs through every key from 0 to 25
        plain_text = ''
        for item in ciphertext:
            index = alphabet.find(item)
            plain_text += alphabet[index + i]
        #calls fitness_calculator function
        fitness_score = fitness_calculator(plain_text, ngrams_dictionary)
        tup = (fitness_score,i, plain_text) #inputs fitness score, key, and 
                                            #plaintext into tuple
        fitnesslist.append(tup) #Adds tuple to new list
        
    fitnesslist.sort(reverse = True) #sort in descending order
    
    #print first 5 tuples in the list
    for i in range(5):
    
        print("{:<5d}{:^35s}   {:>10.4f}".format(fitnesslist[i][1], fitnesslist[i][2][:35], fitnesslist[i][0]))
    input("\npress any key to continue...")
    print("\nDecrypted ciphertext: ", fitnesslist[0][2])
        
def fitness_calculator(potential_plaintext, quadgram_dictionary):
    '''Take two parameters- potential_plaintext
    and quadgram_dictionary from log_probability_dictionary
    function. Returns sum of fitness values corresponding
    to each quadgram found in plaintext.'''

    overall_fitness = 0
    potential_plaintext = potential_plaintext.upper()
    #loops through each character in length of given plaintext
    for ch in range(len(potential_plaintext)-3):
        #index potential_plaintext to go from character and to character
        #with an addition of four-- this makes the quadgrams out of the 
        #plaintext
        quadgrams = potential_plaintext[ch:ch+4]
        quadgrams = str(quadgrams)

        if quadgrams in quadgram_dictionary:
            #sums all fitness scores for quadgrams in dictionary
            overall_fitness += quadgram_dictionary[quadgrams][1]
            
    return overall_fitness

def main():
    ''' Asks user to make a choice between
    chosen plaintext attack or Ngram frequency analysis
    attack. If user inputs choice 1, user is
    asked for plaintext, ciphertext, bifurcation number,
    text to decrypt- calls chosen_plaintext_attack()
    function. If user inputs choice 2, user is asked
    to input file name, given quadgram dictionary
    from log_probability_dictionary, asked for ciphertext 
    and given decrypted ciphertext.'''
    
    BANNER = """\
    ------------------------------------------------------------------------
    Welcome to the world of code breaking. This program is meant to help
    decipher encrypted ciphertext in absence of knowledge of algorithm/key.
    ------------------------------------------------------------------------
    """
    MENU = """\
    1. Chosen plaintext attack
    2. Ngram frequency analysis
    """
    print(BANNER)
    print(MENU)
    
    choice = input("Choice: ")
    #Loops through to see if input is not 1 or 2. Prints error statement
    while choice != '1' and choice != '2':
        print("Invalid input.")

        choice = input("Choice: ")
    #if input is 1, asked for plain and cipher text, bifurcation and text to 
    #decrypt- calls chosen_plaintext_attack to show decrypted text or key error
    if choice == '1' in MENU:
        plaintext = input("Plaintext: ")
        ciphertext = input("Ciphertext: ")
        bifurcation = input("Bifurcation: ")
        bifurcation = int(bifurcation)
        texttodecrypt = input("Text to decrypt: ")
        chosen_plaintext_attack(plaintext, ciphertext, bifurcation, texttodecrypt)
    
    #if input is 2, asked to input a file name, calls to display quadgram 
    #dictionary, asks for ciphertext input, in turn displays bruteforce cipher
    #of key, plaintext and fitness score, illustrates decrypted ciphertext
    if choice == '2' in MENU:
        fp = open_file()
        x = log_probability_dictionary(fp)
        ciphertext = input("Ciphertext: ")
        ciphertext = ciphertext.strip(" ") #strips space from beginning and end
                                            #of text
        ciphertext = ciphertext.replace(" ", "") #replaces spaces with 
                                                    #empty string
        
        ciphertext = ciphertext.strip(string.punctuation)#strips punctuation from
                                                            #beginnging/end
                                                            
        #goes through all punctuation found in string.punctuation, finds and 
        #replaces that punctuation with an empty string in ciphertext
        for punct in string.punctuation:
            ciphertext = ciphertext.replace(punct, "")
        bruteforce_shift_cipher(ciphertext, x) #call for bruteforce function
        fp.close() #closes file
if __name__ == "__main__":
    main()
            
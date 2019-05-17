#########################################################
# Computer Project 3
#
#   Alogrithm
#       Currency conversions
#           prompts for original currency 
#           prompts for new currency to convert to
#           prompts for integer amount to convert
#           rounds new currency integer two decimal places
#           prompts for outputs in real time
#       loops 
##########################################################

import urllib.request

# currency to convert from
original_currency = input("What is the original currency? " )
original_currency.upper()
#currency to convert to
converted_currency = input("What currency do you want to convert to? " )
converted_currency.upper()

#defining variable again_str for wanting to convert to another currency
again_str = 'yes' or 'YES'

while again_str == 'yes' or 'YES':
    #integer amount to convert
    amount_entered = input ("How much do you want to convert (int)? \n")
    if amount_entered.isdigit(): #assures the integer amount is a digit
        #custom url (in real time)
        url_str = \
        "https://finance.google.com/finance/converter?a={}&from={}&to={}"
        #url format to correctly prompt user input
        full_url = url_str.format(amount_entered,original_currency,\
                                  converted_currency)
  
        response = urllib.request.urlopen(full_url)
        result = str(response.read())
        
        #extracts new value from custom url with new currency
        INDEX_1 = result.find("<span class=bld>")   
        INDEX_2 = result.find("</span>")
        NEW_VALUE = result[INDEX_1:INDEX_2]
        NEW_VALUE = NEW_VALUE[16:-4]
        
        #turns new value into a float (digit with decimal)
        new_value_float = float(NEW_VALUE)
        #rounds new value 2 decimal places
        NEW_VALUE_ROUND = "{:.2f}".format(new_value_float)
        
        print(amount_entered, original_currency.upper(), "is", \
              NEW_VALUE_ROUND, converted_currency.upper())
        
        #again_str, prompting if user wants to convert to another currency
        again_str = input("Do you want to convert another currency? ")
        if again_str.lower() == 'yes': #if answer is yes 
            original_currency = input("What is the original currency? " )
            converted_currency = \
            input("What currency do you want to convert to? " )
            continue #continues the loop
        else: #if answer is anything other than yes
            break #does not prompt for more input
    else:
      #when value inputted is not an integer
      print("The value you input must be an integer. Please try again.")
      continue
    


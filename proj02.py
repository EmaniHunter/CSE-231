#################################################################
# Computer Project 2
#
#   Alogrithm
#       prompts for input of an income
#       input an integer    
#       tax calculations
#           assign tax rates based on income ranges.
#           runs tax calculations on old and new rates
#           takes the difference of old and new tax calculations
#           takes the difference percentage wise 
#           prompts for outputs
#       prompts for input of a different income
#       loops
################################################################
Income_str = input("Enter income as an integer with no commas: \n")
Income = int(Income_str)

#defining 2018 and 2017 tax variables

tax_2017 = 0

tax_2018 = 0

while Income >= 0:  #allows for only positive integers to be inputted
#2017 tax calculations
   if Income <= 9325:
       # 2017 income range for 10% tax rate
        tax_2017 = Income * 0.10  # tax_2017 variable for overall 2017 tax      
   elif 9326 <= Income <= 37950:
       # 2017 income range [9326, 37950] for 15% tax rate
        tax_2017 = (9325 * 0.10)+(0.15 * (Income - 9325))    
   elif 37951 <= Income <= 91900:
       # 2017 income range [37951, 91900] for 25% tax rate
        tax_2017 = (9325 * 0.10) + (0.15 * (28625)) \
        + (0.25 * (Income - 37950))       
   elif 91901 <= Income <= 191650:
       # 2017 income range [91901, 191650] for 28% tax rate
        tax_2017 = (9325 * 0.10) + (0.15 * (28625))+ (0.25 * (53950)) \
        + (0.28 * (Income - 91900))
   elif 191651 <= Income <= 416700:
       # 2017 income range [191651, 416700] for 33% tax rate
        tax_2017 = (9325 * 0.10) + (0.15 * (28625)) + (0.25 * (53950)) \
        + (0.28 * (99750)) + (0.33 * (Income - 191650)) 
   elif 416701 <= Income <= 418400:
       # 2017 income range [416701, 418400] for 35% tax rate
        tax_2017 = (9325 * 0.10)+ (0.15 * (28625))+ (0.25 * (53950)) \
        + (0.28 * (99750)) + (0.33 * (225050)) + (0.35 * (Income - 416700))
   elif Income > 418400:
       # 2017 income range for 39.6% tax rate
       tax_2017 = (9325 * 0.10) + (0.15 * (28625)) + (0.25 * (53950)) \
       + (0.28 * (99750)) + (0.33 * (225050)) + (0.35 * (1700)) \
       + (0.396 * (Income - 418400)) 
                   
#2018 tax calculations      
   if Income <= 9525:
            # 2018 income range for 10% tax rate
           tax_2018 = Income * 0.10 # tax_2018 variable for overall 2018 tax          
   elif 9526 <= Income <= 38700:
            # 2018 income range [9526, 38700] for 12% tax rate
            tax_2018 = (9525 * 0.10) + (0.12 * (Income - 9525))              
   elif 38701 <= Income <= 82500:
            # 2018 income range [38701, 82500] for 22% tax rate
            tax_2018 = (9525 * 0.10) + (0.12 * (29175))+ (0.22 * (Income - 38700))              
   elif 82501 <= Income <= 157500:
            # 2018 income range [82501, 157500] for 24% tax rate
            tax_2018 = (9525 * 0.10) + (0.12 * (29175)) + (0.22 * (43800)) \
            + (0.24 * (Income - 82500))                 
   elif 157501 <= Income <= 200000:
            # 2018 income range [157501, 200000] for 32% tax rate
            tax_2018 = (9525 * 0.10) + (0.12 * (29175)) + (0.22 * (43800)) \
            + (0.24 * (75000))+ (0.32 * (Income - 157500))               
   elif 200001 <= Income <= 500000:
            # 2018 income range [200001, 500000] for 35% tax rate
            tax_2018 = (9525 * 0.10) + (0.12 * (29175)) + (0.22 * (43800)) \
            + (0.24 * (75000))+ (0.32 * (42500)) + (0.35 * (Income - 200000))           
   elif Income > 500000:
            # 2018 income range for 37% tax rate
            tax_2018 = (9525 * 0.10) + (0.12 * (29175)) + (0.22 * (43800)) \
            + (0.24 * (75000))+ (0.32 * (42500)) + (0.35 * (300000)) \
            + (0.37 * (Income - 500000))     
            
   Difference = tax_2018 - tax_2017 #difference of old (2017) and new (2018) tax
   Difference_percent = ((abs (tax_2018 - tax_2017)) / tax_2017) * 100 #difference of old and new tax
                                                                       #as a percentage
   
   print("Income: \n", Income)    
   print("2017 tax:",round(tax_2017, 2))
   print("2018 tax:", round(tax_2018, 1))
   print("Difference:", round(Difference, 2))
   print("Difference (percent):", round(Difference_percent, 2))
   Income_str = input("Enter income as an integer with no commas: \n")
   Income = int(Income_str)
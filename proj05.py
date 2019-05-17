###########################################################################
#   Computer Project 5
#
#       Alogrithm
#         defined functions
#           define an open file function to open a data file that is found
#           read data function to ask for correct input, read the data
#               in the file line by line
#           calculate average happiness scores
#           display line function to display data in a table
2#           main function, ask for input, displays correct data with
#               correct input
#        close data file
###########################################################################

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
    
def read_data(fp, input_str, search_str):
    ''' Asks for fp, which points to the file, input
    which is '1' or '2' and a search keyword,
    calls display line function and calculates
    all average happiness scores'''
    
    happy_count = 0
    happiness_score_sum = 0
    fp.readline() #takes out the first line in the data display
    for line_str in fp: #goes through each line in the file
        line_list = line_str.split(',')
        country_name = line_list[0]
        region_name = line_list[1]
        happiness_score = float(line_list[2])
        
        if input_str == '1':
            if search_str.lower() in country_name.lower():
                #calls display line function to display
                display_line(country_name, region_name, happiness_score)
                #calculates average happiness scores:
                happiness_score_sum += happiness_score 
                happy_count +=1

        elif input_str == '2':
            if search_str.lower() in region_name.lower():
                #calls display line function to display
                display_line(country_name, region_name, happiness_score)
                #calculates average happiness scores:
                happiness_score_sum += happiness_score
                happy_count +=1
                
    happy_average = happiness_score_sum / happy_count
    
    print("-" *71)
    print("{:24s}{:32s}{:<17.2f}".format("Average Happiness Score"," ", \
          happy_average))
    
    
def display_line(country_name, region_name, happiness_score):
    '''Prints country names, region names and happiness
    scores values with .format statement'''
    print("{:24s}{:<32s}{:<17.2f}".format(country_name, region_name, \
          happiness_score))
    
def main():
    '''Prompts for correct inputs, asks for search keyword
    and calls read data function. Closes file'''
    
    fp = open_file()
    input_str = input( \
            "Input 1 to search in country names, 2 to search in regions: ")
    while input_str != '1' and input_str !='2': #loops until correct input
        print("Invalid choice, please try again!")
        input_str = input( \
            "Input 1 to search in country names, 2 to search in regions: ")

    search_str = input("What do you want to search for? ")
    
    print("{:24s}{:<32s}{:<17s}".format("Country", "Region", "Happiness Score"))
    print("-" *71)
    if input_str == '1':
        #calls read data function
            read_data(fp, input_str, search_str)
        #calls read data function
    elif input_str == '2':
            read_data(fp, input_str, search_str)

    fp.close() #closes data file
if __name__ == '__main__':
   main()

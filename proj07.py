##############################################################################
#   Computer Project 7
#       Alogrithm
#           focus: list/tuples, file manipulation
#           defined functions
#               define an open file function to open a data file that is found
#               read data function to ask for correct input, read the data
#                   in the file line by line
#               create a year list to get medications by year
#               calculate average prescription costs, average unit costs
#               create a list of top ten medications and prescriptions
#               create plot graph if input is positive
#               main function, ask for input, displays correct data with
#                correct input
#            closes data file
##############################################################################
from operator import itemgetter
import pylab
list_of_years = ['2011','2012','2013','2014','2015']

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

def read_data(fp):
    '''Takes a file pointer that points to a file,
    reads through each line in file, calculates
    average prescription and unit cost, creates tuple with all
    medication data, adds tuple to new list, sorts list'''
    data = []

    fp.readline()
    for line_str in fp: #reads through each line
        try:
            line = line_str.split(',') #splits at the comma, makes list
            year = int(line[0])
            brand = line[1]
            total = float(line[3])
            prescriptions = int(line[4])
            units = int(line[5])
            #AVERAGE CALCULATIONS
            avg_cost_prescription = total/ prescriptions #calculates average
                                                        #prescription cost
            avg_cost_units = total/units #calculates average unit cost
            

            medications = (year, brand, total, prescriptions, units,\
                           avg_cost_prescription, avg_cost_units)
            data.append(medications) #adds tuple to new list
        except: #if any value in the file does not have a value (i.e., N/A)
            pass       
    return sorted(data)

def top_ten_list(column, year_list):
    '''Takes two parameters: 'column' for column index
    and 'year_list' (found in get_year_list function), returns
    list with brand names of the top 10 and another list
    for values in specified column index for top 10 tuples'''
    list_1 = []
    list_2 = []
    #Sorts year list using itemgetter and reverse=true (descending order)
    sorted_yr = sorted(year_list, key = itemgetter(column-1,1), reverse=True)
    for item in sorted_yr[:10]:
        list_1.append(item[1]) #adds for item in list to new list
        
    for item in sorted_yr[:10]:
        list_2.append(item[column-1]) #adds item in list with index minus 1
        
        
    return list_1, list_2
    
def get_year_list(year, data):
    '''Takes two paraments 'year' and 'data' (from 
    read_data function, year being the specified year,
    returns a sorted list of tuples with all medications
    covered during the specified year'''
    year_list = []
    for item in data: #reads through each item in the data list
        year = int(year)
        if item[0] == year: #if item at index 0 equals year add to year_list
            year_list.append(item)
            
    return sorted(year_list)

def display_table(year, year_list):
    ''' Displays data with specified formatting, displays
    brand name, prescriptions,prescription cost and total of all'''
    print("{:^80s}".format("Drug spending by Medicaid in "+ year))
    print("{:<35s}{:>15s}{:>20s}{:>15s}".format("Medication",\
              "Prescriptions", "Prescription Cost","Total"))
    for item in year_list: #Reads through each item in the year_list
        brand = item[1]
        prescription = int(item[3])
        avg_prescription_cost = float(item[5])
        total_spending = float(item[2])
        total_spending = total_spending/1000 #divides total spending by 1000
                                            #to allow for easy reading of values
        #Formats all items for display
        print("{:<35s}{:>15,d}{:>20,.2f}{:>15,.2f}".format(brand,\
              prescription,avg_prescription_cost,total_spending))
            
def plot_top_ten(x, y, title, xlabel, ylabel):
    '''
        This function plots the top 10 values from a list of medications.
        This function is provided to the students.
        
        Input:
            x (list) -> labels for the x-axis
            y (list) -> values for the y-axis
            title (string) -> Plot title
            xlabel (string) -> Label title for the x-axis
            ylabel (string) -> Label title for the y-axis
    '''
    
    pos = range(10)
    pylab.bar(pos, y)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.xticks(pos,x, rotation='90')
    pylab.show()
    

def main():
    '''Asks for input of a specified year, if year in specified
    list of years- displays all medications with prescription and costs,
    if year input is not in list of years- returns an error, asks for
    yes or no input if user wants to plot the data of top 10 values'''
    fp = open_file()
    print("Medicaid drug spending 2011 - 2015")
    year = input("Enter a year to process ('q' to terminate): ")
    
    year_list = read_data(fp)
    
    while year != 'q':

        if year not in list_of_years: #if input is not in given list, return
                                    #error
            print("Invalid Year. Try Again!")
            year = input("Enter a year to process ('q' to terminate): ")
            continue #continues to run through each input

        if year in list_of_years: #if input is in list, display all medications
                                #Data
            x = get_year_list(year, year_list)           
            display_table(year, x)
        #If user wants to plot top 10 values data
        plot_str = input("Do you want to plot the top 10 values (yes/no)? ")
        if plot_str.lower() == 'yes': #if input is yes, calls top_ten function
            column_number = 4
            x,y = top_ten_list(column_number, year_list)
            plot_top_ten(x,y, "Top 10 Medications Prescribed in " + year, \
                         "Medication Name","Prescriptions")
            column_number2 = 3
            x, y = top_ten_list(column_number2, year_list)
            plot_top_ten(x,y, "Top 10 Medications Prescribed in " + year, \
                         "Medication Name", "Amount")

        year = input("Enter a year to process ('q' to terminate): ")

        fp.close()
if __name__ == "__main__":
    main()
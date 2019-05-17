###############################################################################
#   Computer Project 8
#       Alogrithm
#           focus: list/tuples, file manipulation
#           defined functions
#               define an open file function to open a data file that is found
#               read file function to ask for correct input, read the data
#                   in the file line by line
#                   find city, state, date, pollutant values
#                   create new dictionary with values, city, state
#               total_years function to calculate total pollution for each
#                   pollutant over 17 years
#               cities function to calculate total average pollution per city 
#                   for given state and year, returns dictionary
#               months function to calculate 4 lists of each pollutant, to find
#                   top 5 months with the greatest total pollution 
#               main() function to ask for input of state and year, calculate
#                   total years, top cities, top months, display results and 
#                   generate plot graph
#       fp.close() to close file
###############################################################################
import csv
import pylab

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
            
def read_file(fp):
    '''Takes file pointer of file, returns dictionary 
    containing all pollutant data, city name, 
    state name as a key,cdate. Ignores duplicate 
    values in the file and skips empty values'''
    
    reader = csv.reader(fp) #reads/ loops through csv file, if file has messy 
                            #numbers
    next(reader, None) #skips the header lines of file
    
    D = {}
    previous_date = ''
    previous_city = ''
    for line_list in reader:

        try:
            state_name = line_list[5]
            city = line_list[7]
            date = line_list[8]
            no2mean = float(line_list[10])
            o3mean = float(line_list[15])
            so2mean = float(line_list[20])
            comean = float(line_list[25])  
            #Turns everything that is parts per million into parts per billion
            if line_list[9] == "Parts per million":
                no2mean = no2mean * 1000
            if line_list[14] == "Parts per million":
                o3mean = o3mean * 1000
            if line_list[24] == "Parts per million":
                comean = comean * 1000
            #checks for AQI values that are not empty in the file
            if line_list[13] != '' and (line_list[18] != "") \
            and (line_list[23] != "") and (line_list[28] != ""):
                record_values = [city, date, no2mean, o3mean, so2mean, comean]
                #checks for duplicate cities and dates in the file
                if previous_date == date and previous_city == city:
                    continue
                previous_date = date
                previous_city = city
                #puts all found values in a new list
                record_values = [city, date, no2mean, o3mean, so2mean, comean]
                
                if state_name not in D:
                    D[state_name] = []
                    
                if state_name in D:
                    #appends this list of values into the new dictionary
                    D[state_name].append(record_values)

        except ValueError:
            pass
            
    return D

def total_years(D, state):
    '''Takes dictionary returned from read_file 
    and state name, calculates total pollution for
    each pollutant for the state over 17 years, pollutant
    values are summed for everyday of the year, returns
    a list containing the average pollution, max and min values'''
    
    list_of_zeros = []
    maxval = 0

    for i in range(17):
        list_of_zeros.append([0,0,0,0])
        
    for item in D[state]:
        #indexes to find the year, turns into an integer
        year = item[1][-4:]
        year = int(year)
        
        no2mean = item[2]
        o3mean = item[3]
        so2mean = item[4]
        comean = item[5]
        
        i = year % 2000
        #adds and sums pollutant values into list
        list_of_zeros[i][0] += no2mean
        list_of_zeros[i][1] += o3mean
        list_of_zeros[i][2] += so2mean
        list_of_zeros[i][3] += comean
        #finds minimum and maximum values in the list
    for item_list in list_of_zeros:
        for items in item_list:
            if items > maxval:
                maxval = items
            else:
                minval = items
    #makes new tuple containing a list of the data
    totals_list = (list_of_zeros, maxval, minval)
    return totals_list 

def cities(D, state, year):
    '''Takes the dictionary from read_file,
    state name and an integer year,finds total average
    pollution per city for a state and year, values
    get added to a new dictionary with the city as the key
    and averages as values, returns new dictionary'''
    
    D_cities = {}

    for item in D[state]:
        #indexes the year and splits into a list at the forward slash
        theyear = int(item[1].split('/')[2])
        
        if theyear == year:
            city = item[0]
            no2mean = item[2]
            o3mean = item[3]
            so2mean = item[4]
            comean = item[5]
        #adds and suns pollutant values in new dictionary with city as the key
            if city in D_cities:
                D_cities[city][0] += no2mean
                D_cities[city][1] += o3mean
                D_cities[city][2] += so2mean
                D_cities[city][3] += comean
            else:
                #makes list of pollutant values as a value in dictionary
                D_cities[city] = [no2mean, o3mean, so2mean, comean]
        
    return D_cities

def months(D,state,year):
    '''Takes dictionary from read_file and
    inputted state and year, finds top 5 months
    with greatest total pollution for each pollutant, then
    returns four lists of the pollutants with the top 5
    sorted from largest to smallest, returns all four lists
    in a tuple'''
    
    #create four new lists
    NO2 = []
    O3= []
    SO2 = []
    CO = []

    for i in range(12):
        NO2.append(0)
        O3.append(0)
        SO2.append(0)
        CO.append(0)

    for item in D[state]:
        #indexes the date, splits into a list at the forward slash
        date = item[1].split('/')
        month = int(date[0])
        theyear = int(date[2])
        
        if theyear == year:
            #adds pollutant values to specific position into each list
            NO2[month - 1] += item[2]
            O3[month - 1] += item[3]
            SO2[month - 1] += item[4]
            CO[month - 1] += item[5]
    #sorts all lists from largest to smallest
    NO2.sort(reverse=True)
    O3.sort(reverse=True)
    SO2.sort(reverse=True)
    CO.sort(reverse=True)
    #slices off at 5 to go to top 5 months
    top_months = (NO2[:5], O3[:5], SO2[:5], CO[:5])
        
    return top_months 

def display(totals_list,maxval,minval,D_cities,top_months):
    '''Displays data with specified formatting,
    returns max and min pollution values, pollution totals
    by year, pollution by city, and top months'''
    
    #displays MINIMUM and MAXIMUM pollution values
    print("\nMax and Min pollution\n")
    print("{:>10s}{:>10s}".format("Minval","Maxval"))
    print("{:>10.2f}{:>10.2f}\n".format(minval,maxval))
    
    #displays POLLUTION TOTALS by year
    print("Pollution totals by year\n")
    print("{:<6s}{:>8s} {:>8s} {:>8s} {:>10s}".format("Year", "NO2", "O3", "SO2", "CO"))
    year = 2000
    for item in totals_list:
        NO2 = item[0]
        O3 = item[1]
        SO2 = item[2]
        CO = item[3]
        
        if NO2 != 0: #ONLY IF THE VALUE IS NOT ZERO
            print("{:<6d}{:>8.2f} {:>8.2f} {:>8.2f} {:>10.2f}".format(year, NO2, O3, SO2, CO))
        year += 1 #adds 1 to the year to go through each year from 2000 to 2016
        
    #displays POLLUTION TOTALS by city
    print("\nPollution by city\n")
    print("{:<16s}{:>8s} {:>8s} {:>8s} {:>8s}".format("City","NO2", "O3","SO2","CO"))
    for key,values in D_cities.items(): #searches through all items finds key 
                                            #values
        city = key
        NO2 = values[0]
        O3 = values[1]
        SO2 = values[2]
        CO = values[3]
        print("{:<16s}{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}".format(city, NO2, O3, SO2, CO))
    #displays TOP MONTHS values
    print("\nTop Months\n")
    print("{:>8s} {:>8s} {:>8s} {:>8s}".format("NO2", "O3", "SO2", "CO"))
    for item in range(5): #goes through up to 5 to display top 5 values of
                            #pollutant values
        NO2 = top_months[0][item]
        O3 = top_months[1][item]
        SO2 = top_months[2][item]
        CO = top_months[3][item]
        print("{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}".format(NO2,O3,SO2,CO))
        
def plot_years(totals_list,maxval,minval):
    '''plots all given values'''
    
    #Creates new lists
    no2 = []
    so2 = []
    o3 = []
    co = []
    years = []

    #goes through each item in the range between 2000 and 2017 
    for i in range(2000,2017):
        years.append(i)
    #goes through each item in the totals_list to append pollutant values
    for i in totals_list:
        no2.append(i[0])
        o3.append(i[1])
        so2.append(i[2])
        co.append(i[3])
    #generates plot graph
    fig, ax = pylab.subplots()
    pylab.ylabel('Average Concentration')
    pylab.xlabel('Year')
    pylab.title('Total Average Pollution Per Year')
    ax.plot(years,no2, 'ro')
    ax.plot(years,o3, 'bo')
    ax.plot(years,so2, 'go')
    ax.plot(years,co, 'yo')
    ax.plot(years,no2, 'ro', label='NO2')
    ax.plot(years,o3, 'bo', label='O3')
    ax.plot(years,so2, 'go', label='SO2')
    ax.plot(years,co, 'yo', label='CO')


    ax.legend(loc='upper right', shadow=True, fontsize='small')

    pylab.show() #shows plot graph

def main():
    '''Asks for input of a state name and year, 
    calculates total years, top cities, top months,
    display the results of each values, then
    prompts if user wants to plot the data, generates
    graph if input is yes'''
    
    fp = open_file() #calls file pointer
    D = read_file(fp) #finds dictionary returned in read file
    state = input("Enter a state ('quit' to quit): ") #asks for specific state
    
    while state not in D and state != 'quit': #if state is not in dictionary 
                                                #and is not quit
        print("Invalid state.") #prints error statement
        state = input("Enter a state ('quit' to quit): ")

    if state == 'quit': #if state is quit, stops the program
        return
    
    year = input("Enter a year ('quit' to quit): ") #year input
    year = int(year) #turns year into an integer

    while state != 'quit' and year != 'quit': #if state and year do not equal 
                                                #quit
        x = total_years(D, state) #calls total_years function
        y = cities(D, state, year) #calls cities function
        z = months(D, state, year) #calls months function
        display(x[0],x[1], 0.00 , y, z) #displays min and max value, pollution
        #totals by year, city, and top 5 months
        plot_str = input("Do you want to plot (yes/no)? ") #asks if user wants 
                                                            #plot their data
        if plot_str.lower() == 'yes':
            totals_list = x[0] #takes index 0 of totals list 
            maxval = x[1] #finds max value
            minval = x[2] #finds min value
            plot_years(totals_list, maxval, minval) #calls plot function to 
                                                        #generate graph of values
            
        state = input("Enter a state ('quit' to quit): ")
        while state not in D and state != 'quit':
            print("Invalid state.")
            state = input("Enter a state ('quit' to quit): ")
            
        if state == 'quit':
            return
        
        year = input("Enter a year ('quit' to quit): ")
        if year == 'quit':
            return
        year = int(year)
        fp.close() #closes file


if __name__ == "__main__":
    main()          

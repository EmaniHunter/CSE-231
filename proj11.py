###############################################################################
#   Computer Project 11
#       Alogrithm
#           focus: practice classes and file handling
#           design two classes to help with reading and writing CSV files
#               two classes: Cell class and CsvWorker class
#               CsvWorker class represents a whole csv spreadsheet
#               Cell class represents one cell in the entire spreadsheet
#                   CsvWorker class contains MANY Cell objects
#           open_file() function implements and opens a correct file
#           main() function implements a smaller version of the csv spreadsheet
###############################################################################

import csv

class Cell(object):
    '''Cell class defines a cell component of a 
    CSV file/ spreadsheet (one cell that is 
    contained in the CsvWorker class.
    Has four attributes: column number, value,
    the alignment for printing, and a CsvWorker instance.'''
    def __init__(self, csv_worker = None, value = '', column = 0, alignment = '^'):
        '''This method initializes the Cell
        object and its four attributes.'''
        self.__csv_worker = csv_worker #CsvWorker instance- describes the csv
                                        #spreadsheet that the cell is in.
        self.__value = value
        self.__column = column
        self.__alignment = alignment
        
    def __str__(self):
        '''This method builds a formatted string
        to be used for printing the values.'''
        #This finds the cell width from the csv worker instance,
        #calls the CsvWorker's get_width method for width assignment
        
        new_special = self.__csv_worker.get_special(self.__column)
        if new_special:
            val = new_special((self.__value))
        else:
            val = self.__value
        W = self.__csv_worker.get_width(self.__column) 
        result ="{" + ":{}{}".format(self.__alignment, W) + "}"

        return result.format(val)

    def __repr__(self):
        ''' This method returns a shell 
        representation of a Cell object.'''
        #only calls the __str__ method and returns the value
        return self.__str__()
    
    def set_align(self, align):
        '''This method takes in an alignment
        parameter, as a string, and redefines the cell's
        alignment attribute if it is the correct
        alignment'''
        #correct alignment pertains to center, left, or right alignment
        if align.lower() == 'center':
            align = '^'
        elif align.lower() == 'right':
            align = '>'
        elif align.lower() == 'left':
            align = '<'
#            
        self.__alignment = align #Redefines the alignment attribute

        
    def get_align(self):
        ''' This method returns the object's 
        alignment'''
        return self.__alignment

    def set_value(self, value):
        '''This method takes in a new value 
        and redefines its value attribute'''
        self.__value = value
        
    def get_value(self):
        '''This method returns the object's
        value'''
        return self.__value
        
class CsvWorker(object):
    '''This class takes a csv file as input
    and then processes it. It then stores its data for
    the correct output'''
    def __init__(self, fp = None):
        '''This method initializes the worker class.
        This allows for the CsvWorker object to be 
        instantiated with a file pointer (to be processed).
        It contains five attributes- columns, rows, data,
        widths and special.'''
        self.__column = 0 #represents the size of the CSV table in the file 
                            #column wise
        self.__row = 0 #represents the size of the CSV table in the file
                        #row wise
        self.__data = [] #contains all data in the CSV file
        self.__widths = [] #defines the formatted width of each column
        self.__special = [] #list of functions defining the special formatting
                            #functions for each column
        if fp: #if the file pointer is SOMETHING, it will be read and
                        #processed in the read_file function/method
            self.read_file(fp)
            
    def read_file(self, fp):
        '''This method passes in a file pointer,
        for a CSV file and iterates over the file. All five
        attributes: columns, rows, widths, special 
        and data are to be filled and stored.'''
        self.__column = 0
        self.__data = []
        self.__row = 0
        self.__widths = []
        self.__special = []
        reader = csv.reader(fp)
        for line in reader:
            #determines number of rows in the file
            self.__row += 1
            row_list = []
            column_count = 0
            for val in line:
                val = val.strip()
                   #if the value has an empty value/ no value in the file,
                #it will be an empty cell- containing an empty string
                if val == 'NULL':
                    val = ''

                #adds zeros to the widths attribute if the column count
                #is greater than or equal to the len of the width
                if column_count >= len(self.__widths):
                    self.__widths.append(0)
                
                #stores the width of the widest element in each column:
                width = len(val)
                
                if width > self.__widths[column_count]:
                    self.__widths[column_count] = width
                #call the Cell class

                cell = Cell(self,val, column_count)
                column_count +=1 #count columns for column values
                #adds the new cell calss containing the new values to a list
                row_list.append(cell)
                
            #determines the column values from the number of columns in file
            
            if column_count >= self.__column:
                self.__column = column_count  #redefines the column attribute
                                            #to the new value of columns
            self.__data.append(row_list)
            for i in range(self.__column): #for every item in the range of the 
                                               #number of columns, the special 
                                            #attribute is consisted of NONE
                self.__special.append(None) 
    
            for row in self.__data: #iterates through all values in the data
                if len(row) < self.__column:  #if the len of the row in the data is
                                                #less than the columns value
                    #the row (list) will add the Cell class,with new 'values'
                    #for its attributes- for every item within the range of the
                    #length of the row and the column values
                    row += [Cell(self,'',i) for i in range(len(row),self.__column)]
        
        fp.close() #closes file (pointer)
            
    def __getitem__(self, index):
        '''This method overloads the empty list
        operator to allow for one to access (and return)
        the values in the data attribute'''
        #the data list indexed at a certain inputted index
        return self.__data[index]
    
    def __setitem__(self, index, value):
        '''This method overloads the empty list
        operator to allow for one to set values
        in the data attribute''' 
        #the data list indexed at a certain inputted index
        self.__data[index] = value
    
    def __str__(self):
         '''This method allows for the csv
         class to convert data to a string (to be printed).'''
         empt_str = '' #Creates new empty string for data to be inputted
         for row in self.__data: #iterates through each row in the data list
             for item in row: #goes through each item within the row
                 empt_str += str(item) #adds the item as a string to the
                                         #empty string 
             empt_str += "\n" #Adds a new line character to print a new line
                                 #for each item
         return empt_str
                 
        #x = csvworker()
        #print(x)
        
    def __repr__(self):
        '''This method returns a shell representation
        of a CsvWorker object, calls the __str__ method'''
        return self.__str__()
        
    def limited_str(self, limit):
        '''This method passes in a limit parameter,
        that limits the number of lines to be 
        printed. It prints the maximum of limit number
        of lines. It allows the user to see
        a smaller portion of the data'''
        number = 0 #initializes a value of zero 
        empt_str2 = ''
        if limit == None:
            limit = len(self.__data)
            
        for row in self.__data:
            number += 1 #for each item in the row, 1 is added to the 
                                 #initialized value of zero
            for item in row:
                empt_str2 += str(item)
            empt_str2 += "\n" #adds a newline character to print a newline
                                 #for each item
            if number == limit: #if the initialized value that was add
                                     #(as a counter), is greater than the
                                     #limit, break the loop
                break
            
        return empt_str2
    
    def remove_row(self, index):
        '''This method removes a row from the data
        attribute at a specific index and
        takes one off of the row attribute.'''
        self.__data.pop(index)
#        self.__row -= 1
    
    
    def set_width(self, index, width):
        ''' This method sets the width of the column
        of the data attribute at a specific index.
        Goes through the width attribute at a certain index
        and reassigns the attribute to the width parameter.'''
        self.__widths[index] = width
        
    def get_width(self, index):
        '''This method returns the value/
        information about the width of any column 
        at a certain index within the width attribute'''
        return self.__widths[index]
        
    def set_special(self, column, special):
        '''This method links a special formatting
        function (percentage or currency) to the specific
        column.'''

        self.__special[column] = special

    def get_special(self, column):
        '''This method returns the special
        formatting function that was assigned
        to a specific column'''
        
        return self.__special[column]
        

    def set_alignment(self, column, align):
        '''This method sets the alignment of
        a specified column by providing a string
        value alignment such as center/right/left.'''
        if align == '^':
            new_align = 'center'
        elif align == '>':
            new_align = 'right'
        elif align == '<':
            new_align = 'left'
#                or align == '<':
        else: #if alignment is not one of the 3 valied alignments
                    #a typeerror is raised
            raise TypeError
            
        for row in range(len(self.__data)): #loops through each row in
                                    #the range of the length of all data
            for col in range(len(self.__data[row])): #loops through each
                                        #column in the range of the 
                                        #length of the data at the row 
                if col == column:                          #index
                    self.__data[row][col].set_align(new_align) #calls set_align from
                                                    #cell class
    def get_columns(self):
        '''This method returns number
        of columns in the CsvWorker object class'''
        return self.__column
    
    def get_rows(self):
        '''This method returns number of
        rows in the CsvWorker object class'''
        return self.__row
        
    def minimize_table(self, columns):
        '''This method returns a new CsvWorker object,
        a minimized version of the original CsvWorker 
        (and its attributes)'''
        csv_worker = CsvWorker() #creates a new CsvWorker instance
        data_new = [[] for i in range(self.__row)]
        #adds new width val
        #at the index to the new
        #instance 'list'
        csv_worker.__widths = [self.__widths[i] for i in columns]
        
        for row in range(self.__row): #loops through each row in the range
                                        #of the number of rows
            count = 0 
            for col in columns: #iterates through the index within the 
                                #columns (given & passed into the function)
                #Calls cell class, passes in new
                #instance of csv_worker and the indexed
                #Data values (creating new cell)
                
                #self.__data[row][col] #indexes the data values at the
                                    #row index and index within column
                data_new[row].append(Cell(\
                        csv_worker, self.__data[row][col].get_value(),\
                        count, self.__data[row][col].get_align()))
                
                count += 1
                
            csv_worker.__data = data_new
            csv_worker.__row = self.__row
            csv_worker.__column = len(columns)
            
            #Adds new special,at the index to the new instance 'list'
            csv_worker.__special = [self.__special[i] for i in columns]

        return csv_worker
             
    def write_csv(self, filename, limit = None):
        '''This method writes the data into a 
        CSV file named by a filename parameter. The
        values within the file are only written. The
        limit parameter limits the number of rows to
        be written in the CSV file'''
        fp = open(filename, "w", encoding = "utf-8")
        if limit != None: #if the limit is none
            count = 0 #the limit will be assigned to the length of the data list
#            limit = len(self.__data)
#            row_count = 0
        for row in self.__data: #loops through the rows in the data list
#            if limit >= 0: #if the limit is greater than or eqaul to zero,
                            #the limit number will be subtracted by 1
#                limit -= 1
            new_row_str = '' #Creates empty string to be added to 
#                row_str = ''
#                row_count += 1
            for col in row: #loops through each column in every row
                if col == 'NULL':
                    col = ''
                cell_string = str(col.get_value()) #creates a new string, by
                cell_string += ','                   #obtaining the value, 
                                            #calling the get_value function
                new_row_str += cell_string  #adds the new string
                                        #to the empty string, and 
                                        #concatenates a comma to each
            fp.write(new_row_str[:-1] + '\n') #does not account for
                                        #last comma, adds a newline 
                                    #Character to the string
            if limit != None:
                count +=1
                if count >= limit:
                    break
#            else: #if the limit is something is not greater than or equal to
                #zero
#                break #breaks the loop

        fp.close() #closes the file

    def write_table(self, filename, limit = None):
        '''This method writes data into a formatted
        text file named filename. The number of rows to be 
        written is controlled by the limit parameter (that
        is passed in)'''
        #opens a file:
        fp = open(filename, "w")
        #writes the file , calling the limited_str function
        fp.write(self.limited_str(limit))
        #closes file
        fp.close()
        
    def minimum(self, column):
        '''This method returns the cell with 
        the smallest value (minimum) of a column.'''
        min_val = 1000000000000000 #a large value to be compared
        cell = None
        for row in self.__data: #for each item in the data list

            try:
                val = row[column].get_value() #the value is the item indexed 
                                        #at a specific column, calls the
                                        #get_value function to grab the value
                #if the value is a digit,turn it into a float
                val = float(val)
                if val < min_val: #if the value is smaller than the
                            #minimum value, the minimum value is the
                            #value
                    min_val = val
                    cell = row[column]
#                return cell
            except ValueError: #raises ValueError if the value
                                #cannot be converted to a float
                continue
        return cell
        
    def maximum(self, column):
        '''This method returns the cell
        with the largest value(maximum) of a column.'''
        max_val = -1 #a small value to be compared
        cell = None
        for row in self.__data: #for each item in the data list
            
            try:
                val = row[column].get_value() #the value is the item indexed at
                                    #a specific column, calls the get_value
                                    #function to grab the value
                 #if the value is a digit, turn it into a float
                val = float(val)
                if val > max_val: #if the value is greater than the 
                            #maximum vale, the maximum value is now the 
                            #value
                    max_val = val
                    cell = row[column]
#                return cell
            except ValueError: #raises ValueError if the value
                                #cannot be converted into a float
                continue
        return cell
      
def open_file():
     ''' Prompts for a file name and opens it if
    the file can be correctly found, loops until
    correct file can be found '''
    
     while True: #loops until correct file can be found
        file = input("Input a file name: ")
        try:
            fp = open(file, "r", encoding="utf-8")
            return fp
        except FileNotFoundError: #shows error if file cannot be found
            print("File not found. Try again")
            
def percentage(value):
    '''This function passes in a float
    value parameter. It will convert the value into
    percentage format with one decimal place.'''
    try:
        value = float(value) #converts the value into a float
        return "{:.1f}%".format(value) #format the value percentage wise
    except ValueError: #Raises ValueError if the value is not a float
        return value #returns the value unchanged(unformatted)
    
def currency(value):
    '''This function passes in a float value
    parameter. It will convert the value into 
    currency format with two decimal places.'''
    try:
        value = float(value) #converts the value into a float
        return "${:,.2f}".format(value) #format the value , currency wise
    except ValueError: #Raises ValueError if the value is not a float
            return value #returns the value unchanged(unformatted)

def main():
    '''This function calls to open the file,
    instantiates a CsvWorker with the input file and 
    minimizes it to contain specific columns (7). Percentage
    columns are formatted as percentages, currency columns 
    formatted as currency.'''

    fp = open_file()
    
    master = CsvWorker(fp)

    csv_worker = master.minimize_table([3,5,40,55,116,118,122])

    csv_worker.set_special(3, percentage) #percentage columns formatted as %
    csv_worker.set_special(6, percentage)
    csv_worker.set_special(4, currency) #currency columns formatted as $
    csv_worker.set_special(5, currency)
    
    for i in range(len(csv_worker[0])):
        csv_worker.set_width(i, csv_worker.get_width(i) + 4)
    
    csv_worker.write_table("output.txt",10) #Data written to text format
    csv_worker.write_csv("output.csv", 10) #data written to csv format

    max_act = csv_worker.maximum(2) #calls maximum method
    min_act = csv_worker.minimum(2) #calls minimum method
    
    max_earn = csv_worker.maximum(4) #calls maximum method
    min_earn = csv_worker.minimum(4) #calls minimum method

    print("Maximum ACT:", str(max_act).strip())
    print("Minimum ACT:", str(min_act).strip())
    print("Maximum Earnings:", str(max_earn).strip())
    print("Minimum Earnings:", str(min_earn).strip())

if __name__ == "__main__":
    main()

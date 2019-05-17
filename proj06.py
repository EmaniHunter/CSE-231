##############################################################################
#   Computer Project 6
#
#       Alogrithm
#           focus: tuples/lists
#           defined functions
#               define an open file function to open a data file that is found
#               read data function to ask for correct input, read the data
#                   in the file line by line
#               extract gene information for specific and all chromosomes
#               calculate gene length, average gene length, standard deviation
#               display data function to display results
#               main function, ask for input, displays correct data with
#                correct input
#            closes data file
##############################################################################

import math
CHROMOSOMES = ['chri','chrii','chriii','chriv','chrv','chrx']

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
            print("Unable to open file.")

def read_file(fp):
    ''' Takes a file pointer that points to a file,
    reads all genes information in the file,
    saves each gene in a tuple, tuple is added
    to a list and then sorted '''
    
    new_list = []
    for line_str in fp: #goes through each line in the file
        line = line_str.strip().split('\t')
    
        #avoids all lines with '#' in beginning of file
        if line_str.startswith('#'):
            continue
        chromosome = line[0]
        gene_start = int(line[3])
        gene_end = int(line[4])

        genes = (chromosome,gene_start,gene_end) #saves each gene into tuple
        new_list.append(genes) #add tuple to list
    
    new_list.sort() #sorts the new list
    return new_list

def extract_chromosome(genes_list, chromosome):
    '''Receives list of genes and chromosome name,
    takes and extracts gene information for specific
    chromosome, saved in a list (chrom_gene_list)
    and sorted'''
    
    chrom_gene_list = []
    for item in genes_list:
        if item[0] == chromosome:
            chrom_gene_list.append(item) #adds item (gene info) to list
            
    chrom_gene_list.sort() #sorts list
    return chrom_gene_list
            
def extract_genome(genes_list):
    ''' Receives list of genes and takes and extracts
    all gene information for each chromosome, saved in 
    a list (genome_list) and sorted'''
    
    genome_list = []
    for item in CHROMOSOMES:
        #calls extract_chromosome function to extract all gene information
        #for each chromosome
        extraction_list = extract_chromosome(genes_list, item)
        genome_list.append(extraction_list) #adds gene info to list
        
    genome_list.sort() #sorts list
    return genome_list

def compute_gene_length(chrom_gene_list):
    ''' Receives the list of genes for a specific 
    chromosome (chrom_gene_list), computes gene length
    for each gene, saved in a list (gene_length),
    computes average gene length and standard
    deviation with the saved list, results saved in
    a tuple'''
    
    gene_length = []
    sum_length = 0
    for item in chrom_gene_list:
        gene_start = int(item[1])
        gene_end = int(item[2])
        gene_len = (gene_end-gene_start) + 1 #determines the length of one gene
        gene_length.append(gene_len) #adds the length to list

    #determines average length of all genes:
    gene_mean = (sum(gene_length))/ len(gene_length) 
    for item in gene_length:
        #finds summation of gene length minus average and sets to the power of 2
        sum_length += ((item)-gene_mean)**2
        
    #determines standard deviation
    gene_stddev = math.sqrt(sum_length/ len(gene_length))
    gene_list = (gene_mean, gene_stddev) #turns results into tuple
    return gene_list

def display_data(chrom_gene_list, chrom):
    ''' Receives list (chrom_gene_list), and chrom, a string
    name for specific chromosome, displays chromosome name,
    average length of gene and standard deviation'''
    
    #calls compute_gene_length function to be displayed
    length_genes = compute_gene_length(chrom_gene_list)
    first_3_chrom = chrom[:3].lower() #displays first 3 characters in lowercase
    last_chrom = chrom[3:].upper() #displays remaining characters in uppercase
    chrom = first_3_chrom + last_chrom
    
    print("{:<11s}{:9.2f}{:9.2f}".format(chrom,length_genes[0],length_genes[1]))

def main():
    ''' Asks for input, a specific chromosome name,
    all for all chromosomes or quit to quit the program,
    prints chromosome, mean and standard deviation of input
    prints error if input is not a specific chromosome name or
    not 'all' chromosomes'''
    
    print("Gene length computation for C. elegans.\n")
    fp = open_file()
    chrom = input("\nEnter chromosome or 'all' or 'quit': ")
    chrom_gene_list = read_file(fp)
    chrom = chrom.lower()
    while chrom.lower() != 'quit':
        chrom = chrom.lower()
        if chrom.lower() not in CHROMOSOMES and chrom.lower() != 'all':
            #prints error statement if input is not specific chromosome or all
            print("Error in chromosome.  Please try again.")
            chrom = input("\nEnter chromosome or 'all' or 'quit': ")
            continue
        print("\nChromosome Length")
        print("{:<11s}{:>9s}{:>9s}".format("chromosome","mean","std-dev"))
        
        #displays specific chromosome and its mean and standard deviation
        if chrom.lower() in CHROMOSOMES:
            x = extract_chromosome(chrom_gene_list, chrom)
            display_data(x, chrom)
            
        #displays all chromosomes and their means and standard deviations
        elif chrom.lower() == 'all':
            for i in CHROMOSOMES:
                compute_gene_length(chrom_gene_list)
                compute_gene_length(chrom_gene_list)
                compute_gene_length(chrom_gene_list)
                compute_gene_length(chrom_gene_list)
                compute_gene_length(chrom_gene_list)
                compute_gene_length(chrom_gene_list)
                x = extract_chromosome(chrom_gene_list, i)
                display_data(x, i)

        chrom = input("\nEnter chromosome or 'all' or 'quit': ")
    fp.close() #closes file
if __name__ == "__main__":
    main()
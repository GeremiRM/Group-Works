
def main(): 

    # Gets the file name from the user 
    filename = input('Enter the name of the file: ')

    # Opens the file in read mode
    infile = open(filename, 'r')
    
    # Starts at line number one
    line_number = 1
    
    # Loops through and reads every line in the file starting at 1
    for line in infile:
        print(f"{line_number}: {line.rstrip()}")
        line_number += 1
    
    # Closes file once done
    infile.close()

if __name__ == "__main__":
    main()
    

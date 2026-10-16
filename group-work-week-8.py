
# Takes a list of numbers and a number as params
# Returns a list of numbers bigger than the number given
def get_larger_than_list(num_list, number): 
    
    # Initialize larger-than list
    list_larger_than = [] 
    
    # Loop through num_list
    for elem in num_list: 
        
        # If number in list is larger than
        if(elem > number):
            
            # Add it to list
            list_larger_than.append(elem)
    
    # Once done, return list
    return list_larger_than


# Takes number of elements in list and returns list of numbers
# User inputs numbers one by one, stored in num_list
# Returns list of numbers 
def get_num_list(num_of_elems): 
    
    # Initialize numbers list
    num_list = []
        
    # Loop through
    for i in range(num_of_elems): 
        
        # User inputs number
        elem = int(input('Enter number: '))
        
        # Add it to list
        num_list.append(elem)
    
    # Return numbers list
    return num_list
    


def main(): 
    try:
    # Gets the number of elements in the list
        num_of_elems = int(input('Enter here how many numbers you would like to enter into a list? '))
        
        # If number of elements is less than 0
        if(num_of_elems < 1): 
            # Raise exception 
            raise ValueError('Number of elements has to be bigger than 0')

        # Get numbers list
        print('Please enter the numbers you would like to make into a list, one at a time')
        num_list = get_num_list(num_of_elems)
    
        # Get number to compare
        print('Please enter a whole number, ideally between the range of number values entered into the previous list.')
        comparison_number = int(input('Enter number n: '))
        
        # Get list with larger than 'comparison_number' numbers
        larger_than_list = get_larger_than_list(num_list, comparison_number)
        
        # Print list of numbers
        print(f'List of numbers entered\n{num_list}')
        
        # If larger than list is populated
        if(len(larger_than_list) > 0): 
            
            # Print results
            print(f'List of numbers that are larger than {comparison_number}:')
            print(larger_than_list)
            
        # Otherwise (no larger numbers found)
        else: 
            print(f'No numbers larger than {comparison_number} found')
    
    # If ValueError is raised (eg num_of_elements < 0 )       
    except ValueError as e:
        # handle it 
        print('Error: ', e)
        
    
if __name__ == '__main__': 
    main()
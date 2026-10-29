
# Constant with Months names
# Index correspond to number of the month - 1
# Eg: March is month 3, but has an index of 2. So subtract 1 to get right month  
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']

def main():
    try: 
        # Get date from user
        date = input('Enter a date in the format mm/dd/yyyy: ')
        
        # Split date into a list
        split_date = date.split('/')
        
        # If not in correct format, raise error
        if len(split_date) != 3: 
            raise ValueError
        
        # Get month name with month number - 1
        month = MONTHS[int(split_date[0]) - 1]
        
        # Get day. Convert to int so it prints as, for example, 5 instead of 05
        day = int(split_date[1])
        
        #Get year
        year = split_date[2]
        
        # Print
        print(f'{month} {day}, {year}')
    
    except ValueError:
        print('Wrong Format. Try again') 
    
if __name__ == '__main__': 
    main()
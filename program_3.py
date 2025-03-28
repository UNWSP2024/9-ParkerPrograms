# Nathan Parker
# 03/28/25
# Program #3: Average Numbers

# define the main function
def main():

    # perform the following code if it does not raise an exception
    try:
        # set the accumulator to 0
        accumulator = 0

        # open numbers.txt
        nums = open('numbers.txt', 'r')

        # loop over the numbers in the file
        for num in nums:

            # convert the numbers to integers
            int_num = int(num)

            # display the numbers
            print(int_num)

            # add the numbers
            accumulator += int_num

        # close the file
        nums.close()

        # display the sum of the numbers
        print(f'The sum of the numbers is {accumulator}.')

    # catch errors
    except IOError:
        print('An error occured trying to read the file.')
    except ValueError:
        print('Non-numeric data found in the file.')
    except:
        print('An error occured.')

# call the main function
if __name__ == '__main__':
    main()


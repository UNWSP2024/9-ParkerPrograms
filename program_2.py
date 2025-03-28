# Nathan Parker
# 03/28/25
# Program #2: Random Number File Writer

# define the main function
def main():

    # import the random module
    import random

    # create a file named random_numbers.txt or clear its existing data
    rand_num_file = open('random_numbers.txt', 'w')

    # define the nums variable
    nums = 1001

    # while nums is greater than 1000, get a number from the user
    while nums > 1000:
        nums = int(input('Enter how many random numbers should be added to the file (up tp 1000): '))

    # fill the file with the desired number of random numbers
    for num in range(nums):
        rand_num_file.write(f'{random.randint(1,500)}\n')

    # close the file
    rand_num_file.close()

# call the main function
if __name__ =='__main__':
    main()


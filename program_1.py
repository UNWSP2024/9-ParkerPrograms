# Nathan Parker
# 03/28/25
# Program #1: Item Counter

# define the main function
def main():

    # set the accumulator to 0
    accumulator = 0

    # open names.txt to read
    names = open('names.txt', 'r')

    # count the number of names in names.txt
    for name in names:
        accumulator += 1

    # display the number of names in names.txt
    print(f'There are {accumulator} names in names.txt.')

    # close names.txt
    names.close()

# call the main function
if __name__ == '__main__':
    main()


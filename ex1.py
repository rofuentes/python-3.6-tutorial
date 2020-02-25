import argparse
from sys import exit

def ex_1():
    print("Hello World!")
    # Immediately terminate the program.
    if args.single == True:
        exit()
    print("Hello Again")
    print("I like typing this.")
    print("This is fun.")
    print('Yay! Printing.')
    print("I'd much rather you 'not'.")
    #print('I "said" do not touch this.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Learn print function.')
    parser.add_argument('-s', '--single', action='store_true', 
                        help='limit output to a single line')
    args = parser.parse_args()
    ex_1()
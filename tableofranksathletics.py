import sys


def errorage():
    if a > 120 or a < 1:
        print('Are you idiot?')

def checkingman60m():
    if r <= 9.54 and r > 8.94:
        if a >= 10:
            print(n + ', your sports category: III youth')
        else:
            print(n + ', your sports category is III youth, but you cannot be assigned because your age is less than 10 years old.')
    elif r <= 8.94 and r > 8.44:
        if a >= 10:
            print(n + ', your sports category: II youth')
        else:
            print(n + ', your sports category is II youth, but you cannot be assigned because your age is less than 10 years old.')
    elif r <= 8.44 and r > 8.04:
        if a >= 10:
            print(n + ', your sports category: I youth')
        else:
            print(n + ', your sports category is I youth, but you cannot be assigned because your age is less than 10 years old.')
    elif r <= 8.04 and r > 7.64:
        if a >= 10:
            print(n + ', your sports category: III')
        else:
            print(n + ', your sports category is III, but you cannot be assigned because your age is less than 10 years old.')
    elif r <= 7.64 and r > 7.34:
        if a >= 10:
            print(n + ', your sports category: II')
        else:
            print(n + ', your sports category is II, but you cannot be assigned because your age is less than 10 years old.')
    elif r <= 7.34 and r > 7.04:
        if a >= 10:
            print(n + ', your sports category: I')
        else:
            print(n + ', your sports category is I, but you cannot be assigned because your age is less than 10 years old.')
    elif r <= 7.04 and r > 6.78:
        if a >= 14:
            print(n + ', your sports category: Candidate for Master of Sports')
        else:
            print(n + ', your sports category is Candidate for Master of Sports, but you cannot be assigned because your age is less than 14 years old.')
    elif r <= 6.78 and r > 6.60:
        if a >= 15:
            print(n + ', your sports category: Master of Sports')
        else:
            print(n + ', your sports category is Candidate for Master of Sports, but you cannot be assigned because your age is less than 15 years old.')
    elif r <= 6.60:
        if a >= 16:
            print(n + ', your sports category: Master of Sports of international class')
        else:
            print(n + ', your sports category is Candidate for Master of Sports of international class, but you cannot be assigned because your age is less than 16 years old.')


if __name__ == '__main__':
    n = input('Enter your name: ')
    a = int(input('Enter your age: '))
    g = int(input('Choose your gender: Man - 1; Woman - 2: '))
    d = int(input('Enter your distance: '))
    r = float(input('Enter your result: '))

    errorage()

    if g == 1 and d == 60:
        checkingman60m()
    else:
        sys.exit('You enter incorrect value')
import sys


def enter_age():
    while True:
        try:
            age = int(input('Enter your age: '))
            if 5 <= age <= 100:
                return age
            else:
                print('Age could be from 5 to 100')
        except ValueError:
            print('Enter an integer')


def check_man_60m(age, name):
    categories = [
        (9.54, 8.94, 10, 'III youth'),
        (8.94, 8.44, 10, 'II youth'),
        (8.44, 8.04, 10, 'I youth'),
        (8.04, 7.64, 10, 'III'),
        (7.64, 7.34, 10, 'II'),
        (7.34, 7.04, 10, 'I'),
        (7.04, 6.78, 14, 'Candidate for Master of Sports'),
        (6.78, 6.60, 15, 'Master of Sports'),
        (6.60, -float('inf'), 16, 'Master of Sports of international class')
    ]
    for upper, lower, min_age, category in categories:
        if upper >= result > lower:
            if age >= min_age:
                return f'{name}, your sports category: {category}'
            else:
                return f'{name}, your sports category is {category}, but you cannot be assigned because your age is ' \
                       f'less then {min_age} years old'


def check_man_100m(age, name):
    categories = [
        (15.64, 14.64, 10, 'III youth'),
        (14.64, 13.74, 10, 'II youth'),
        (13.74, 12.84, 10, 'I youth'),
        (12.84, 12.04, 10, 'III'),
        (12.04, 11.44, 10, 'II'),
        (11.44, 10.94, 10, 'I'),
        (10.94, 10.55, 14, 'Candidate for Master of Sports'),
        (10.55, 10.28, 15, 'Master of Sports'),
        (10.28, -float('inf'), 16, 'Master of Sports of international class')
    ]
    for upper, lower, min_age, category in categories:
        if upper >= result > lower:
            if age >= min_age:
                return f'{name}, your sports category: {category}'
            else:
                return f'{name}, your sports category is {category}, but you cannot be assigned because your age is ' \
                       f'less then {min_age} years old'


def check_man_200m(age, name):
    categories = [
        (34.24, 30.74, 10, 'III youth'),
        (30.74, 28.24, 10, 'II youth'),
        (28.24, 26.24, 10, 'I youth'),
        (26.24, 24.54, 10, 'III'),
        (24.54, 23.24, 10, 'II'),
        (23.24, 22.24, 10, 'I'),
        (22.24, 21.30, 14, 'Candidate for Master of Sports'),
        (21.30, 20.65, 15, 'Master of Sports'),
        (20.65, -float('inf'), 16, 'Master of Sports of international class')
    ]
    for upper, lower, min_age, category in categories:
        if upper >= result > lower:
            if age >= min_age:
                return f'{name}, your sports category: {category}'
            else:
                return f'{name}, your sports category is {category}, but you cannot be assigned because your age is ' \
                       f'less then {min_age} years old'


if __name__ == '__main__':
    name = input('Enter your name: ')
    age = enter_age()
    gender = int(input('Choose your gender: Man - 1; Woman - 2: '))
    distance = int(input('Enter your distance: '))
    result = float(input('Enter your result: '))

    if gender == 1 and distance == 60:
        print(check_man_60m(age, name))
    elif gender == 1 and distance == 100:
        print(check_man_100m(age, name))
    elif gender == 1 and distance == 200:
        print(check_man_200m(age, name))
    else:
        sys.exit('You enter incorrect value')

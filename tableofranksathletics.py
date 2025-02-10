import sys

from table_of_results import results_run


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


def enter_gender():
    while True:
        try:
            gender = int(input('Choose your gender: Man - 1; Woman - 2: '))
            if 2 < gender < 1:
                return gender
            elif gender == 1:
                return 'men'
            else:
                return 'women'
        except ValueError:
            print('Enter an integer')


def check_man_run(age, name, gender):
    categories = results_run.get(gender, {}).get(distance)

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
    gender = enter_gender()
    distance = int(input('Enter your distance: '))
    result = float(input('Enter your result: '))
    print(check_man_run(age, name, gender))

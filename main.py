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
            if gender == 1:
                return 'men'
            elif gender == 2:
                return 'women'
            else:
                continue
        except ValueError:
            print('Enter an integer')


def enter_distance():
    while True:
        try:
            list_distance = {60, 100, 200, 400, 800}
            distance = int(input('Enter your distance: '))
            if distance in list_distance:
                return distance
            else:
                print('Enter correct distance')
        except ValueError:
            print('Enter an integer')


def check_run(name, age, gender, distance):
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
    distance = enter_distance()
    result = float(input('Enter your result: '))
    print(check_run(name, age, gender, distance))

from table_of_results import results_sport


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
            list_distance = results_run['men'].keys()
            distance = int(input('Enter your distance: '))
            if distance in list_distance:
                return distance
            else:
                print('Enter correct distance')
        except ValueError:
            print('Enter an integer')


def enter_result():
    while True:
        result = input('Enter your result in the format 00:00:00.00/00:00.00/00.00: ')
        if ':' in result:
            result_in_parts = result.split(':')
            try:
                if len(result_in_parts) == 2:
                    minutes = int(result_in_parts[0])
                    seconds = float(result_in_parts[1])
                    result_seconds = minutes * 60 + seconds
                elif len(result_in_parts) == 3:
                    hours = int(result_in_parts[0])
                    minutes = int(result_in_parts[1])
                    seconds = float(result_in_parts[2])
                    result_seconds = hours * 60 + minutes * 60 + seconds
                else:
                    print('Incorrect time format')
                    continue
            except ValueError:
                print('Enter an float')
                continue
        else:
            try:
                result_seconds = float(result)
            except ValueError:
                print('Enter a valid number for seconds')
                continue

        return result_seconds


def check_result(name, age, gender, distance, result):
    categories = results_sport.get(gender, {}).get(distance)
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
    result = enter_result()
    print(check_result(name, age, gender, distance, result))

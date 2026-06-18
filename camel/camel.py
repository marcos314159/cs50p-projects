def main():
    name_convert = {'name': 'name',
            'firstName': 'first_name',
            'preferredFirstName': 'preferred_first_name'
            }
    name = input('camelCase: ')
    print('snake_case:', name_convert[name])


main()

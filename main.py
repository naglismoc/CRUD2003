from db_CRUD import *

dishes = load_dishes()
id_counter = 3

while True:
    print_info()
    choise = input() # viskas kas ateina is input yra string tipo.
    match choise:
        case '1':
            print_dishes(dishes)
        case '2':
            id_counter = create_dish(dishes,id_counter)
        case '3':
            edit_dish(dishes)
        case '4':
            delete_dish(dishes)
        case '5':
            print("Išeiti iš programos")
            break
        case _:
            print("Netinkamas pasirinkimas, bandykite iš naujo.")
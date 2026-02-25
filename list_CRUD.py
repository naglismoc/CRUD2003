def print_info():
    print("-------------------------")
    print("1. Atvaizduoti patiekalus.")
    print("2. Įtraukti patiekalą.")
    print("3. Redaguoti patiekalą.")
    print("4. Trinti patiekalą.")
    print("5. Išeiti iš programos.")
    print("-------------------------")

def print_dishes(dishes):
    for dish in dishes:
        print(f"{dish['id']}. {dish['title']}  Kilmė: {dish['origin']}  Kaina: €{dish['price']:.2f}  Ingredientai:"
              f" {dish['ingredients']}")

def delete_dish(dishes):
    print('Įrašykite id patiekalo kurį norite trinti')
    del_id = int(input())
    for dish in dishes:
        if dish['id'] == del_id:
            dishes.remove(dish)
            print("Patiekalas sėkmingai ištrintas")
            break

def edit_dish(dishes):
    print('Įrašykite id patiekalo kurį norite redaguoti')
    edit_id = int(input())
    for dish in dishes:
        if dish['id'] == edit_id:
            print("Įveskite pavadinimą:")
            dish['title'] = input()
            print("Įveskite Kilmės šalį:")
            dish['origin'] = input()
            print("Įveskite kainą:")
            dish['price'] = float(input())
            print("Įveskite ingridientus:")
            dish['ingredients'] = input()

def create_dish(dishes,id_counter):
    print("Įveskite pavadinimą:")
    title = input()
    print("Įveskite Kilmės šalį:")
    country = input()
    print("Įveskite kainą:")
    price = float(input())
    print("Įveskite ingridientus:")
    ingredients = input()
    id_counter += 1
    dish = {
        'id': id_counter,
        "title": title,
        "origin": country,
        "price": price,
        "ingredients": ingredients
    }
    dishes.append(dish)
    return id_counter
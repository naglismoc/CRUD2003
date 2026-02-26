import csv

headers = ['id','title','origin','price','ingredients']
def load_dishes():
    with open("./dishes.csv", mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def save_dishes(dishes):
    with open('./dishes.csv',mode='w',newline='',encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(dishes)

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
        print(f"{dish['id']}. {dish['title']}  Kilmė: {dish['origin']}  Kaina: €"
              f"{float(dish['price']):.2f}  Ingredientai:"
              f" {dish['ingredients']}")

def create_dish(dishes,id_counter):
    print("Įveskite pavadinimą:")
    title = input()
    print("Įveskite Kilmės šalį:")
    country = input()
    print("Įveskite kainą:")
    price = float(input())
    print("Įveskite ingridientus:")
    ingredients = input()
    id_counter = int(dishes[-1]['id']) + 1 if len(dishes) > 0 else 1
    dish = {
        'id': id_counter,
        "title": title,
        "origin": country,
        "price": price,
        "ingredients": ingredients
    }
    dishes.append(dish)
    save_dishes(dishes)
    return id_counter

def edit_dish(dishes):
    print('Įrašykite id patiekalo kurį norite redaguoti')
    edit_id = input()
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
    save_dishes(dishes)

def delete_dish(dishes):
    print('Įrašykite id patiekalo kurį norite trinti')
    del_id = input()
    for dish in dishes:
        if dish['id'] == del_id:
            dishes.remove(dish)
            print("Patiekalas sėkmingai ištrintas")
            break
    save_dishes(dishes)


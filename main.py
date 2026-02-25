dishes = [
    {'id':1,
    "title":"bulviniai blynai",
     "origin":"Lietuva",
     "price":6.5,
     "ingredients":"bulvės, svogūnas, kiaušinis, prieskoniai"},
    {'id':2,
    "title":"jūros gėrybės",
     "origin":"Kreta",
     "price":12,
     "ingredients":"midijos, kalmarai, aštunkojai, ryžiai, grietinėlė, prieskoniai"},
    {'id':3,
    "title":"šaltekai",
     "origin":"Lietuva",
     "price":4.2,
     "ingredients":"bulvės, burokėliai, svogūnų laiškai, krapai, kefyras"},
]
id_counter = 3

while True:
    print("-------------------------")
    print("1. Atvaizduoti patiekalus.")
    print("2. Įtraukti patiekalą.")
    print("3. Redaguoti patiekalą.")
    print("4. Trinti patiekalą.")
    print("5. Išeiti iš programos.")
    print("-------------------------")
    choise = input() # viskas kas ateina is input yra string tipo.
    match choise:
        case '1':
            print("Atvaizduoju patiekalus")
            for dish in dishes:
                print(f"{dish['id']}. {dish['title']}  Kilmė: {dish['origin']}  Kaina: €{dish['price']:.2f}  Ingredientai:"
                       f" {dish['ingredients']}")
        case '2':
            print("Įtraukiu patiekalą:")
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
                "ingredients":ingredients
            }
            dishes.append(dish)
        case '3':
            print("Redaguoju patiekalą")
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
        case '4':
            print("Trinu patiekalą:")
            print('Įrašykite id patiekalo kurį norite trinti')
            del_id  = int(input())
            for dish in dishes:
                if dish['id'] == del_id:
                    dishes.remove(dish)
                    print("Patiekalas sėkmingai ištrintas")
                    break
        case '5':
            print("Išeiti iš programos")
            break
        case _:
            print("Netinkamas pasirinkimas, bandykite iš naujo.")

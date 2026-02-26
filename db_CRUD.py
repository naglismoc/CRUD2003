import pymysql

DB_CONFIG = {
    'host':'localhost', #127.0.0.1 alternatyva rasymui "localhost" ;)
    'port': 3312,
    'user':'root',
    'password':"root",
    'database':'menu_db'
}

headers = ['id','title','origin','price','ingredients']

def get_conn():
    return pymysql.connect(**DB_CONFIG)

def load_dishes():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from dishes")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    dishes = []
    for row in rows:
        single_dish = {}
        for col_num in range(len(headers)):
            single_dish[headers[col_num]] = row[col_num]
        dishes.append(single_dish)
    return dishes

def print_info():
    print("-------------------------")
    print("1. Atvaizduoti patiekalus.")
    print("2. Įtraukti patiekalą.")
    print("3. Redaguoti patiekalą.")
    print("4. Trinti patiekalą.")
    print("5. Išeiti iš programos.")
    print("-------------------------")

def print_dishes(dishes):
    dishes = load_dishes()
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
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO `menu_db`.`dishes`(`title`,`origin`,`price`,`ingredients`) VALUES (%s,%s,%s,%s);",(title,country,price,ingredients))
    conn.commit()
    cur.close()
    conn.close()

def edit_dish(dishes):
    print('Įrašykite id patiekalo kurį norite redaguoti')
    edit_id = input()
    print("Įveskite pavadinimą:")
    title = input()
    print("Įveskite Kilmės šalį:")
    country = input()
    print("Įveskite kainą:")
    price = float(input())
    print("Įveskite ingridientus:")
    ingredients = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE `menu_db`.`dishes`SET `title` = %s,`origin` = %s, `price` = %s,`ingredients` = %s WHERE `id` = %s;",(title,country,price,ingredients,edit_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_dish(dishes):
    print('Įrašykite id patiekalo kurį norite trinti')
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from dishes where id = %s", (del_id,))
    row = cur.fetchone()
    if row:
        print(f"{row[0]}. {row[1]}  Kilmė: {row[2]}  Kaina: €"
              f"{float(row[3]):.2f}  Ingredientai:"
              f" {row[4]}")
        cur.execute("delete from dishes where id = %s",(del_id,))
        conn.commit()
    else:
        print('Įrašo su tokiu id nėra.')
    cur.close()
    conn.close()



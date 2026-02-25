# #      0 1 2 3
# arr = [1,2,5,10]
# print(arr[0])
# #           name             surname              age
# student = {"name":"Jonas", "surname":"Petraukas","age":26}
# print(student['name'])
# print(f"sveiki mano vardras yra {student['name']}, pavarde {student['surname']}. Man yra {student['age']} metu.")
#
# sakila actor
# actor_id first_name last_name created_at
# 1        Nikole     Kidman      2006-01-01
# 2        Bred       Pitt      2006-01-01
#
# actors = [
#     {"actor_id":1, 'first_name':'Nikole', 'last_name':'Kidman', 'created_at': '2006-01-01'},
#     {"actor_id":2, 'first_name':'Bred', 'last_name':'Pitt', 'created_at': '2006-01-01'},
# ]
import random

rnd_num = random.randint(1,5)

if rnd_num == 1:
    print("vienas")
if rnd_num == 2:
    print("du")
if rnd_num == 3:
    print("trys")
if rnd_num == 4:
    print("keturi")
if rnd_num == 5:
    print("penki")

match rnd_num:
    case 1:
        print("vienas")
    case 2:
        print("du")
    case 3:
        print("trys")
    case 4:
        print("keturi")
    case 5:
        print("penki")

if rnd_num % 2 == 0:
    print('porinis')
else:
    print('neporinis')

# a if condition else b
print("porinis" if rnd_num % 2 == 0 else 'neporinis')

print("ka gero pasakysi?")
ivestis = input()
print(f'tu pasakei {ivestis}')

# print(dishes)
# print("-----------------")
# print(dishes[0])
# print("-----------------")
# print(dishes[0]['title'])

arr = [1,2,10]
for i in arr:
    i = 20

print(arr)
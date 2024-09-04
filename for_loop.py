# Task 01
fav_foods = ['Pizza','Tacos','Salmon']
for food in fav_foods:
    print(f" \t My Favorate Food is : {food}")

# Task 02
fav_foods = ['Pizza','Tacos','Salmon']
for food in fav_foods:
    if food == "Pizza":
        size = input(" \t What is the Pizza Size ?")
        size.lower()
    print(f" \t\t Your Ordered Pizza Size is : {size.upper()} .\n \t\t Payment Price : \t 100.0 \n \t \t ------- Yepp ! Your Pizza is Ready ....  -------")
    break

# Task 03
person = {
    "name" : "Gauri Hole",
    "instragram" : "@hole_gauri_r",
    "email" : "gaurihole27@gmail.com",
}
for key , value in person.items():
    print(f"The key is :\t {key}\n The value is : \t {value}")
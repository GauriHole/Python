while True:
    name = input(" \t \t What is your Name ? If New User Then Enter Info : ")
    if name == "Gauri":
        fav_food = "Pani-puri"
        print(f"\t \t Welcome Gauri , Yepp ! ! ! \n \t \t Your {fav_food} is Ready !")
    elif name != "Gauri" or name == "New":
        new_name = input(" Add Your new name here :")
        new_food = input(" Add Your Favorate Food :")
        print(f"\t \t Welcome {new_name.upper()} ,  Yepp ! ! ! \n \t \t Your {new_food} is Ready !")
        break
    else:
        print("Your Name is Not Registered Yet , Try again .")
        continue
    print(" \t ------------ T H A N K   Y O U  ! ------------- ")

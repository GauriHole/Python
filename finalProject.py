import random
while 1:
    print("         Choose       Rock        Paper     Scissors      OR    \n.  For  Quit  Game  Type  Exit    ")  
    user_answer = input(" >   Enter Your Choice : ")
    user_answer = user_answer.lower()
    if user_answer == "exit":
        break
    else:
        if user_answer != "rock" and user_answer != "paper" and user_answer != "scissors":
            print(" Please Enter Valid Input ")
            print("         Choose       Rock        Paper     Scissors      OR    \n.  For  Quit  Game  Type  Exit    ")  
            user_answer = input(" >   Enter Your Choice : ")
            user_answer = user_answer.lower()
            if user_answer == "exit":
                break
        comp_answer = random.choice(["rock","paper","scissors"])

        print(f" //                          Computer Chosed : {comp_answer}     //")
        if user_answer == comp_answer:
            print(".     -----------------    M A T C H   T I E D   -----------------")
            continue
        elif user_answer == "paper" and comp_answer == "rock":
            print(".     -----------------   Y O U   A R E   W I N N E R  -----------------")
            continue
        elif user_answer == "rock" and comp_answer == "scissors":
            print(".     -----------------   Y O U   A R E   W I N N E R  -----------------")
            continue
        elif user_answer == "scissors" and comp_answer == "paper":
            print(".     -----------------   Y O U   A R E   W I N N E R  -----------------")
            continue
        else:
            print(". -------------------------------    Y O U   L O S T   F R O M   C O M P U T E R   ----------------------------")
            continue
    
    

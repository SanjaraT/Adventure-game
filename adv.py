name = input("What's your name? ").upper()
print(" WELCOME "+name+" TO THE ADVENTURE!")
print("-----------------------------------")

while True:
    ans1 = input("YOU ARE ON A DIRT ROAD, IT HAS CAME TO AN END AND YOU CAN GO LEFT OR RIGHT OR FORWARD.WHICH WAY WOULD YOU LIKE TO GO? ").lower()

    if ans1 == "left":
        ans11 = input("YOU CAME TO A RIVER, DO YOU WANT TO WALK AROUND IT OR SWIM ACROSS IT(WALK/SWIM)? : ").lower()

        if ans11 == "walk":
            print("YOU WALKED FOR MANY MILES, RAN OUT OF WATER AND LOST!")
            quit()
        elif ans11 == "swim":
            ans111 = input("YOU CROSSED THE RIVER AND CAME TO AN NARROW ROAD! DO YOU WANT TO GO FORWARD OR HEAD BACK(FORWARD/BACK)? ").lower()
            if ans111 == "forward":
                ans1111 = input("YOU FOUND A MAN.DO YOU WANT TO TALK OR HEAD BACK(TALK/BACK)? ").lower()
                if ans1111 == "talk":
                    print("CONGRATULATIONS!YOU FOUND GOLD AND YOU WON!")
                    quit()
                elif ans1111 == "back":
                    print("YOU ARE BACK TO ROUND ONE!")
                    continue
                else:
                    print("INVALID OPTION! TRY AGAIN!")
                    continue
            elif ans111 == "back":
                print("YOU ARE BACK TO ROUND ONE!")
                continue
            else:
                print("INVALID OPTION! TRY AGAIN!")
                continue
        else:
            print("INVALID OPTION! TRY AGAIN!")
            continue

    elif ans1 == "right":
        ans12 = input("YOU CAME TO A BRIDGE. IT LOOKS WOBBLY, DO YOU WANT TO CROSS OR HEAD BACK(CROSS/BACK)? ").lower()
        if ans12 == "cross":
            ans121 = input("YOU CAME TO A NARROW ROAD, YOU WANT TO GO FORWARD OR HEAD BACK(FORWARD/BACK)? ").lower()
            if ans121 == "forward":
                ans1211 = input("YOU FOUND A MAN, DO YOU WANT TO TALK OR NOT (YES/NO)? ").lower()
                if ans1211 == "yes":
                    print("CONGRATULATIONS! YOU FOUND GOLD AND WON!")
                    quit()
                elif ans1211 == "no":
                    print("OOPS THE MAN GOT OFFEND AND YOU LOST!!")
                    quit()
                else:
                    print("INVALID OPTION! TRY AGAIN!")
                    continue
            elif ans121 == "back":
                print("YOU ARE BACK TO ROUND ONE!")
                continue
            else:
                print("INVALID OPTION! TRY AGAIN!")
                continue

        elif ans12 == "back":
            print("YOU ARE BACK TO ROUND ONE!")
            continue
        else:
            print("INVALID OPTION! TRY AGAIN!")
    elif ans1 == "forward":
        print("YOU ARE AT WRONG PLACE,YOU LOST! BETTER LUCK NEXT TIME! ")
        quit()
    else:
        print("INVALID OPTION! TRY AGAIN!")
        continue

def Question1():

    price = 300

    valid_quanty = True

    discount = 0.0

    print(f"Welcome to the Pancho Bakery, Bread price: ${price}")
    while valid_quanty:


        try:
            delivery = int(input("How many Bread's do you want?: "))

        except ValueError:
            print("Insert a integer number")

            continue

        if delivery < 0:
            print("Negative number's not allowed. Try again")

            continue


        elif delivery > 50:
            discount = float((price * delivery) * 0.2)

            print(f"\nGreat, a 20% of discount applied. :)")

            valid_quanty = False


        elif delivery > 20:
            discount = float((price * delivery) * 0.1)

            print(f"\nGreat, 10% of discount applied. :)")

            valid_quanty = False


        else:
            discount = 0.0
            print("\nDiscount doesn't apply for purchase less or equal than 20 bread's")


            valid_quanty = False

    
        total_cost = delivery * price

        discount_applied = (total_cost - discount)

        print("\n" + "="*25)

        print("Resume of your facture")

        print("="*25)
  
        print(f"""


    -------------------------------------------------------        


    |        Total cost: {total_cost}                     


    |        Discount Applied: {discount_applied}                     


    -------------------------------------------------------
    """)

def Question2():
    print("""



    =================================


    ¡Welcome to the cinema The Stars!


    =================================


""")

    valid_age = True
    valid_menu = True
    while valid_menu:

        print("""\n

    ============================

    Choose an option:

    1. Verify age for ticket
    2. Exit 

    ============================


    """)

        option = input("> ")

        if  not option.isdigit():
            print("\n--Insert a valid option")
            continue



        option = int(option)
        if option == 1:

            while valid_age:
                age = input("Enter the user age: ")

                if not age.isnumeric():
                    print("Invalid age, Try again.")
                    continue

                age = int(age)


                if age <= 0:
                    print("Invalid Age, Try again.")
                    continue


                elif age < 5:
                    print("Entry is free.")
                    break


                elif 5 <= age <= 11:
                    print("The ticket cost is $5000.")
                    break

                elif 12 <= age <= 59:
                    print("The ticket cost is $8000.")
                    break

                else:
                    print("The ticket cost is $4000.")
                    break
            continue


        if option == 2:
                valid_menu = False

        else:
                print("\n--Insert a valid option")

def Question3():
    val_train = True


    point = 1


    while val_train:


        days_tr=input("How many days do you trained this week?: ")


        if not days_tr.isdigit():


            print("\n" + "Insert a valid number".center(50,"=") + "\n")


            continue


        days_tr = int(days_tr)


        if 0 <= days_tr <= 1:


            print("\n"+"¡Dont give up, you can do better!".center(50, "=") + "\n")


        elif 2 <= days_tr <= 3:


            print("\n"+"Nice! But you can give more!".center(50,"=")+"\n")


        elif 4 <= days_tr:


            print("\n"+f"Excelent discipline, keep it! +{point} of energy".center(50,"=")+"\n")


        break

def Questin4():

    flavors = {


    "chocolate": 4000,


    "vanilla": 3500


}


    topping = 1000


    print("\n"+"Welcome to Frosty".center(50, "=") + "\n")


    print(f"""


    ===========================


        Flavor's & Prices


        


        1. chocolate: ${flavors['chocolate']}


        2. vanilla: ${flavors['vanilla']}


        Toppping: ${topping}


    ===========================


    """)


    frosty = True


    tpp_valid = True


    while frosty:
            flavor = input("What flavor do you want (vanilla or chocolate): ").lower()
            if flavor in flavors:


                while tpp_valid:


                    slct_tpp = input("Do you want add toppins? (y/n): ").lower()


                    total = flavors[flavor]


                    if slct_tpp == "y":


                        total += topping


                        print(f"Thanks for your purchase, the total receipt is: {total}")


                        tpp_valid = False


                    elif slct_tpp == "n":


                        print(f"Total recepit is: {total}")


                        tpp_valid = False


                    else:


                        print("Select a valid option(y/n).")


            else:


                print("Flavor not avaliable.")


            frosty = False

def question5():

    cost_bk = 25000

    is_student = input("is student?(y/n): ").lower()

    total = cost_bk

    if is_student == "y":


        total *= 0.85

        cpn = input("Do you have a cupon? insert code: ")


        if cpn == "LIBRO10":

            total *= 0.90

        else:

            pass


    print(f"total to pay: ${total}")

    #i know that the validations are missing, but from here i need to make fast code for the delivery.

def Question6():
    fee = 2000


    ticket = 5000





    print("Parking fee\n0-5hr: $2000 x hour\n5hr: $2000 x hour + ticket fixed $5000")


    hours = input("Hours park: ")


    if hours.isdigit():


        hours = int(hours)


        total = fee * hours


        if 0 <= hours < 5:


            print(f"Total cost: {total}")


        elif hours >= 5:


            total = total + ticket


            print(f"Total cost: {total}")


        else:


            print("insert a valid hour.")


    else:


        print("Insert a valid number.") 

def Question7():

    menu = 12000


    juice = 3000


    iva = 15000 * 0.08


    print(f"MENU\n${menu}\n${juice} (optional - drink)")





    delivery = input("You want to include drink (optional for $3000, y/n): ").lower()


    if delivery == "y":


        total = (menu + juice + iva)


        print(f"Total cost: {total}")


    elif delivery == "n":


        print(f"Total cost: {menu}")


    else:


        print("insert a valid value. (s/n)")

def Question8():

    technical = input("Inser a note (0.0 - 5.0): ")


    logic = input("Insert a note (0.0 - 5.0): ")





    if technical.isnumeric():


        pass


    if logic.isnumeric():


        technical = float(technical) 


        logic = float(logic)


        if 0.0 <= technical <= 5.0 and 0.0 <= logic <= 5.0:


            final_note = (technical * 0.7) + (logic * 0.3)


            print(f"Final note: {round(final_note, 2)}")


        if final_note >= 3:


            print("Aprobado")


        elif 2 <= final_note < 3:


            print("revision")


        else:


            print("reprobado")


    else:


        print("Insert a valid value.")

def Question9():

    cost_unit = 2000

    quanty = input("How many units are you going to buy: ")


    if quanty.isdigit():


        quanty = int(quanty)


        if quanty > 0:


            subtotal = cost_unit * quanty


            if quanty >= 30:


                discount = subtotal * 0.15


            elif quanty >= 10:


                discount = subtotal * 0.05


            else:


                discount = 0


            total_discount = subtotal - discount


            if total_discount < 50000:


                total_discount += 5000


                print("deliver apply for 5000")


            print(f"subtotal: ${subtotal} | discount applied: {discount} | Total: {total_discount}")


    else:
        print("INsert a valid number")
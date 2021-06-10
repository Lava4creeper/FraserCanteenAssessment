#Fraser Canteen v1.1 was created by Thomas Gardner on the 10/06/2021
#Sequence 1: Greeting v1.1 was created by Thomas Gardner on the 10/06/2021 
def greeting():
  #asking the user for their name
  name = input("Hello! What's your name? ")
  print()
  #asking the user if they want to view the menu
  menu_yes_no = input("Kia Ora {}! Wecome to the Fraser High School Canteen! Would you like to see the menu? ".format(name)).lower()
  print()
  #Moving to sequence 2
  show_menu(menu_yes_no)
#Sequence 2: Show_Menu v1.1 was created by Thomas Gardner on the 10/06/2021
def show_menu(menu_yes_no):
  #Looping mechanics
  while True:  
    #If the user wants to view the menu, display it
    if menu_yes_no == 'yes' or menu_yes_no == 'y':
      #Asking the user for their food choice and displaying the menu
      print("*-*-* Menu *-*-*")
      print()
      print("*** Pie: $4.50 ***")
      print("*** Burger: $7.89 ***")
      print()
      food_choice = input("What would you like to purchase? ").lower()
      print()
      #Moving to sequence 3
      Pie_Burger_Sensing(food_choice)
    #If the user doesn't want to view the menu, display the leaving message
    elif menu_yes_no == 'no' or menu_yes_no == 'n':
      #Thank the user for visiting
      print("Thankyou for visiting us at the Fraser High School Canteen. We hope to see you again soon!")
      print()
      #Go back to the beginning
      greeting()
    #If the user doesn't input yes or no ask them to re-input an answer
    else:
      #Ask the user to re-enter their answer
      menu_yes_no = input("Invalid input. Please enter 'Yes' or 'No': ")
      print()
#Sequence 3: Pie_Burger_Sensing v1.1 was created by Thomas Gardner on the 10/06/2021
def Pie_Burger_Sensing(food_choice):
  #If food choice is pie, tell them the usser their price
  if food_choice == "pie":
    print("You have purchased a Pie. This costs $4.50. Thank you for visiting the Fraser High School Canteen!")
    print()
    #Go back to the start of the program
    greeting()
  #If food choice is burger, tell the user their price
  elif food_choice == "burger":
    print("You have purchased a Burger. This costs $7.89. Thank you for visiting the Fraser High School Canteen!")
    print()
    #Go back to the start of the program
    greeting()
  #A little easter egg
  elif food_choice == "creeper":
    print("Aww man!")
    print()
    print("Creepers are not currently served here, as they cause explosive diarrhoea in some cases.")
    print()
    print("Thankyou for visiting us at the Fraser High School Canteen. We hope to see you again soon!")
    print()
    greeting()
  #If none of the above cases are met, return to the beginning
  else:
    print("Thankyou for visiting us at the Fraser High School Canteen. We hope to see you again soon!")
    print()
    greeting()
#Begin the program
greeting()
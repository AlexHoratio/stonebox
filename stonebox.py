from os import system
import datetime

data = None

def main_menu():
    system("clear")
    
    print("""
         ===============================================
           I M   S T O N E D   T O   T H E   B O N E
         ===============================================

  WHERE WOULD YOU LIKE TO GO TODAY?:
                      ______
                   .-"      "-.    #==========================#
                  /            \\   # 1. Insert a thought      #
                 |              |  # 2. View a random thought #
                 |,  .-.  .-.  ,|  #                          #
                 | )(_o/  \o_)( |  #==========================#
                 |/     /\     \|
       (@_       (_     ^^     _)
  _     ) \_______\__|IIIIII|__/__________________________
 (_)@8@8{}<________|-\IIIIII/-|___________________________>
        )_/        \          /
       (@           `--------`
                         

""")

    user_input = input("                              >")

    if(str(user_input).strip() == "1"):
        insert_thought()
    elif(str(user_input).strip() == "2"):
        view_random_thought()


def insert_thought():
    system("clear")

    data = open("stoned_thought_box.txt", "a+")

    print("""
         ===============================================
           I M   S T O N E D   T O   T H E   B O N E
         ===============================================

           ENTER SOME INTERDIMENSIONAL TRUTHS BELOW...

""")

    are_you_done = False
    
    second_rodeo = False

    while not(are_you_done):

        if(second_rodeo):
            stoned_thought = stoned_thought + "\n" + str(input("\n"))
        else:
            stoned_thought = str(input(">"))

        print("""\n\n

      ~~~~~~~~=======#######################=======~~~~~~~~
                     #  ARE YOU DONE?(y/n) #
      ~~~~~~~~=======#######################=======~~~~~~~~


""")
        decision = input("\n\n                              >")

        if(str(decision).strip() == "y"):
            are_you_done = True
        elif(str(decision).strip() == "n"):
            are_you_done = False
            second_rodeo = True
            system("clear")
            print("""
         ===============================================
           I M   S T O N E D   T O   T H E   B O N E
         ===============================================

           ENTER SOME INTERDIMENSIONAL TRUTHS BELOW...


>""" + stoned_thought, end="")

    data.write("\n" + stoned_thought + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    data.close()

    system("clear")

    print("""
         ===============================================
           I M   S T O N E D   T O   T H E   B O N E
         ===============================================

               YOUR THOUGHT HAS BEEN RECORDED...
 
                       ################
                       ###          ###
                       ### GOODBYE. ###
                       ###          ###
                       ################


             ,.   (   .      )        .      "
            ("     )  )'     ,'        )  . (`     '`
          .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
          _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
  






""")

main_menu()
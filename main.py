##################################################################################
# Aces Up Game 
#
# ALGORITHM
# 
# This project layouts the code for the famous aces up game
# This project uses two classes (Class and Deck) as described in card.py
# It uses these classes by importing cards from the cards.py 
# This project uses 9 functions and a main function. The 9 functions are as follows:
# init_game(): This function initializes the stock,tableau and foundation 
# deal_to_tableau(): This function deals one card to each of the 4 columns in tableau  
# validate_move_to_foundation(): When a card is moved from tableau to foundation,
# this function checks its validity. If move valid, return true else false 
# move_to_foundation(): This function moves the bottom most card of chosen 
# column to foundation, only if the move is valid
# validate_move_within_tableau(): When a card is tried to move from one column to 
# another, this function checks its validity. If vaid, return True else False
# move_within_tableau: If move is valid, this function moves the card from origin
# column to the destination column 
# check_for_win(): This function checks if the game was won
# get_option(): This function returns a list based on the type of user_input
# this list is further used in the main function
# main(): The mani function displays the RULES and the MENU of options. It then calls
# the appropriate functions to complete the task desired by the chosen option.
# If at any point, the game is won, this function ends the game and displays winning message.
#
########################################################################################


import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    '''
    This function ilitializes the aces up game. It initializes the foundation 
    to an empty list and uses the class Deck to initialize the stock to 52 
    cards of a deck. It then deals one card to each column of the tableau.
    This function returns a list of stock, a list of lists (tableau) and 
    a list of foundation which is empty.
    '''

    foundation = []     #initialize foundation as an empty list
    tableau = []

    #initialize the stock with a deck of cards using class Deck
    stock = cards.Deck()
    stock.shuffle()     #shuffle the deck of cards in the stock

    #deal one card to each of the 4 columns (or lists) of the tableau using deal() function
    for i in range(4):
        tableau.append([stock.deal()])

    return stock,tableau,foundation
    
    
def deal_to_tableau( tableau, stock):
    '''
    This function deals one card to each of the four columns in
    a tableau. It uses the class method .deal() to accomplish this
    '''
    #for loop to iterate over each list in the list of lists (tableau)
    for column in tableau:
        card = stock.deal()    #use .deal() to deal one card from stock to column
        column.append(card)


def validate_move_to_foundation(tableau, from_col):
    '''
    This function validates a move from tableau to foundation. It returns true
    when a card can be moved to foundation, else it returns False. A card can only
    be moved if a higher rank card of the same suit is present at the bottom 
    of any of the other three remaining columns. 
    '''

    #if the chosen column is empty, return False
    if len(tableau[from_col]) == 0:
        print("\nError, empty column: {}".format(from_col + 1))
        return False
    
    card = tableau[from_col][-1]
    
    #if the bottom card of the chosen column is an ace, return False
    if card.rank() == 1:
        print("\nError, cannot move {}.".format(card))
        return False

    #for loop to iterate over each column in the tableau
    for i in range(4):

        #proceed only if column is not empty
        if len(tableau[i])>0:

            #if bottom card is ace and the chosen card has same 
            #suit as that of the ace card, return True.
            if tableau[i][-1].rank() == 1 and tableau[i][-1].suit() == card.suit(): 
                return True

            #If the bottom card is not an ace and if the bottom card is of
            #the same suit as that of the chosen card and its rank is higher 
            #than the chosen card, return True.
            elif tableau[i][-1].suit() == card.suit() and tableau[i][-1].rank() > card.rank():
                return True
    
    #return false in all the other cases
    print("\nError, cannot move {}.".format(card))
    return False

def move_to_foundation( tableau, foundation, from_col ):
    '''
    This function moves the botom card of the chosen column to the
    foundation only if the move is valid.
    '''
    #call validate_move_to_foundation to check if the move is valid or not
    boolean = validate_move_to_foundation(tableau, from_col)

    #if move is valid, move card from tableau to foundation
    if boolean == True:
        foundation.append(tableau[from_col][-1])    #append bottom card to foundation
        tableau[from_col].remove(tableau[from_col][-1])     #remove bottom card
    

def validate_move_within_tableau( tableau, from_col, to_col ):
    '''
    This function takes three parameters, tableau, from_col and to_col.
    it returns true if a card can be move from one column to another
    within the tableau, else returns False. 
    '''

    '''if condition to check if the origin column is empty and if the
    destination column is filled. If both conditions satisfy, return False''' 
    if len(tableau[from_col]) == 0 and len(tableau[to_col]) > 0:
        print("\nError, target column is not empty:",to_col + 1)
        return False

    #return false if origin column empty
    elif len(tableau[from_col]) == 0:
        print("\nError, no card in column:",(from_col + 1))
        return False

    #return False if destination column not empty
    elif len(tableau[to_col]) > 0 :
        print("\nError, target column is not empty:",to_col + 1)
        return False

    #return true in all other cases 
    else:
        return True


def move_within_tableau( tableau, from_col, to_col ):
    '''
    This function is used to move the bottom card of one column
    to tn empty column, only if the move is valid
    '''
    #call validate_move_within_tableu to check if move is valid
    boolean = validate_move_within_tableau( tableau, from_col, to_col )

    #if move is valid, move the card from origin column to destination column
    if boolean == True:
        tableau[to_col].append(tableau[from_col][-1])
        tableau[from_col].remove(tableau[from_col][-1])
        

def check_for_win( tableau, stock ):
    '''
    This function checks if the stock is empty and if only 
    fou aces are left in the tableau. If this condition is 
    satisfied, it returns true else it returns False.
    '''
    #initializing two empty helper lists
    helper_list = []
    helper_list_2 = []

    #proceed only if stock is empty
    if len(stock) == 0:
        #for loop to iterate over each column in tableau
        for i in range(4):      #i is column index
            #for loop to iterate over each card in column
            for j in range(len(tableau[i])):    #j is card's index
                helper_list.append(tableau[i][j])    #append each card to helper list
    
    #proceed only if 4 cards were present in tableau
    if len(helper_list) == 4:

        #for loop to iterate over each card in helper_list
        for k in range(len(helper_list)):   #k is card index in helper_list
            #if condition to check for an ace
            if helper_list[k].rank() == 1:
                helper_list_2.append(k)     #append card to helper_list_2 only is its an ace
    
    #if all four cards in helper_list were aces, they will be added to helper_list_2
    #if condition to check the length of helper_list, return true if 4 cards present
    if len(helper_list_2) == 4:
        return True
    else:
        return False


def display( stock, tableau, foundation ):
    '''Provided: Display the stock, tableau, and foundation.'''

    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    maxm = 0
    for col in tableau:
        if len(col) > maxm:
            maxm = len(col)
    
    assert maxm > 0   # maxm == 0 should not happen in this game?
        
    for i in range(maxm):
        if i == 0:
            if stock.is_empty():
                print("{:<8s}".format(""),end='')
            else:
                print("{:<8s}".format(" XX"),end='')
        else:
            print("{:<8s}".format(""),end='')        
        
        #prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print( "{:4s}".format( str(col[i]) ), end='' )

        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')
                
        print()

def get_option():
    '''
    This function prompts the user to enter an option. It 
    is then used to get an option list from the input string, 
    which is later used in the main function. If the entered 
    option is incorrect, it returns an empty list.
    '''
    len1_list = ["D","H","R","Q"]
    #prompt user to input desired option from the list of options displayed in the MENU
    user_input = input("\nInput an option (DFTRHQ): ")
    option = user_input.upper()     #convert input string to upper case
    
    #if user_input is one of D,H,R,Q options, return list of that option in upper case
    if option in len1_list:
        return[option]

    #if user input is of length 3 and first character is F
    elif len(option) == 3 and option[0] == "F":
        #retrive column number from user_input
        if option[2].isdigit():
            x = int(option[2]) 
            if 1 <= x <= 4:     #check if the column number is valid
                #(x-1) because it is index number of column x
                return ["F",x-1]    #return list of option F and column index

    #if user_input is of length 5and first character is T
    elif len(option) == 5 and option[0] == "T":
        if option[2].isdigit() and option[4].isdigit():
            x = int(option[2])
            y = int(option[4])

            #check if the origin and destination column numbers are valid
            if 1 <= x <= 4 and 1 <= y <= 4:
                #(x-1) and (y-1) because they are index numbers for columns x and y
                return ["T",x-1,y-1]
    print("\nError in option:",user_input)
    return []   #return empty list if user_input is invalid 


def main():
    '''
    This is the main function that interacts with the user and enables
    the user to play the aces up game. It displays the status of the game after
    each move andalso displatys if the game is won or restarted by the user"
    '''
    print(RULES)
    print(MENU)
    #initialize the game 
    stock, tableau, foundation = init_game()
    #display the initial status of the game 
    display(stock,tableau,foundation)

    while True: #main while loop
        option = get_option()   #fetch the option list by calling get_option() function.

        #if option is D, deal one card to each of the four columns of the tableau
        if option == ["D"]:
            deal_to_tableau(tableau,stock)  #call deal_tableau_function to deal cards
            display(stock,tableau,foundation) #display game status 

        #if option is R, print restart game message, re-initialize variables and print RULES & MENU
        elif option == ["R"]:
            print("\n=========== Restarting: new game ============")
            print(RULES)
            print(MENU)

            # Re-initialize the game and display the new status
            stock,tableau,foundation = init_game()
            display(stock,tableau,foundation)

        #if option is H, print MENU of options and display the status of the game
        elif option == ["H"]:
            print(MENU)
            display(stock,tableau,foundation)
        
        #if option is Q, break the loop, print quit message and quit the program
        elif option == ["Q"]:
            print("\nYou have chosen to quit.")
            break

        #if option is F, move bottom card of chosen column to foundation   
        elif 'F' in option:
            from_col = option[1]    #retrive column number
            #call move_to_foundation function to move bottom card of column to foundation
            move_to_foundation(tableau,foundation,from_col)
            
            #call check_for_win function to check for win
            boolean = check_for_win(tableau,stock) 

            #if game is won display winning message and break the loop
            if boolean == True:
                print("\nYou won!")
                break
            
            #if game not won, display the game status
            else:
                display(stock,tableau,foundation)

        #if option is T, move card from origin column to destination column
        elif 'T' in option:
            from_col = option[1]    #retrieve origin column number
            to_col = option[2]      #retrieve destination column number

            #call move_within_tableau function to move card from origin column to destination column 
            move_within_tableau(tableau,from_col,to_col)

            #call check_for_win function to check for win
            boolean = check_for_win(tableau,stock) 

            #if game is won display winning message and break the loop
            if boolean == True:
                print("\nYou won!")
                break
            #if game not won, display the game status
            else:
                display(stock,tableau,foundation)
        
if __name__ == '__main__':
    main()

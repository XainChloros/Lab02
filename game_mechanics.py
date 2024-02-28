
#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    print("~~~~~~~~~~~~~~WELCOME TO THE GAME~~~~~~~~~~~~~~")
    #------------------------

    #------------------------
#---------------------------------------
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    # Add your code here
    print("1) Maths")
    print("2) History")
    print("3) Science")

    choice=int(input("Choose a category to play"))

    if choice >=1 and choice <=3:
        return choice
    else:
        print("Invalid Choice.Kindly choose again")
    #------------------------

    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    # Add your code here

    print("Curent round number: ", round_number)

    print("Current Score: ",score)

    #------------------------

    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    # Add your code here
    print("Game Over. Your final score is ",final_score)

    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    # Add your code here
    for i in range(5):
        picked_category=choose_category(categories)
        question, right_answer= choosing_random_question(choose_category)
        user_answer=show_quest/ans(question)
        correct=validate_answer(user_answer,right_answer)
        score=update_score(score,correct)
        display_score(score, i+1)
        next_round(i+1)
        delete_question(picked_category,question)
    #------------------------


    #------------------------

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    return player_answer == correct_answer

    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    # Add your code here
    if correct:
        return score +1
    else:
        return score
    #------------------------

    #------------------------

#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    #------------------------
    return round_number +1
    #------------------------

    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    # Add your code here
    return incorrect_answers >=3
    #------------------------
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
    # Add your code here
    replay = input('\nDo you want to play the game again?\nEnter "Y" to continue or "N" to exit: ')
    if replay == 'N' or replay == 'n':
        print('\nExiting the Game')

    elif replay == 'Y' or replay == 'y':
        print()

    #------------------------

#---------------------------------------


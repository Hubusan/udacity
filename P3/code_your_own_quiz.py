"""
These are the text definitions for 3 difficulty levels.
"""
text = \
    ['''Python is an interpreted __1__-level programming language for general-purpose programming. \nCreated by Guido van Rossum and first released in __2__, \nPython has a design philosophy that emphasizes code readability, notably using significant whitespace. \nIt provides constructs that __3__ clear programming on both small and large __4__.'''
     ,
     '''Python features a __1__ type system and automatic memory management. \nIt supports __2__ programming paradigms, including object-oriented, imperative, \n__3__ and procedural, and has a large and comprehensive standard __4__'''
     ,
     '''Python __1__ are available for many operating systems. __2__, the reference implementation of Python, is open source software and has a __3__-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python __4__ Foundation'''
     ]

"""
Correct Answer list for the questions. It is a list that is divided by difficulty levels.
"""
correct_answers = [['high', '1991', 'enable', 'scales'], ['dynamic',
                   'multiple', 'functional', 'library'], ['interpreters'
                   , 'CPython', 'community', 'Software']]

"""
    General variable definitions.
"""
clearscreen = 500                                                                                   #Variable to clear the screen
max_chances = 5                                                                                     # Amount of max retries


"""
Welcome function prints welcome text and difficulty options. No inputs. Justs prints to the screen
"""
def welcome():
    print 'Welcome to fill in the blanks quiz'
    print 'Would you please pick a difficulty ? easy or medium or hard'


"""
    pick_difficulty method is the place where user picks a difficulty level.
    It takes no inputs.
    And returns an integer amongs 0,1,2 accourding to the difficulty selected.
"""
def pick_difficulty():                                                                              # lets user to decide on what difficulty to play. Takes no inputs. Returns an integer according to selected difficulty.
    difficulty = raw_input()                                                                        #takes in the difficulty
    if difficulty.lower() == 'easy':                                                                #difficulty comparison with user input
        difficulty = 0
    elif difficulty.lower() == 'medium':                                                            #difficulty comparison with user input
        difficulty = 1
    elif difficulty.lower() == 'hard':                                                              #difficulty comparison with user input
        difficulty = 2
    else:                                                                                           # makes sure that user enters one of 3 difficulty levels
        print 'Please pick one of the following: \neasy or medium or hard'
        difficulty = pick_difficulty()
    return difficulty                                                                               # Returns an integer among 0,1,2

"""
    check_answers is the method where each user answer is compared with correct answers.
    It takes 3 inputs. difficulty as integer, blankNumber as integer and user_answer as string.
"""
def check_answers(difficulty, blankNumber, user_answer):                                            
    correct_answers_for_difficulty = correct_answers[difficulty]                                    #gets correct answer list
    if user_answer == correct_answers_for_difficulty[blankNumber]:                                  #compares user answers and correct answer
        print '################\nCorrect\n################\nAnswer the next blank\n################\n'
        count_of_answer = 0                                                                         #Count of the answer initialized to zero
        blank="__"+str(blankNumber+1)+"__"                                                          #sets blank variable to hold the blank number with __ on both sides as text
        textByDifficulty=text[difficulty]                                                           #gets the text according to difficulty
        textWithCorrectAnswer=textByDifficulty.replace(blank,user_answer)                           #sets the text with correct answer replaced to textWithCorrectAnswer string.
        text[difficulty]=textWithCorrectAnswer                                                      #changes global variable text to have correct answers replaced.
        print text[difficulty]                                                                      #prints the text with correct answers
        return True                                                                                 # returns True if the answer is correct
    else:
        print '################\nWrong Answer\n################\n'              
        print text[difficulty]
        return False # returns False if the answer is not correct                                   # returns boolean False if the answer is wrong

"""
    This method clears the screen.
"""    
def clearScreenAndPrintText(difficulty):
    print '\n' * clearscreen                                                                        #prints a new line and value times clearscreen variable

"""
    quiz is the core method that applies the algorithm to have the quiz.
    It takes an integer value as difficulty level.
    It has no return value.
"""
def quiz(difficulty):                                                                               # takes difficulty variable as integer
    print text[difficulty]                                                                          # prints the text according to selected difficulty.
    i = 0                                                                                           # sets loop variable i to zero for initiation
    while i < int(len(correct_answers)) + 1:                                                        # this loops until i is equal to lenght of correct answers list + 1 to make sure each question is asked
        count_of_answer = 0                                                                         # this is the count for each answers given by user for each question. It is initialized to zero for each question at first
        while count_of_answer < max_chances:                                                        # makes sure that if user gives wrong answer, user can try as much as max_chances and else goes to next question
            print '\n############################\n#Answer for blank number: ' + str(i + 1) +'#\n############################\n' # prints the expected blank number to be answered
            user_answer = raw_input()                                                               # Takes the user answer and sets it into user_answer string
            clearScreenAndPrintText(difficulty)                                                     # calls the clearScreenAndPrintText method to clear the screen after user input to make it reeady for the results
            if check_answers(difficulty, i, user_answer) == True:                                   # Checks if the user answer is correct by calling the check_answers method
                i += 1                                                                              # if the answer is correct it increases i by one and breaks the loop to wait for next answer for next blank
                break
            else:                                                                                   # if the answer is wrong it goes into this else to check answer limits
                count_of_answer += 1                                                                # increases answer count by one
                if count_of_answer == max_chances:                                                  # checks if the user exceeded the max_chances
                    i += 1                                                                          # increases i by one to go for the next blank.
                    if i < int(len(correct_answers)) + 1:                                           # checks if user has tried all the blanks
                        print 'You have failed on blank number ' + str(i) + '\nGo for the next blank' # prints the failed blank number and tells user to go for the next blank

"""
    The main method that triggers the quiz.
    It takes no value and returns nothing.
"""
def main():                                                                                         # Main method to call flow of the program
    print '\n' * clearscreen                                                                        # Clears the screen                                                          
    welcome()                                                                                       # Calls welcome method to print welcome messages.
    difficulty = pick_difficulty()                                                                  # calls pick_difficulty method to get users preferred difficulty level and sets it to difficulty integer
    quiz(difficulty)                                                                                # calls the quiz method with variable difficulty to start the quiz with selected difficulty level.


# call of main method

main()


			

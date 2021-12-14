# Jaiden Wilson -J.W
# Temi Akanni - T.A
# Aaron Koarlall - A.K
import random
from colorama import Fore, Back, Style
coins = 0
tries = 0
hintPrice = 5 
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+ 
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
## Generate a list of words to be guessed according to theme and difficulty - Done by T.A and A.K
animals = (['ant','bat','bear', 'dog', 'fox', 'cat', 'goat', 'eagle', 'hawk', 'lion'],['lizard', 'beaver', 'llama', 'chimpanzee','python', 'panda', 'salmon', 'moose', 'parrot', 'dolphin'],['newt','liger','mule','orca','sloth','trout','wombat','flamingo','tarantula','platypus'])
countries = (['canada','china','america','japan','spain','france','italy','brazil','mexico','russia'],['germany', 'netherlands', 'egypt', 'sweden','nigeria', 'south africa', 'peru', 'argentina', 'england', 'ireland'],['afghanistan','zimbabwe','cyprus','uruguay','kazakhstan','czech republic','dominican republic','jordan','azerbaijan','seychelles'])
foods = (['eggs','chicken','rice', 'fries', 'ham', 'pizza', 'burger', 'apple', 'corn', 'cake'],['sushi', 'burrito', 'lettuce', 'eggplant','lobster', 'spaghetti', 'mushroom', 'pumpkin', 'cranberry', 'dragon fruit'],['gelatin','gyro sandwich','caviar','calamari','tamale','calzone','lasagna','tilapia','edamame','guacamole'])
sports = (['soccer','basketball','hockey','baseball','football','tennis','volleyball','swimming','rugby','track'],['table tennis','ultimate frisbee','cricket','mixedmartialarts','cycling','gymnastics','skiing','handball','skateboarding','boxing'],['waterpolo','squash','snooker','rowing','netball','motorsport','mountain climbing','formula 1','fencing','curling'])
miscellaneous = (['bedroom','quicksand','palm tree','asylum','saxophone','volcano','pharaoh','engineer','diaphragm','carbon dioxide'],['esophagus','onomatopoeia','aristocrat','asphyxiation','blandishment','espionage','pteradactyl','chauffeur','pythagorean theorem','erroneous'],['logorrhea','acquiesce','matriculation','solitary confinement','regurgitate','manoevre','undulate','lugubrious','bureaucracy','connoisseur'])


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
## Prints an element from the Hangman_Pics list based on the updated number of missed letters. Also displays the amount of coins the user has and their remaining tries. - Displayed values modified by J.W and colours modified by A.K
def displayBoard(missedLetters, correctLetters, secretWord):
    print(Fore.RED + HANGMAN_PICS[len(missedLetters)]+'                     '+'coins: '+str(coins)+'       tries remaining: '+str(len(HANGMAN_PICS)-1-len(missedLetters)))
    print()
 
    print(Fore.GREEN+'Missed letters:', end=' ')
    for letter in missedLetters:
        print(Fore.GREEN + letter, end=' ') 
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(Fore.WHITE + letter, end=' ')
    print()

def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

## Initializes the length of missedletters and correctletters to 0 
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
#Prompts the user for their choice of theme and difficulty, and ensures that their input is valid. - Done by J.W
themes= input( "What theme would you like to choose?\n1-Animals\n2-Countries\n3-Foods\n4-Sports\n5-Miscellaneous")
while(themes.isdigit()==False):
    themes= input( "Please enter a whole number from 1 to 5 corresponding to the above themes")
if(themes.isdigit()):
    while int(themes) not in range(1,6):
        themes= input( "Please enter a whole number from 1 to 5 corresponding to the above themes")
difficulty = input("What difficulty would you like to play on?\n1-Easy\n2-Intermediate\n3-Advanced")
while(difficulty.isdigit()==False):
    difficulty= input( "Please enter a whole number from 1 to 3 corresponding to the above difficulties.")
if(difficulty.isdigit()):
    while int(difficulty) not in range(1,4):
        difficulty= input( "Please enter a whole number from 1 to 3 corresponding to the above difficulties")    
#Selects a random word from a list based on the user's choice of theme and difficulty - T.A and A.K     
if(int(themes)==1):
    if(int(difficulty)==1):
        secretWord = getRandomWord(animals[0])
    elif(int(difficulty) == 2):
        secretWord = getRandomWord(animals[1])
    elif(difficulty == 3):
        secretWord = getRandomWord(animals[2])
elif(int(themes)==2):
    if(int(difficulty)==1):
        secretWord = getRandomWord(countries[0])
    elif(int(difficulty) == 2):
        secretWord = getRandomWord(countries[1])
    elif(int(difficulty) == 3):
        secretWord = getRandomWord(countries[2])
elif(int(themes)==3):
    if(int(difficulty)==1):
        secretWord = getRandomWord(foods[0])
    elif(int(difficulty) == 2):
        secretWord = getRandomWord(foods[1])
    elif(int(difficulty) == 3):
        secretWord = getRandomWord(foods[2])
elif(int(themes)==4):
    if(int(difficulty)==1):
        secretWord = getRandomWord(sports[0])
    elif(int(difficulty) == 2):
        secretWord = getRandomWord(sports[1])
    elif(int(difficulty) == 3):
        secretWord += getRandomWord(sports[2]) 
elif(int(themes)==5):
    if(int(difficulty)==1):
        secretWord = getRandomWord(miscellaneous[0])
    elif(int(difficulty) == 2):
        secretWord =getRandomWord(miscellaneous[1])
    elif(int(difficulty) == 3):
        secretWord = getRandomWord(miscellaneous[2])
   
 

gameIsDone = False
def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.' + Fore.MAGENTA + '(Enter $ to try and guess the entire word. If you are stuck, you may press # to purchase a hint) ')
        guess = input()
        
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz' and guess!='$' and guess!='#':
            print('Please enter a LETTER.') 
        else:
            return guess
## Updates the values of missed letters, correct letters and secret word   
while True: 
    displayBoard(missedLetters, correctLetters, secretWord) 
    # Let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)
    tries +=1
    #Gives the user a chance to guess the entire word # Done by T.A
    if(guess=='$'):
        superGuess = input('What do you think the word is?') 
        if(superGuess==secretWord):
            print(Fore.WHITE +'Yes! The secret word is "' + secretWord + '"! You have won!')
            #Rewards the user with additional coins for purchasing hints if they have guessed the secret word within a small number of attempts - Done by J.W
            if(tries==1):
                print('Achievement unlocked: Guess the word in one try!\nReward: +15 coins')
                coins+=15
            elif(tries==2):
                print('Achievement unlocked: Guess the word in less than 3 tries!\nReward: +10 coins') 
                coins+=10    
            elif(tries==3):
                print('Achievement unlocked: Guess the word in less than 4 tries!\nReward: +5 coins')
                coins+=5    
            gameIsDone = True
        #Implements a penalty of two tries lost if the user tries to guess the entire word but fails # J.W
        else:
            missedLetters = missedLetters + '.' + '.' 
    # Done by J.W
    elif(guess=='#'):
        # Reveals a letter in the hidden word for a price of 5 coins, assuming the user has at least 5 coins
        if(coins>=hintPrice):
            coins-=hintPrice
            guess= secretWord[random.randint(0, len(secretWord) - 1)]
            correctLetters = correctLetters + guess
            print(Fore.GREEN+'You purchased a hint for '+ str(hintPrice)+ ' coins')
        #Declines the user's request to reveal a letter if coins<hintPrice
        else:
            print("Sorry. You don't have enough coins to buy a hint :( ")
            
    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)): 
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(Fore.WHITE+'Yes! The secret word is "' + secretWord + '"! You have won!')
            if(tries==1):
                print('Achievement unlocked: Guess the word in one try!\nReward: +15 coins')
                coins+=15
            elif(tries==2):
                print('Achievement unlocked: Guess the word in less than 3 tries!\nReward: +10 coins')
                coins+=10    
            elif(tries==3):
                print('Achievement unlocked: Guess the word in less than 4 tries!\nReward: +5 coins')
                coins+=5    
            gameIsDone = True
    elif guess not in secretWord and guess!='$' and guess!='#' :
        missedLetters = missedLetters + guess

    #Check if player has guessed too many times and lost. 
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
        gameIsDone = True
        
        
    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            tries=0
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            themes= input("What theme would you like to choose?\n1-Animals\n2-Countries\n3-Foods\n4-Sports\n5-Miscellaneous")
            difficulty = input("What difficulty would you like to play on?\n1-Easy\n2-Intermediate\n3-Advanced")
            secretWord=''
            if(int(themes)==1):
                if(int(difficulty)==1):
                    secretWord += getRandomWord(animals[0])
                elif(int(difficulty) == 2):
                    secretWord += getRandomWord(animals[1])
                elif(difficulty == 3):
                    secretWord += getRandomWord(animals[2])
            elif(int(themes)==2):
                if(int(difficulty)==1):
                    secretWord += getRandomWord(countries[0])
                elif(int(difficulty) == 2):
                    secretWord += getRandomWord(countries[1])
                elif(int(difficulty) == 3):
                    secretWord += getRandomWord(countries[2])
            elif(int(themes)==3):
                if(int(difficulty)==1):
                    secretWord += getRandomWord(foods[0])
                elif(int(difficulty) == 2):
                    secretWord += getRandomWord(foods[1])
                elif(int(difficulty) == 3):
                    secretWord += getRandomWord(foods[2])
            elif(int(themes)==4):
                if(int(difficulty)==1):
                    secretWord += getRandomWord(sports[0])
                elif(int(difficulty) == 2):
                    secretWord += getRandomWord(sports[1])
                elif(int(difficulty) == 3):
                    secretWord += getRandomWord(sports[2]) 
            elif(int(themes)==5):
                if(int(difficulty)==1):
                    secretWord += getRandomWord(miscellaneous[0])
                elif(int(difficulty) == 2):
                    secretWord +=getRandomWord(miscellaneous[1])
                elif(int(difficulty) == 3):
                    secretWord += getRandomWord(miscellaneous[2])
        else:
            break
 
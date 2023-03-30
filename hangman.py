import random
import turtle
#choose a word 
#only end the game when the word is finished or they ran out of tries
#ask the user to guess a character of the word
#if they fail i deduct one point from the tries 
#if they win i type the character in its respective placwe
word_dict = {
    "banana": "A yellow fruit that monkeys love to eat.",
    "computer": "An electronic device that can perform various tasks and calculations.",
    "guitar": "A musical instrument with strings that is played by strumming or plucking.",
    "umbrella": "An object used to protect oneself from rain or sun.",
    "ocean": "A large body of salt water",
    "cat": "A small domesticated carnivorous mammal with soft fur.",
    "dog": "A domesticated carnivorous mammal with a long snout and an acute sense of smell.",
    "horse": "A large domesticated mammal with a flowing mane and tail, used for riding, racing, and to carry and pull loads.",
    "elephant": "A very large mammal with a long, curved trunk and ivory tusks, native to Africa and southern Asia.",
    "rhinoceros": "A large, thick-skinned herbivorous mammal with one or two horns on the nose, native to Africa and Asia.",
    "hippopotamus": "A large African mammal with a broad mouth, short legs, and thick, gray skin.",
    "crocodile": "A large predatory semiaquatic reptile with a long snout, broad jaws, and strong teeth.",
    "giraffe": "A large African mammal with a very long neck and forelegs, having a coat patterned with brown patches separated by lighter lines.",
    "penguin": "A flightless bird of the southern hemisphere, having a black-and-white plumage and walking with a waddling gait.",
    "rhododendron": "A plant of the heath family, having large clusters of showy, brightly colored flowers and evergreen leaves."}
secret_word = random.choice(list(word_dict.keys())) 
current_word = ["_"] * len(secret_word)
tries = 6
difficulty = input("Please select difficulty (easy,medium or hard):")
easy = False
medium = False
hard = False
valed = True
made_guess = []
jim = turtle.Turtle()
correct_guess = False
while True:
    
    match difficulty:
        case "easy": 
            easy = True
            difficulty = ""
        case "medium":
            medium = True
            difficulty = ""
            
        case "hard":
            
            hard = True
            difficulty = ""
            
        case _:
            print("invalid please choose from the options")
            valed = False
            break
    

    if(easy == True and len(secret_word) > 5):
        while len(secret_word) > 5:
            secret_word = random.choice(list(word_dict.keys()))
            current_word = ["_"] * len(secret_word)
        break
        
         
    elif(medium == True and len(secret_word) > 6):
          while len(secret_word) > 6:
            secret_word = random.choice(list(word_dict.keys()))
            current_word = ["_"] * len(secret_word)
          break
        
    elif(hard == True and len(secret_word) > 7):
          while len(secret_word) > 7:
            secret_word = random.choice(list(word_dict.keys()))
            current_word = ["_"] * len(secret_word)
          break
        


while tries > 0 and '_' in current_word and valed == True:
    guess = input("do you want a hint or you want to guess? (Enter one characteror type Hint): ")
    
   

    
    if guess in made_guess:
        print("you already guessed that")
    
    elif guess =="Hint":

        print(word_dict[secret_word])
    elif len(guess) != 1:
        print("input only one character")
    elif guess in secret_word and guess != "Hint" and len(guess) == 1 :
        indices = [i for i, letter in enumerate(secret_word) if letter == guess]
        for index in indices:
            current_word[index] = guess
        print("Correct!")
        print(' '.join(current_word))
        made_guess += guess
        correct_guess = True

    else:
        tries -= 1
        print("Incorrect. You have {} tries left.".format(tries))
        correct_guess = False
     

     
if '_' not in current_word:
    print("Congratulations, you guessed the word {}!".format(secret_word))
elif tries == 0:
    print("Hangman! The word was {}.".format(secret_word))


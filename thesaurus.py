import json # To working with json file
from difflib import get_close_matches # To check the word similarity and differences
import sys # To handle the comman line argument

# Load the dictionary json file
myData = json.load(open('dictionary.json'))

def translate(word):
    # Check the given word is exists in the dictionary
    if word in myData:
        return(myData[word])
    # Check the given word is exists in the dictionary if starts with capital letter
    elif word.title() in myData:
        return(myData[word.title()])
    # Check the given word is exists in the dictionary if the word is acronym
    elif word.upper() in myData:
        return(myData[word.upper()])
    # Search a word what is similar with the user`s word. It is handy when the user made typo
    elif len(get_close_matches(word, myData.keys())) > 0:
        userAnswer = str(input('Did you mean: %s? Press y if yes and n if no: ' % get_close_matches(word, myData.keys())[0]))
        if userAnswer.lower() == 'y':
            return myData[get_close_matches(word, myData.keys())[0]]
        elif userAnswer == 'n':
            return '\nThis word doesn`t exists. Please add new word!'
        else:
            return '\nHmm sorry but I don`t understand what you wrote.'
    else:
        return '\nThis word doesn`t exists. Please add new word!'

def noArgv():
    running = True
    while running:
        # Get a word from the user
        print('\nType a word for translate or type --quit to exit program.')
        userWord = str(input('\nEnter a word: '))
        if userWord == '--quit':
            print('\nThank you. Bye!')
            running = False
        else:
            # Send the user`s word to translate
            result = translate(userWord.lower())
            # Check te result is translated or it is just a message
            if type(result) == list:
                for line in result:
                    print(line)
            else:
                print(result)

def withArgv(userWord):
    result = translate(userWord.lower())
    # Check te result is translated or it is just a message
    if type(result) == list:
        for line in result:
            print(line)
    else:
        print(result)

if len(sys.argv) >1:
    withArgv(sys.argv[1])
else:
    noArgv()

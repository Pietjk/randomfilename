import os
import json
import random
import textPrinter as tp

running = True

def program(old_path = None):
    tp.Dialogue.get('opening')

    # Get users filepath
    global given_path
    if old_path == None:
        given_path = input('\nGive a filepath: ')
    else:
        given_path = old_path
        
    file_list = []

    # Check if user is trying to access root or windows os directories
    if(os.path.dirname(given_path) == given_path or os.environ['WINDIR'].upper() == given_path.upper()):
        tp.Dialogue.get('rootException')
        exit()

    # Check if filepath exists
    assert os.path.exists(given_path), 'I could not find anything at '+str(given_path)

    # Loop over files in falpath and append them to file_list
    print('Your chosen path is: '+ str(given_path))
    for root, dirs, files in os.walk(given_path):
        for file in files:
            file_list.append(os.path.join(root,file))  

    # Open json word list
    dirname = os.path.dirname(__file__)
    words_json = os.path.join(dirname, 'words.json')
    f = open(words_json)
    data = json.load(f) # 177957 words
    word = ''
    names = []

    # Loop over all files
    for file in file_list:
        # Genrate a new name with 3 random words from the json file 
        for i in range(3):
            new_word = data[random.randrange(0, len(data))]
            word += str(new_word).capitalize()
        # Get extension
        extension = file.split('.')[-1]
        # Rename each file
        os.rename(file, given_path + '\\' + word + '.' + extension)
        # Get all names in a list to show in the end
        names.append(word + '.' + extension)
        word = ''

    # Display closing dialogue
    tp.Dialogue.get('end', names)
    
    restart = input('\nDo you want to restart? (y/n) ')

    if restart == 'n' or restart == 'no':
        tp.Dialogue.get('bye')
        global running
        running = False

    if restart == 'y' or restart == 'yes':
        reset = input('\nDo you want to use the previous directory? (y/n) ')

        if reset == 'y' or reset == 'yes':
            program(given_path);

while running == True:
    program()

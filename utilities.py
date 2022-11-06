import random
import os
import json
import textPrinter as tp

class Utils:
    def getWords():
        dirname = os.path.dirname(__file__)
        words_json = os.path.join(dirname, 'words.json')
        f = open(words_json)
        data = json.load(f) # 177957 words
        return data

    def getFiles(path):
        file_list = []

        for root, dirs, files in os.walk(path):
            for file in files:
                file_list.append(os.path.join(root,file))

        return file_list

    def generateNames(path):
        file_list = Utils.getFiles(path)
        data = Utils.getWords()
        word = ''
        names = []

        for file in file_list:
            # Genrate a new name with 3 random words from the json file 
            for i in range(3):
                new_word = data[random.randrange(0, len(data))]
                word += str(new_word).capitalize()

            # Get extension
            extension = file.split('.')[-1]

            # Rename each file
            os.rename(file, path + '\\' + word + '.' + extension)

            # Get all names in a list to show in the end
            names.append(word + '.' + extension)
            word = ''

        return names

    def validateRequest(path):
        # Check if filepath exists
        assert os.path.exists(path), 'I could not find anything at '+str(path)

        # Check if user is trying to access root or windows os directories
        if(os.path.dirname(path) == path or os.environ['WINDIR'].upper() == path.upper()[:10]):
            tp.Dialogue.get('rootException')
            exit()

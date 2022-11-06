import time

class Dialogue:
    def get(section, variable = None):
        if section == 'opening':
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(')                                          (')
            print('(     Welcome to randomfilename-inator     )')
            print(')                                          (')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif section == 'rootException':
            print('You are not alowed to change these directories')
            time.sleep(1)
            print('Shutting down...')
            time.sleep(1)
        elif section == 'end':
            print('-----------------------------')
            for name in variable:
                print(name)
                print('-----------------------------')
            print('\nDone! Thank you for using randomfilename-inator!')
            time.sleep(1)
            print('\nAbove are your new filenames ^')
            print('                             |')
            time.sleep(5)
            print('\nGoodbye!')
            time.sleep(1)
import textPrinter as tp
import utilities as ut

running = True

def program(old_path = None):
    tp.Dialogue.get('opening')

    # Get users filepath
    global given_path
    if old_path == None:
        given_path = input('\nGive a filepath: ')
    else:
        given_path = old_path

    # Validate the given filepath
    ut.Utils.validateRequest(given_path)
    
    # generate names
    names = ut.Utils.generateNames(given_path)

    # Display closing dialogue
    tp.Dialogue.get('end', names)
    
    # Restart the app if desired, also save the previous directory if desired
    restart = input('\nDo you want to restart? (y/n) ')

    # Shut down app
    if restart == 'n' or restart == 'no':
        tp.Dialogue.get('bye')
        global running
        running = False

    # Restart app
    if restart == 'y' or restart == 'yes':
        # save old directory
        reset = input('\nDo you want to use the previous directory? (y/n) ')
        if reset == 'y' or reset == 'yes':
            program(given_path);

while running == True:
    program()

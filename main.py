import datetime as dt

def mainMenu():
    choice = input('Welcome to the MyMoneyMyProblems Program.\n'
                   'Enter your choice (1-4):\n'
                   '1. Make a new tracker\n'
                   '2. Open an existing tracker\n'
                   '3. Delete a tracker\n'
                   '4. Exit\n')
    return choice

def createTracker(trackers):

    try:

        trackerName = input('Tracker name: ')
        monthlyAllowance = float(input('Monthly allowance (GBP): '))
        needsPot = float(input('How much do you want to allocate to your NEEDS pot? (%): ')) / 100 * monthlyAllowance
        savingsPot = float(input('How much do you want to allocate to your SAVINGS pot? (%): ')) / 100 * monthlyAllowance

        if needsPot + savingsPot > monthlyAllowance:
            print('Allocation exceeds 100%. Please try again.\n')
            return

        wantsPot = monthlyAllowance - needsPot - savingsPot

    except ValueError:
        print('Invalid value. Please enter a number.\n')
        return

    print(f'\nTracker name: {trackerName}')
    print(f'Monthly allowance: {monthlyAllowance}')
    print(f'Needs : Savings : Wants')
    print(f'{needsPot:.2f} : {savingsPot:.2f} : {wantsPot:.2f}')

    needsFraction = needsPot / monthlyAllowance
    savingsFraction = savingsPot / monthlyAllowance
    wantsFraction = wantsPot / monthlyAllowance

    confirm = input('Confirm if this split correct? (Y/N)\n')
    if confirm == 'Y':
        trackers[trackerName] = {
            'Monthly Allowance' : monthlyAllowance,
            'Needs Pot' : [needsPot, needsFraction],
            'Savings Pot' : [savingsPot, savingsFraction],
            'Wants Pot' : [wantsPot, wantsFraction],
            'Expenses' : {
                'Needs' : [],   # list of lists [name, amount, date]
                'Savings' : [],
                'Wants' : [],
                'Total spend' : 0
            }
        }

        print(f'Tracker {trackerName} added.')
        print('Returning to main menu...\n')
    else:
        print('Tracker creation cancelled.')
        print('Returning to main menu...\n')

def displayerTracker(tracker, trackers):
    ...
    ''' 
    Display stats:
    - Monthly allowance
    - Needs, savings, wants split
    - Howm much you are below, above, or on track with each pot
    - Next upcoming expense and how much it costs
    '''

def trackerMenu(tracker):
    choice = input(f'Tracker {tracker} menu:\n'
                    '1. Add expense\n'
                    '2. Update expense\n'
                    '3. Remove expense\n'
                    '4. Update tracker name\n'
                    '5. Export tracker\n'
                    '6. Discard changes and exit\n'
                    '7. Save and exit\n')
    return choice

def deleteTracker(tracker, trackers):
    trackers.pop(tracker, None)

def main():

    example1 = {
            'Monthly Allowance' : 2500,
            'Needs Pot' : [1000.0, 0.4],
            'Savings Pot' : [500.0, 0.2],
            'Wants Pot' : [1000, 0.4],
            'Expenses' : {}
        }
    
    example2 = {
            'Monthly Allowance' : 2000,
            'Needs Pot' : [800.0, 0.4],
            'Savings Pot' : [600.0, 0.3],
            'Wants Pot' : [600, 0.3],
            'Expenses' : {}
        }

    trackers = {'Test1' : example1,
                'Test2' : example2}

    while True:

        choiceMain = mainMenu()

        match choiceMain:
            case '1':   # Add a new tracker
                createTracker(trackers)

            case '2':   # Open a tracker
                print('Trackers available:')
                for key, value in trackers.items():
                    print(key)
                print('(Exit)')
                tracker = input('Choose a tracker:\n').strip()

                if tracker not in trackers:
                    print('Tracker not in list.')
                    print('Returning to main menu...\n')
                elif tracker == 'Exit':
                    print('Returning to main menu...\n')
                else:
                    #displayTracker(tracker, trackers)
                    choiceTracker = trackerMenu(tracker)

                    match choiceTracker:
                        case '1':   # Add expense
                            ...
                        case '2':   # Update expense
                            ...
                        case '3':   # Delete expense
                            ...
                        case '4':   # Update tracker name
                            ...
                        case '5':   # Export tracker
                            ...
                        case '6':   # Discard changes and exit
                            ...
                        case '7':   # Save and exit
                            ...
                        case _:
                            print('Invalid choide, try again\n')
            
            case '3':   # Delete a Tracker
                print('Trackers available:')
                for key, value in trackers.items():
                    print(key)
                print('(Exit)')
                tracker = input('Choose a tracker:\n').strip()

                if tracker not in trackers:
                    print('Tracker not in list.')
                    print('Returning to main menu...')
                elif tracker == 'Exit':
                    print('Returning to main menu...\n')
                else:
                    print(f'Tracker {tracker} deleted.\n')
                    deleteTracker(tracker, trackers)
                    

            case '4':   # Exit program
                print('Exiting program...')
                break

            case _:
                print('Invalid choide, try again\n')




if __name__ == '__main__':
    main()
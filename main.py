def mainMenu():
    choice = input('Welcome to the MyMoneyMyProblems Program.\n'
                   'Enter your choice (1-4):\n'
                   '1. Make a new tracker\n'
                   '2. Open an existing tracker\n'
                   '3. Delete a tracker\n'
                   '4. Exit\n')
    return choice

def createTracker(trackers):
    ...
    '''
    What do you want to call this tracker?
    What is your monthly allowance?
    How much do you want to allocate to your NEEDS pot? (bills, fixed payments, loans, etc.)
    How much do you want to allocate to your SAVINGS pot? (ISA's, stocks and shares, etc.)
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
    ...

def main():

    trackers = {'Test1' : 1,
                'Test2' : 2}

    while True:

        choiceMain = mainMenu()

        match choiceMain:
            case '1':   # Add a new tracker
                createTracker(trackers)

            case '2':   # Open a tracker
                print('Trackers available:')
                for key, value in trackers.items():
                    print(key)
                tracker = input('Choose a tracker:\n')

                if tracker not in trackers:
                    print('Tracker not in list\n')
                else:
                    choiceTracker = trackerMenu(tracker, trackers)

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
                tracker = input('Choose a tracker:\n')

                if tracker not in trackers:
                    print('Tracker not in list\n')
                else:
                    deleteTracker(tracker, trackers)

            case '4':   # Exit program
                print('Exiting program...')
                break

            case _:
                print('Invalid choide, try again\n')




if __name__ == '__main__':
    main()
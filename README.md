# MyMoneyMyProblems
A little program for myself to add and track my personal finances. Separating a given monthly allowance into my needs, wants, and savings.

Welcome to my first little Github project. I've decided to put my python into practice by demonstrating how to manipulate multiple data types such as dictionaries, lists and others. You will be welcomed by a 
nice little menu interface presenting you options to:

1. Make a new finance tracker
2. Open and edit an existing finance tracker
3. Delete a finance tracker
4. Exit

For the first time you use the program there are currently no trackers of course and you will default start making your first one. You will be asked multiple set up questions such as:

1. What do you want to call this tracker?
2. What is your monthly allowance?
3. How much do you want to allocate to your NEEDS pot? (bills, fixed payments, loans)
4. How much do you want to allocate to your SAVINGS pot? (ISA's, stocks and shares, etc.)

The remaining amount will be your allowance for your WANTS pot.

Once set up, you will create a whole new nested dictionary which branches off to detail dictionaries of your NEEDS, SAVINGS, and WANTS.

This is the menu for when you open an existing tracker, which will display your latest (unsaved) tracker:

1. Add expense
2. Update expense
3. Remove expense
4. Update tracker name
5. Export tracker
6. Discard changes and exit
7. Save and exit

You have the choice to add/delete/update the entries in each dictionary assigning the type of expense as keys, and then a dictionary of costs, and the dates these costs are incurred.

The sum of the values in each dictionary will be compared to the proposed % allowance you give for each pot and informs you if you are under or over the allowance you set up, so you know if you need to rebalance your allowance better or not.

When exporting the tracker, it will create a csv file that you can use which details all of your expenses, which pots they are in, and its further details you've provided for each expense

Lessons learned:
Python data structures:
- this project has helped me reinforce my understanding of dictionaries and lists, and how to organise nested data

User input validation:
- practicing putting in validation code to ensure the variables of my code are in the correct format and preventing errors and crashes down the line

Menu design and user experience:
- desigining a simple command line interface menu and learning to build more intuitive interfaces, and handling user actions

CSV export logic:
- creating a CSV export to practice file I/O and structuring data for external use

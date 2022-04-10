import os
from tabulate import tabulate
import uuid
import csv

def intro(name):
    table=['            Marketplace               ',f'            name:{name}']
    print(tabulate(table))
def orders_marketplace():
    print('----------------------------------------------')
    print('--Press 1 to acces an existing marketplace ---')
    print('----------------------------------------------')
    print('--Press 2 to create a new marketplace --------')
    print('----------------------------------------------')
    print('--Press 3 to delete a old marketplace---------')
    print('----------------------------------------------')
    command=input('Command:')
    return command
def orders():
    print('-------------------------------')
    print('-Press 1 to add a new client---')
    print('-------------------------------')
    print('-Press 2 to find a client  ----')
    print('-------------------------------')
    print('-Press 3 to delete a client   -')
    print('-------------------------------')
    do=input(f'Command for "{name}" contact book:')
    return do

redo_name='r'
while redo_name == 'r' or redo_name == 'R':
    do_marketplace = orders_marketplace()
    if do_marketplace == '1':
        name = input('Contact marketplace name:')
        if os.path.exists(f"{name}.csv"):
            intro(name)
            redo = "r"
            while redo == "r" or redo == "R":
                do = orders()
                if do == "1":
                    entry_user_name = input('User name:')
                    list_of_products=[]
                    while True:
                        product=input(f'Choose a product to add to {name}\'s command:' )
                        list_of_products.append(product)
                        add_more=input("Wish to add something else(Y/N):")
                        if add_more!='Y' and add_more!='y':
                            break
                    command_nr = uuid.uuid4()

                    with open(f'{name}.csv', 'a') as f:
                        elements=''
                        for elem in list_of_products:
                            if elements=='':
                                elements=elem
                            else:
                                elements = elements + ',' + elem

                        f.write(f'{entry_user_name},{elements},{command_nr}\n')

                    print('For the new command to be added to the marketplace please re-run the program')
                    redo = input("If you wish to make another option press (R) key if not press (Enter):")
                elif do == '3':
                    print('{Please enter the name for the entry you want to delete->}')
                    del_name = input('Name:')
                    os.remove(f"backup_file.csv")
                    with open(f"{name}.csv", 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        for row in csv_reader:
                            if row[0] != del_name:
                                with open(f'backup_file.csv','a') as f:
                                    row_str=''
                                    for elem in row:
                                        if row_str=='':
                                            row_str=elem
                                        else:
                                            row_str=row_str+','+elem
                                    f.write(f'{row_str}\n')
                    os.remove(f"{name}.csv")

                    with open(f"backup_file.csv", 'r') as f:
                        f = csv.reader(f)
                        for row in f:
                            add=str(row)
                            with open(f'{name}.csv', 'a') as f:
                                row_str = ''
                                for elem in row:
                                    if row_str=='':
                                        row_str = elem
                                    else:
                                        row_str = row_str + ',' + elem
                                f.write(f'{row_str}\n')
                    redo = input("If you wish to make another option press (R) key if not press (Enter):")
                elif do == '2':
                    count_find = False
                    find = input('Find client:')
                    print(f'Search for {find}:')
                    with open(f"{name}.csv", 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        for row in csv_reader:
                            if row[0]==find:
                                print(f'#{row}')
                                count_find = True
                    if count_find == False:
                        print(f'There is no contact containing "{find}"')
                    redo = input("If you wish to make another option press (R) key if not press (Enter):")
                else:
                    print("You did not select a valid option")
                    redo = input("If you wish to make another option press (R) key if not press (Enter):")
            redo_name = input('If you wish to go back to the main menu press (R) if not press (Enter):')
        else:
            print(f'There is no contact book named:{name}')
            redo_name = input(
                'If you wish to add a new contact book pres (R) and the choose option "2" if not press (Enter):')
    elif do_marketplace == '2':
        name = input('New marketplace name:')
        if os.path.exists(f"{name}.csv"):
            print(f'There is allready a contact book called {name}')
        else:
            with open(f'{name}.csv', 'w') as f:
                f.write('')
            print("For the new marketplace to be avalable please re-run the project")
        redo_name = input('If you wish to go back to the main menu press (R) if not press (Enter):')
    elif do_marketplace=='3':
        delete_retry='r'
        while delete_retry=='r' or delete_retry=='R':
            delete_marketplace=input(f"Enter the name of the contact book you would wish to remove:")
            if os.path.exists(f"{delete_marketplace}.txt"):
                os.remove(f"{delete_marketplace}.txt")
                print("For the contact book to be deleted please re-run the project")
                delete_retry=input("If you wish to delete another contact book press (R) if not press (Enter)")
            else:
                print(f'There is no contact book called "{delete_marketplace}"')
                delete_retry=input("If you wish to try another name press (R) if not press (Enter)")
        redo_name=input('If you wish to go back to the main menu press (R) if not press (Enter)')
    else:
        print("You did not select a valid option")
        redo_name = input('If you wish to go back to the main menu press (R) if not press (Enter)')




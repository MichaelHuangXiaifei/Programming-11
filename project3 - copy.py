# project3 - Building a Library with Python Dictionary
import time


database = open('library_database.txt')

library_database = eval(database.read())
database.close()
print('Library')
while True:
    book_name = input('What is the book you want to search for?\n')
    if book_name in library_database:
        print('Author: %s\n%d copies available' % (library_database[book_name][0], library_database[book_name][1]))
        if library_database[book_name][1] == 0:
            print('Please search for another book')
            time.sleep(2)
            continue
        elif library_database[book_name][1] > 0:
            answer = input('Do you want to borrow/return a copy? B/R/N\n')
            if answer == 'B':
                library_database[book_name][1] -= 1
                database = open('library_database.txt', mode='w')
                database.write(str(library_database))
                database.close()
                print('You have borrowed a copy of %s' % book_name)
                time.sleep(2)
                continue
            if answer == 'R':
                library_database[book_name][1] += 1
                database = open('library_database.txt', mode='w')
                database.write(str(library_database))
                database.close()
                print('You have returned a copy of %s' % book_name)
                time.sleep(2)
                continue
            elif answer == 'N':
                print('Happy to help')
                time.sleep(2)
                continue
            else:
                print('Happy to help')
                time.sleep(2)
                continue
        else:
            print('\n' * 100, 'SystemError: Please ask administrator for help')
            exit()
    else:
        answer = input("%s doesn't exist in our library, would you like to add it? Y/N\n" % book_name)
        if answer == 'Y':
            author = input('Who is the author of this book?\n')
            number_of_copies = int(input('How many copies would you like to add?\n'))
            library_database[book_name] = [author, number_of_copies]
            database = open('library_database.txt', mode='w')
            database.write(str(library_database))
            database.close()
            print("You have successfully added %s to our library" % book_name)
            time.sleep(2)
            continue
        elif answer == 'N':
            print('Happy to help')
            time.sleep(2)
            continue
        else:
            print('Happy to help')
            time.sleep(2)
            continue

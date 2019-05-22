# project3
import time


library_data_base = {"Harry Potter": ["JK Rowling", 3],
                     "Tom Sawyer": ["Mark Twain", 2],
                     "The Tale of Two Cities": ["Charles Dickens", 5]}
print('Library')
while True:
    book_name = input('What is the book you want to search for?\n')
    if book_name in library_data_base:
        print('Author: %s\n%d copies available' % (library_data_base[book_name][0], library_data_base[book_name][1]))
        if library_data_base[book_name][1] <= 0:
            print('Please search for another book')
            time.sleep(2)
            continue
        else:
            answer = input('Do you want to borrow a copy? Y/N\n')
            if answer == 'Y':
                library_data_base[book_name][1] -= 1
                print('You have borrowed a copy of %s' % book_name)
                time.sleep(2)
                continue
            elif answer == 'N':
                print('Happy to help')
                break
            else:
                print('Happy to help')
                time.sleep(2)
                continue
    else:
        answer = input("%s doesn't exist in our library, would you like to add it? Y/N\n" % book_name)
        if answer == 'Y':
            author = input('Who is the author of this book?\n')
            number_of_copies = input('How many copies would you like to add?\n')
            library_data_base[book_name] = [author, number_of_copies]
            print("You have successfully added Journey to the West to our library")
            time.sleep(2)
            continue

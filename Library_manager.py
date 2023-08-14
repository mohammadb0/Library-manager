import sys
from colorama import Fore, Style, Back

# defind book object
class book:

    def __init__(self, name, author, yearpublication, quantity):
        self.name = name
        self.author = author
        self.yearpublication = yearpublication
        self.quantity = quantity

# defind user object
class user:

    def __init__(self, user, userpassword, Role):
        self.name = user
        self.password = userpassword
        self.Role = Role
        self.borrowe=[]

    # function for access of user to menu
    def access(self, student):
        # The object of student
        self.student = student
        # print Role of student object
        if self.student.Role == '2':
            acc = int(input('The user menu\n1.Borrowebook\n2.Givebackbook\n3.search book.\n4.Booklist\n5.See working time\n6.Watch bestbook of this week\n7.Login again\n8.exit from program\n=====>'))
            if acc == 1:
                user.borrowebook(self)

            if acc == 2:
                user.givebackbook(self)

            if acc == 3:
                user.searchbookavailable(self)

            if acc == 4:
                Bookmanager.Booklist(1, self.student)

            if acc == 5:
                collegian.Time(self)

            if acc == 6:
                collegian.bestbook(self)

            if acc == 7:
                Run(1)

            if acc == 8:
                sys.exit()

        if self.student.Role == '3':
            acc = int(input(
                'The user menu\n1.Borrowebook\n2.Givebackbook\n3.search book.\n4.Booklist\n5.See working time\n6.Login again\n7.exit from program\n=====>'))
            if acc == 1:
                user.borrowebook(self)

            if acc == 2:
                user.givebackbook(self)

            if acc == 3:
                user.searchbookavailable(self)

            if acc == 4:
                Bookmanager.Booklist(1, self.student)

            if acc == 5:
                studentt.Time(self)

            if acc == 6:
                Run(1)

            if acc == 7:
                sys.exit()

    # the func for borrow book from booklist in bookmanager
    def borrowebook(self):
        for book in Bookmanager.booklist1:
            print(
                f'Bookname:{book.name}---Author:{book.author}---Yearpublication:{book.yearpublication}---quantity:{book.quantity}\n\n')
        borrow = input('Enter bookname:')
        # Search book in library
        for book in Bookmanager.booklist1:
            if borrow == book.name:
                # if quantity of book was 1 removed at all
                if book.quantity == 1:
                    Bookmanager.booklist1.remove(book)

                    for number, objectt in enumerate(Users.Userlist):
                        if objectt == self.student:
                            Users.borrowlist[number].append(borrow)
                            print(f"You borrow {borrow} enjoy it")
                            user.access(self, self.student)

                # else quantity was more than 1, program remove one from all available book that you borrowed
                else:
                    book.quantity = book.quantity-1
                    for number, objectt in enumerate(Users.Userlist):
                        if objectt == self.student:
                            Users.borrowlist[number].append(borrow)
                            print(f"You borrow {borrow} enjoy it")
                            user.access(self, self.student)

        # run if the book is not available
        print('This book is not available.')
        user.access(self, self.student)
        
    # the func for giveback book that borrow
    def givebackbook(self):
        give = input('Enter the book you want giveback:')
        for book in Bookmanager.booklist:
            # if statement for cheak there is this book in library or not
            if give == book.name:
                # cheak for the book is available in boolist1 to add one quantiti to that or add new book to this list
                for books in Bookmanager.booklist1:
                    if books.name == give:
                        # add one to number of book
                        books.quantity += 1
                        # When you wanna giveback book that you didn't take it, return a error massage and return to menu
                        try:
                            # find number of user'element in Userlist and set borrowbook for him to borrowlist
                            for number, objectt in enumerate(Users.Userlist):
                                if objectt == self.student:
                                    Users.borrowlist[number].remove(give)
                                    print('Your book givebacked')
                                    # add book again to booklist1 because book
                                    Bookmanager.booklist1.append(books)
                                    user.access(self, self.student)
                        except:
                            print(
                                'This book is not belong to you or you write wrong name')
                            user.access(self, self.student)

                    # When book is not in booklist1 and there is in booklist ,this add book to booklist1 instead of add quantiti
                    try:
                        for number, objectt in enumerate(Users.Userlist):
                            if objectt == self.student:
                                Users.borrowlist[number].remove(give)
                                Bookmanager.booklist1.append(books)
                                print('Your book givebacked')
                                user.access(self, self.student)
                    except:
                        print(
                            'This book is not belong to you or you write wrong name')
                        user.access(self, self.student)
        # finally when the book there is not in library
        print('This book is not belong to our library')
        user.access(self, self.student)

    # define func for searching book for user(student)
    def searchbookavailable(self):
        bookname = input('Enter search:')
        for book in Bookmanager.booklist1:
            # cheak be same name of searched and book object name
            if book.name == bookname:
                print(
                    f'Bookname:{book.name}---Author:{book.author}---Yearpublication:{book.yearpublication}----quantity:{book.quantity}\n')
                user.access(self, self.student)

        print('This book is not available.')
        user.access(self, self.student)

#inheritance collegian class from user
class collegian(user):
    Timelist = ['8 AM', '1 PM', '5 PM', '10 PM']

    def __init__(self, name, password, Role):
        user.__init__(self, name, password, Role)

    def Time(self):
        print(
            f'Library working hours for collegian\nOpen:{collegian.Timelist[0]}-----Close:{collegian.Timelist[1]}\nOpen:{collegian.Timelist[2]}-----Close:{collegian.Timelist[3]}')
        collegian.access(self, self.student)

    def bestbook(self):
        print('The bestbook of this week is Atomic Habits')
        collegian.access(self, self.student)


#inheritance student class from user
class studentt(user):
    Timelist = ['8 AM', '1 PM', '5 PM', '10 PM']

    def __init__(self, name, password, Role):
        user.__init__(self, name, password, Role)

    def Time(self):
        print(
            f'Library working hours for student\nOpen:{studentt.Timelist[0]}-----Close:{studentt.Timelist[1]}\nOpen:{studentt.Timelist[2]}-----Close:{studentt.Timelist[3]}')
        studentt.access(self, self.student)


# defind Users class for access admin to edit user and book
class Users:
    Userlist = []
    borrowlist = []

    def __init__(self, userr, password):
        self.user = userr
        self.password = password
        # cheak user and password
        if self.user == Users.Userlist[0].name and self.password == Users.Userlist[0].password:
            print('------------------------Welcom admin---------------------------')
            Users.Admin(self)
        # cheak if user not be admin
        for us in Users.Userlist:
            if self.user == us.name and self.password == us.password:
                if us.Role == '3':
                    print('----Welcom student----')
                    user.access(self, us)
                elif us.Role == '2':
                    print('----Welcom collegian----')
                    user.access(self, us)

        print('This user not found')
        Run(1)

    # func that define menu access for admin
    def Admin(self):

        number = int(input(Fore.RED+f"-----The main menu-----\n{Style.RESET_ALL}\
|1.Add new user.|\n|2.Remove user|\n|3.Userlist|\n|4.Change time of working of library|\n|5.Search user. |\n|6.Bookmanager  |\n|7.login again. |\n|8.exit from program|\n-------->"))
        if number == 1:
            Users.Adduser(self)

        if number == 2:
            Users.Removeuser(self)

        if number == 3:
            Users.userlistt(self)

        if number == 4:
            Users.changetime(self)

        if number == 5:
            Users.Searchuser(self)

        if number == 6:
            Bookmanager()
        # go ro Run fun that takes user and password again
        if number == 7:
            Run(1)
        # order for exit from program
        if number == 8:
            sys.exit()

    def Adduser(self):
        file.update(1)
        name = input('Enter newusername:')
        passw = input('Enter his/her password:')
        role = input('Enter the role of user:\n2.collegian\n3.student\n====>')
        file.write(name, passw, role)
        file.update(1)
        Users.borrowlist.append([])
        Users.Admin(self)

    def Removeuser(self):
        for number, user in enumerate(Users.Userlist):
            print(
                f"\nUsername:{user.name}\nPassword:{user.password}\nBorrowed book:{Users.borrowlist[number]}\nRole:{'Collegian'if user.Role=='2' else 'Student' if user.Role=='3' else 'Admin'}")
        name = input("\nEnter name of user you wanna deleted: ")

        if name == 'admin':
            print('You can not delete this user')
            Users.Admin(self)
        file.removefile(name)
        Users.Admin(self)

    def userlistt(self):
        # file.update(1)
        for number, user in enumerate(Users.Userlist):
            print(
                f"\nUsername:{user.name}\nPassword:{user.password}\nBorrowed book:{Users.borrowlist[number]}\nRole:{'Collegian'if user.Role=='2' else 'Student' if user.Role=='3' else 'Admin'}")
        Users.Admin(self)

    def changetime(self):
        number = int(
            input('You wanna change the time of 1.student or 2.collegian?:'))
        if number == 1:
            studentt.Timelist[0] = input(
                'Enter time of opening library at morning:')
            studentt.Timelist[1] = input(
                'Enter time of closing library at morning:')
            studentt.Timelist[2] = input(
                'Enter time of opening library at evening:')
            studentt.Timelist[3] = input('Enter time of opening library at night:')
            Users.Admin(self)
        if number == 2:
            collegian.Timelist[0] = input(
                'Enter time of opening library at morning:')
            collegian.Timelist[1] = input(
                'Enter time of closing library at morning:')
            collegian.Timelist[2] = input(
                'Enter time of opening library at evening:')
            collegian.Timelist[3] = input(
                'Enter time of opening library at night:')
            Users.Admin(self)

    # the func for admin who can search in users
    def Searchuser(self):
        file.update(1)
        username = input('Enter search:')
        for number, user in enumerate(Users.Userlist):
            if user.name == username:
                print(
                    f"\nUsername:{user.name}\nPassword:{user.password}\nBorrowed book:{Users.borrowlist[number]}\nRole:{'Collegian'if user.Role=='2' else 'Student' if user.Role=='3' else 'Admin'}")
                Users.Admin(self)

        print('This user not found')
        Users.Admin(self)

class file:
    #add new user to file and update userlist again
    def write(name, password, role):
        with open('userlist.txt', 'r+') as f:
            userfile = f.readlines()
            f.seek(0)
            l = []
            for number, line in enumerate(userfile):
                l.append(number)
            with open('userlist.txt', 'a+') as f:
                if sum(l) == 0:
                    f.writelines(f'{name} ')
                    f.writelines(password+' ')
                    f.writelines(role+' ')

                else:
                    f.writelines(f'\n{name} ')
                    f.writelines(password+' ')
                    f.writelines(role+' ')
    #add text of file to user class and add as object in userlist
    def update(num):
        if num == 2:
            L = []
            Users.Userlist = []
            with open('userlist.txt', 'r+') as Userl:
                lines = Userl.readlines()
                Userl.seek(0)
                for line in lines:
                    # convert elements of line to the str in list
                    l = line.split()
                    # add element of line in list
                    L.append(l)
                for element in L:
                    name = element[0]
                    password = int(element[1])
                    role = element[2]
                    if role == '2':
                        newuser = collegian(name, password, role)
                        Users.Userlist.append(newuser)
                    elif role == '3':
                        newuser = studentt(name, password, role)
                        Users.Userlist.append(newuser)
                    else:
                        newuser = user(name, password, role)
                        Users.Userlist.append(newuser)

            for line in Users.Userlist:
                Users.borrowlist.append([])
        else:
            L = []
            Users.Userlist = []
            with open('userlist.txt', 'r+') as Userl:
                lines = Userl.readlines()
                Userl.seek(0)
                for line in lines:
                    # convert elements of line to the str in list
                    l = line.split()
                    # add element of line in list
                    L.append(l)
                for element in L:
                    name = element[0]
                    password = int(element[1])
                    role = element[2]
                    if role == '2':
                        newuser = collegian(name, password, role)
                        Users.Userlist.append(newuser)
                    elif role == '3':
                        newuser = studentt(name, password, role)
                        Users.Userlist.append(newuser)
                    else:
                        newuser = user(name, password, role)
                        Users.Userlist.append(newuser)
    #remove from file
    def removefile(name):
        for number, userr in enumerate(Users.Userlist):
            if userr.name == name:
                Users.borrowlist.pop(number)
                password = userr.password
                role = userr.Role

        with open('userlist.txt', 'r') as readfile:
            lines = readfile.readlines()
            readfile.seek(0)
            with open('userlist.txt', 'w') as writefile:
                for line in lines:
                    # choose specific user's name and delete \n with strip
                    if line.strip() != name+' '+str(password)+' '+role+'':
                        writefile.write(f'{line}')
                        f = 1
        if f == 1:
            print('-Removed was seccesfuly-')
        file.update(1)

# defind the bookmanager class for admin to access add book and...
class Bookmanager:
    # booklist static
    booklist = [book('Atomic Habits', 'jeamz', 1900, 1),
                book('Ulysses', 'James Joyce', 1904, 1)]
    # booklist not static, the booklist that borrowe from it
    booklist1 = [book('Atomic Habits', 'jeamz', 1900, 1),
                 book('Ulysses', 'James Joyce', 1904, 1)]

    def __init__(self):
        print(Fore.BLUE+f"Bookmanager menu", end='')
        print(Style.RESET_ALL)
        set0 = int(input(
            f"1.Addbook.\n2.Removebook\n3.Booklist\n4.Searchbook\n5.back to admin menu\n------>"))
        if set0 == 1:
            Bookmanager.Addbook()
        if set0 == 2:
            Bookmanager.Removebook()
        if set0 == 3:
            Bookmanager.Booklist(0, ' ')
        if set0 == 4:
            Bookmanager.Searchbook()
        if set0 == 5:
            Users.Admin(self)

    def Addbook():
        name = input("Enter book's name:")
        author = input("Enter its author:")
        yearpublication = input("Enter its yearpublication:")
        quantity = int(input('Enter number of book you want add:'))
        newbook = book(name, author, yearpublication, quantity)
        Bookmanager.booklist.append(newbook)
        Bookmanager.booklist1.append(newbook)
        # run 'back' fun to do again fun or back to main menu
        Bookmanager.back(1)

    def Removebook():
        for book in Bookmanager.booklist1:
            print(
                f'Bookname:{book.name}---Author:{book.author}---Yearpublication:{book.yearpublication}---quantity:{book.quantity}\n\n')

        name = input("Enter book's name you want delete:")
        # iterate for find Intended book
        for book in Bookmanager.booklist:
            if book.name == name:
                if book.quantity == 1:
                    Bookmanager.booklist.remove(book)
                else:
                    book.quantity = book.quantity-1
                print('The book removed')
                Bookmanager.back(2)
        print("This book not found")
        # same
        Bookmanager.back(2)

    @staticmethod
    def Booklist(N, user):
        if N == 0:
            for book in Bookmanager.booklist:
                print(
                    f'Bookname:{book.name}---Author:{book.author}---Yearpublication:{book.yearpublication}---quantity:{book.quantity}\n')
        if N == 1:
            for book in Bookmanager.booklist1:
                print(
                    f'Bookname:{book.name}---Author:{book.author}---Yearpublication:{book.yearpublication}---quantity:{book.quantity}\n')

        if N == 0:
            Bookmanager.back(3)
        elif N == 1:
            user.access(user)

    # bug ,show 3time book list on adiitaon quantiti
    def Searchbook():
        bookname = input('Enter search.')
        # bug,quntiti dosen't deleted

        for book in Bookmanager.booklist:
            if bookname in book.name:
                print(
                    f'\nBookname:{book.name}---Author:{book.author}---Yearpublication:{book.yearpublication}---quantity:{book.quantity}\n')
                f = 1
        if f == 1:
            Bookmanager.back(4)
        else:
            print("This book doesn't exist")
            Bookmanager.back(4)

    # the staticmethod for "back fun" that Specifies 'back to main menu' or 'do again' past fun
    @staticmethod
    def back(N):
        backmenu = int(input(f"1.Back menu\n2.Do agein\n---->"))
        n = N
        if backmenu == 1:
            Bookmanager()
        # the first Condition- is for what fun in bookmanager,second Condition is for back main menu or do again specified fun
        elif N == 1 and backmenu == 2:
            Bookmanager.Addbook()
        # same
        elif N == 2 and backmenu == 2:
            Bookmanager.Removebook()

        elif N == 3 and backmenu == 2:
            Bookmanager.Booklist(0, '')

        elif N == 4 and backmenu == 2:
            Bookmanager.Searchbook()
        else:
            print('Your intery is not valid')
            Bookmanager.back(n)

# Runing function
## if defind num for creting number of borrowbook list in User when num==2 
## set number of bororowbook list else do thier job
def Run(num):
    file.update(num)
    name = input(Back.CYAN+"Enter your username: ")
    password = int(input("Enter your password: "))
    print(Style.RESET_ALL)
    Users(name, password)


Run(2)

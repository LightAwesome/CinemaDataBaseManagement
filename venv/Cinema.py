import mysql.connector as con
import random
import string

sql = con.connect(host="localhost", password='Apple@10', user='root', database='cinema')
cursor = sql.cursor()
is_login = False
seats_exist = False
seats_list = []
ROWS = []
COLUMN = []


def register():
    # insert
    user_name = str(input('Enter the username: '))
    password = user_name[:3].upper() + str(random.randint(100, 900))
    gender = str(input('Enter your Gender: M/F '))
    dob = str(input('Enter you DOB in YYYY/MM/DD: '))
    id_code = random.randint(1000, 10000)

    cursor.execute('select * from username')
    x = cursor.fetchall()

    for i in x:
        while id_code == i[1]:
            id_code = random.randint(1000, 10000)

    cursor.execute('insert into username values("{}","{}","{}","{}")'.format(user_name, id_code, gender, dob))
    sql.commit()

    cursor.execute('insert into password values ("{}","{}")'.format(id_code, password))
    sql.commit()


def login():
    # search
    global is_login
    username = input('Enter username: ')
    password = input('Enter password: ')

    cursor.execute('select * from username')
    x = cursor.fetchall()

    for i in x:
        if username == i[0]:
            cursor.execute('select  * from password')
            y = cursor.fetchall()
            for j in y:
                if j[0] == i[1] and password == j[1]:
                    print("Password is correct.")
                    is_login = True

    if is_login == False:
        print('Incorrect Password')

    return is_login


def add_movies():
    # update
    while True:
        s_no = int(input('Enter a S_NO: '))
        mov_name = input('Enter the movie name: ')
        duration = input('Enter the duration: ')
        rating = input('Enter the Rating: ')
        genre = input("Enter a Genre: ")

        cursor.execute(
            "insert into movies values({},'{}','{}','{}','{}')".format(s_no, mov_name, duration, rating, genre))
        sql.commit()

        value = str(input("Do you wish to continue adding:y/n  "))

        if value.lower() == 'y':
            continue
        else:
            break


def del_user():
    # delete
    while True:
        username = input('Enter the username you want to delete: ')

        cursor.execute('select * from username')
        x = cursor.fetchall()

        for i in x:
            if username == i[0]:
                cursor.execute('delete from username where username = "{}"'.format(username))
                sql.commit()
                print('User Deleted')

        value = str(input("Do you wish to continue deleting:y/n  "))

        if value.lower() == 'y':
            continue
        else:
            break


def del_movie():
    while True:
        movie = input('Enter the movie you want to delete: ')

        cursor.execute('select * from movies')
        x = cursor.fetchall()

        for i in x:
            if movie == i[1]:
                cursor.execute('delete from movies where mov_name = "{}"'.format(movie))
                print('Movie Deleted')
                sql.commit()

        value = str(input("Do you wish to continue deleting:y/n  "))

        if value.lower() == 'y':
            continue
        else:
            break


def sort():
    # sort
    choice = str(input('Enter your choice of genre to view movies: '))

    cursor.execute('select count(*) "MOVIE NO." from movies group by genre having genre = "{}"'.format(choice))

    for i in cursor.fetchall():
        print('No = ', i[0])


def show():
    # display
    choice = str(input("Which table do you wish to view: "))

    cursor.execute('select * from {}'.format(choice))
    x = cursor.fetchall()

    for i in x:
        print('-------------------------------------------------')
        for j in i:
            print(j, end='|')
        print('\n')


def create_seats():
    cursor.execute('delete from seats')

    rows = int(input('How many rows are there in the theater?: '))
    column = int(input('How many columns are there?: '))

    ROW = string.ascii_uppercase[:rows]

    COLUMNS = []
    for i in range(1, column + 1):
        COLUMNS.append(i)

    global seats_list
    seats_list = []

    for i in ROW:
        print(i, end=' ')
        for j in COLUMNS:
            print(j, end=' ')

        print('\n')

    for i in ROW:
        for j in COLUMNS:
            seats_list.append('{}{}'.format(i, j))

    for i in seats_list:
        cursor.execute('insert into seats values("{}",null,"{}")'.format(i, i))
        sql.commit()

    global seats_exist
    seats_exist = True
    #
    global ROWS
    ROWS = ROW
    global COLUMN
    COLUMN = COLUMNS


def book_seats(ROWS, COLUMNS):
    for i in ROWS:
        print(i, end=' ')
        for j in COLUMNS:
            print(j, end=' ')
        print('\n')

    while True:
        booked = input('Which Seat you would like to book: ')
        name = input('Enter name of person: ')

        cursor.execute('update seats set customer_name = "{}" where seat_no = "{}" '.format(name, booked))
        sql.commit()

        value = str(input("Do you wish to continue booking:y/n  "))

        if value.lower() == 'y':
            continue
        else:
            break


def display_seats():
    global seats_list
    #   print(seats_list)

    L = seats_list.copy()
    cursor.execute('select * from seats')
    x = cursor.fetchall()

    global COLUMN

    largest = len(COLUMN)

    for i in x:
        if i[1] != None:
            for j in L:
                if i[0] == j:
                    x = j[0] + '*'
                    L[L.index(j)] = x

    #     for i in L:
    #         print(L[i][0])

    output_rows = []
    output_columns = {}
    for i in L:

        if i[0] not in output_rows:
            output_rows.append(i[0])

    x = []

    for j in output_rows:
        for i in range(len(L)):
            if j == L[i][0]:
                # output_columns[output_rows[j]] = [x for x in output_rows if j == i[0]]
                x.append(L[i][1])
        output_columns[j] = x.copy()
        x.clear()

    for i in output_columns:
        print(i, end=' ')
        for j in output_columns[i]:
            print(j, end=' ')

        print('\n')


#     print('whole list = ', L)


def edit_seats():
    cursor.execute('select * from seats')
    x = cursor.fetchall()

    edit_seat = str(input("Enter Seat you would like to edit: "))

    for i in x:
        if edit_seat == i[0] and i[1] != None:
            new_info = str(input('Enter the name for booking the seat: '))

            cursor.execute('update seats set customer_name = "{}" where seat_no = "{}" '.format(new_info, edit_seat))
            sql.commit()


if sql.is_connected:
    print('Successfully Connected..')

    while True:
        print('''


                 1. Register
                 2. Login
                 3. Add Movies
                 4. Create seating arrangement
                 5. Delete Users
                 6. Delete Movies
                 7. Sort Movies by Genre
                 8. Show Tables
                 9. Book Seats
                 10.Display Seats
                 11.Edit seats
                 12. Log Out''')

        ch = int(input())

        if ch == 1:
            register()
        elif ch == 2:
            is_login = login()
        elif ch == 3:
            if is_login == True:
                add_movies()
            else:
                print('Login first.')
        elif ch == 4:
            if is_login == True:
                seats = create_seats()
            else:
                print('Login first.')
        elif ch == 5:
            if is_login == True:
                del_user()
            else:
                print('Login first.')
        elif ch == 6:
            if is_login == True:
                del_movie()
            else:
                print('Login first.')
        elif ch == 7:
            if is_login == True:
                sort()
            else:
                print('Login first.')
        elif ch == 8:
            if is_login == True:
                show()
            else:
                print('Login first.')

        elif ch == 9:
            if is_login == True and seats_exist == True:
                book_seats(ROWS, COLUMN)
            else:
                print('Login first and/or create seating arrangements')
        elif ch == 10:
            if is_login == True and seats_exist == True:
                display_seats()
            else:
                print('Login first and/or create seating arrangements.')

        elif ch == 11:
            if is_login == True and seats_exist == True:
                edit_seats()
            else:
                print('Login first and/or create seating arrangements.')
        elif ch == 12:
            is_login = False
        else:
            print('Invalid')


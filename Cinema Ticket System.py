from time import sleep

                                        #{{{This Function is to Exit the Program}}}
def end_pgm():                               
    print("\n\n\n\t\t\t\t\t\tThankyou for Visiting")
    print("\n\t\t\t\t\t\tClearing all the data....")
    sleep(1)
    print("\n\t\t\t\t\t\tExiting the Program")
    sleep(.75)
    print("\n\t\t\t\t\t\tProgram is exited successfully...\n\n\n")
    exit()



                                        #{{{This Function is to deal with Cash Receiving}}}                                        
def payment(amount):                         
    print("\n\t\t\t\tYour total Bill is: "+str(amount))
    while True:
        try:
            money_mode=int(input("\n\t\t\t\tPress 1 for Easypasia\n\t\t\t\tPress 2 for Account Number\n\t\t\t\tPress 0 to cancel the Tickets\n\t\t\t\tPress -1 to Exit the Program:\n\n\t\t\t\tPress the Number:"))
            if money_mode>=-1 and money_mode<=2:
                break
            else:
                continue
        except:
            print("\n\t\t\t\tAn Invalid Input")
            continue
    if money_mode==1:
        while True:
            try:
                easy_paisa=int(input("\n\t\t\t\tEnter Your Easy Paisa Number (11-Digits) : +92"))
                if easy_paisa>=3000000000 and easy_paisa<=3999999999:
                    print("\n\t\t\t\tCash has been deducted. Thank you")
                    return easy_paisa
                else:
                    print("\n\t\t\t\tPlease Enter your Real Number")
            except ValueError:
                print("\n\t\t\t\tAn Invalid Input\n\t\t\t\tEnter your Real number")
                continue
    elif money_mode==2:
        while True:
            account_number=input("\n\t\t\t\tEnter Your IBAN Number (24-Digits) :")
            if len(account_number)<=24 and len(account_number)>23:
                print("\n\t\t\t\tCash has been deducted. Thank you")
                return account_number
            else:
                print("\n\t\t\t\tPlease Enter your Real IBAN Number(24- Digits)")
            continue
    elif money_mode==0:
        print("\n\t\t\t\t\t\tYour Entered data is clearing wait....")
        sleep(.75)
        return 99
    elif money_mode==-1:
        end_pgm()
                                     #{{{This Function is to Get Info from user }}}
def ticket_book(movie_detail_array,data,token,time,seats,price):
    name=input("\n\t\t\t\tEnter your name: ")
    while True:
                try:
                    phone=int(input("\n\t\t\t\tEnter Your Phone Number (11-Digits) : +92"))
                    if phone>=3000000000 and phone<=3999999999:
                        break
                    else:
                        print("\n\t\t\t\tPlease Enter your Real Number")
                except ValueError:
                    print("\n\t\t\t\tAn Invalid Input\n\t\t\t\tEnter your Real number\n\t\t\t\tIf you want to exit first Enter Details then press 0 before Paying")
                    continue
    print("\n\n\t\t\t\t\t[Food pack=Pop-Corn+Cold Drink(300)]\n\n")
    while True:
        try:
            food=int(input("\n\t\t\t\tEnter Numbers of Food-Packs: "))
            if food <=seats and food>=0:
                break
            else:
                print("\n\t\t\t\tSorry You have Entered an Invalid Input\n \t\t\t\tYou Can't buy food-packs more than seats\n")
                continue
        except ValueError:
            print("\n\t\t\t\tSorry You have Entered an Invalid Input\n\t\t\t\tTo cancel ticket, First enter Fodd packs then press 0 in next steps")
            continue
    food_price=food*300
    total_bill=food_price+price
    decision=payment(total_bill)
    if decision==99:
        print('''
                                                Redirecting to Main Menu...
            
            ''')
        sleep(.77)
        return -2
    movie_detail_array.append([])
    movie_detail_array[data].append(token)
    movie_detail_array[data].append(name)
    movie_detail_array[data].append(phone)
    movie_detail_array[data].append(time)
    movie_detail_array[data].append(seats)
    movie_detail_array[data].append(price)
    movie_detail_array[data].append(food_price)
    movie_detail_array[data].append(decision)
    print("\n\t\t\t\t\t\tPlease wait...")
    sleep(1)
    print("\n\n\t\t\t\tYour Seats are confirmed\n\t\t\t\tID: "+str(token)+" (REMEMBER)"+"\n\t\t\t\tName: "+name+"\n\t\t\t\tNum of Seats: "+str(seats)+"\n\t\t\t\tFood-Packs: "+str(food)+"\n\t\t\t\tTotal Bill: "+str(food_price+price))
    press=input("\n\n\n\t\t\t\tPress Enter for Main Menu: ")

                                #{{{This Function is to Display the movies that are displaying today}}}
def display():
    print('''
                                                        4D Cinema

                                                     Displaying Today

                                Movie Title             Display Time            Duration
                                --------------------------------------------------------
                                1:Maula Jatt              12:00 pm                 2:45
                                2:AVATAR                  05:00 pm                 2:30
                                3:ABC                     09:00 pm                 2:00

                                                PRESS  ANY KEY FOR MAIN MENU
                                                PRESS (-1) to EXIT the PROGRAM 


        ''')
    random=input("\t\t\t\t")
    if random=='-1':
        end_pgm()

                                    #{{{This Function is to search the Ticket}}}
def search(num,x):
    print("\n\t\t\t\t\t\t\tCHECKING.....\n")
    sleep(1.5)
    flag=0
    for i in range(0,len(x)):
        if num in x[i]:
            flag=1
            # print("\n\t\t\t\t\t\t\tRecord is found:)\n\t\t\t\t\tID: "+ str(num) + "\n\t\t\t\t\tName :"+x[i][1]+"\n\t\t\t\t\tPhone No: "+str(x[i][2])+"\n\t\t\t\t\tStart Time: "+x[i][3]+"\n\t\t\t\t\tSeats: "+str(x[i][4])+"\n\t\t\t\t\tTicket Price: "+str(x[i][5])+"\n\t\t\t\t\tFood Price: "+str(x[i][6])+"\n\t\t\t\t\tTotal Bill: "+str(x[i][5]+x[i][6]))
            print("\n\t\t\t\t\t\t\tRecord is found:)\n")
            sleep(.5)
            print("\t\t\t\t\tID: "+ str(num))
            sleep(.25)
            print("\t\t\t\t\tName :"+x[i][1])
            sleep(.25)
            print("\t\t\t\t\tPhone No: "+str(x[i][2]))
            sleep(.25)
            print("\t\t\t\t\tStart Time: "+x[i][3])
            sleep(.25)
            print("\t\t\t\t\tSeats: "+str(x[i][4]))
            sleep(.25)
            print("\t\t\t\t\tTicket Price: "+str(x[i][5]))
            sleep(.25)
            print("\t\t\t\t\tFood Price: "+str(x[i][6]))
            sleep(.25)
            print("\t\t\t\t\tTotal Bill: "+str(x[i][5]+x[i][6]))
    if flag==0:
        print("\t\t\t\tSorry Record is Not found\n")
    
    press=input("\n\t\t\t\tPress Enter for Main Menu ")

                                         #{{{This Function is to Delete the Ticket}}}

def remover(num3,y):
    flag=0
    for i in range(0,len(y)):
        if num3 in y[i]:
            flag=1
            break

    if flag==1:
        print("\n\t\t\t\t\t\t\tRecord is found:)\n\t\t\t\t\tID: "+ str(num3) + "\n\t\t\t\t\tName :"+y[i][1]+"\n\t\t\t\t\tPhone No: "+str(y[i][2])+"\n\t\t\t\t\tStart Time: "+y[i][3]+"\n\t\t\t\t\tSeats: "+str(y[i][4])+"\n\t\t\t\t\tTicket Price: "+str(y[i][5])+"\n\t\t\t\t\tFood Price: "+str(y[i][6])+"\n\t\t\t\t\tTotal Bill: "+str(y[i][5]+y[i][6]))
        vacancy=y[i][4]
        print("\n\n\t\t\t\tDeleteing the Record....")
        sleep(1.25)
        del y[i]
        print("\n\t\t\t\t\t\tRedirecting to Main Menu")
        sleep(1)
        return vacancy
    else:
        print("\n\t\t\t\tOops, There's no such record registered with this ID.")
    print("\n\t\t\t\t\t\tRedirecting to Main Menu")
    sleep(.75)
    return 0

                                                #{{{From Here Program starts}}}


print("\n\n\t\t\t\t\t\t\t\tWelcome to 4D Cinema\n\n")
print("\t\t\t\t\t\tGenearl Note: FOR ALL COMANDS, ONLY PRESS RELATED GIVEN NUMBER\n")

movie_1_details=[]              #list for first Movie
movie_2_details=[]              #list for second Movie
movie_3_details=[]              #list for third Movie

data_1=0                        #deal with the index of 1st list
data_2=0                        #deal with the index of 2nd list
data_3=0                        #deal with the index of 3rd list

s1=20                           #seat capacity for first Movie
s2=20                           #seat capacity for 2nd Movie
s3=20                           #seat capacity for 3rd Movie

empty_seats_1=0                 #deal with seats when user of 1st movie cncel his ticket within the way
empty_seats_2=0                 #deal with seats when user of 2nd movie cncel his ticket within the way
empty_seats_3=0                 #deal with seats when user of 3rd movie cncel his ticket within the way

id_1=1001                       #deal with the ID of first Movie
id_2=2001                       #deal with the ID of 2nd Movie
id_3=3001                       #deal with the ID of 3rd Movie
while True:
    print('''                              
                                        --------MAIN MENU------

                                1:Display Movies
                                2:Book your Ticket
                                3:Search your Ticket
                                4:Delete your Ticket
                                5:Exit
                                ''')
    while True:
        try:
            direct=int(input("\t\t\t\tPress the num: "))
            sleep(.25)
            if direct <=5 and direct >=1:
                break
            else:
                print("\n\t\t\t\tSorry You have Entered an Invalid Input\n \t\t\t\tPlease Enter between (1-5)\n")
                print('''                              
                                        --------MAIN MENU------

                                1:Display Movies
                                2:Book your Ticket
                                3:Search your Ticket
                                4:Delete your Ticket
                                5:Exit
                                ''')
                continue
        except ValueError:
            sleep(.25)
            print("\n\t\t\t\tSorry You have Entered an Invalid Input\n \t\t\t\tPlease Enter between (1-5)\n")
            print('''                              
                                        --------MAIN MENU------

                                1:Display Movies
                                2:Book your Ticket
                                3:Search your Ticket
                                4:Delete your Ticket
                                5:Exit
                                ''')
            continue
    if direct==1:
        display()
        continue
    if direct==2:
        print("\n\n\t\t\t\t\t\t\t\t4D Cinema\n\t\t\t\t\t\t\t\t~~~~~~~~~\n\t\t\t\t\t\t\t\tDisplaying Today\n\n\t\t\t\tMovie Title\t\tDisplay Time\t\tDuration\tAvailable Seats")
        print('\t\t\t\t-------------------------------------------------------------------------------')
        print("\t\t\t\t1:Maula Jatt\t\t 12:00 pm\t\t 2:45\t\t\t"+str(s1))
        print("\t\t\t\t2:Avatar\t\t 05:00 pm\t\t 2:30\t\t\t"+str(s2))
        print("\t\t\t\t3:ABC\t\t\t 09:00 pm\t\t 2:00\t\t\t"+str(s3))
        print('''                       
                                                    Press 0 for Main Menu
                                                Press (-1) to Exit the Program
                                        ''')
        
        while True:
            try:
                movie=int(input("\t\t\t\tSelect the movie: "))
                if movie <=3 and movie >=-1:
                    break
                else:
                    print("\n\t\t\t\tSorry You have Entered an Invalid Input\n \t\t\t\tPlease Enter between (1-3)for Movies\n")
                    sleep(.75)
                    print("\n\n\t\t\t\t\t\t\t\t4D Cinema\n\t\t\t\t\t\t\t\t~~~~~~~~~\n\t\t\t\t\t\t\t\tDisplaying Today\n\n\t\t\t\tMovie Title\t\tDisplay Time\t\tDuration\tAvailable Seats")
                print('\t\t\t\t-------------------------------------------------------------------------------')
                print("\t\t\t\t1:Maula Jatt\t\t 12:00 pm\t\t 2:45\t\t\t"+str(s1))
                print("\t\t\t\t2:Avatar\t\t 05:00 pm\t\t 2:30\t\t\t"+str(s2))
                print("\t\t\t\t3:ABC\t\t\t 09:00 pm\t\t 2:00\t\t\t"+str(s3))
                print('''                       
                                                            Press 0 for Main Menu
                                                        Press (-1) to Exit the Program
                                                ''')
                continue
            except ValueError:
                print("\n\t\t\t\tSorry You have Entered an Invalid Input\n \t\t\t\tPlease Enter between (1-3) for movies\n")
                sleep(.75)
                print("\n\n\t\t\t\t\t\t\t\t4D Cinema\n\t\t\t\t\t\t\t\t~~~~~~~~~\n\t\t\t\t\t\t\t\tDisplaying Today\n\n\t\t\t\tMovie Title\t\tDisplay Time\t\tDuration\tAvailable Seats")
                print('\t\t\t\t-------------------------------------------------------------------------------')
                print("\t\t\t\t1:Maula Jatt\t\t 12:00 pm\t\t 2:45\t\t\t"+str(s1))
                print("\t\t\t\t2:Avatar\t\t 05:00 pm\t\t 2:30\t\t\t"+str(s2))
                print("\t\t\t\t3:ABC\t\t\t 09:00 pm\t\t 2:00\t\t\t"+str(s3))
                print('''                       
                                                            Press 0 for Main Menu
                                                        Press (-1) to Exit the Program
                                                ''')
                continue
        
        if movie==1:
            if s1>0:
                while True:
                    try:
                        morning_seats=int(input("\t\t\t\tEnter the Number of seats (Press 0 to cancel the Tickets and (-1) to Exit): "))
                        if morning_seats <=15 and morning_seats >=1:
                            s1=s1-morning_seats
                            if s1<0:
                                s1=s1+morning_seats
                                print("\n\t\t\t\t\tThe only remaining Capacity is "+str(s1)+" seats\n")
                                continue
                            break
                        elif morning_seats==0:
                            print('''
                                                Redirecting to Main Menu...
                                                 ''')
                            sleep(.75)
                            break
                        elif morning_seats==-1:
                            end_pgm()
                        else:
                            print("\n\t\t\t\tSorry you can only book 15 seats once\n \t\t\t\tPlease Enter between (1-15)\n")
                            continue
                    except ValueError:
                        print("\n\t\t\t\tSorry You have Entered an Invalid Input\n \t\t\t\tPlease Enter between (1-15)\n")
                        continue
            else:
                print("\n\t\t\t\tSorry to tell you that Seat capacity is full\n\t\t\t\tYou can chose another movie")
                continue
            if morning_seats!=0:
                price=morning_seats*800
                time='12:00 pm'
                check_1=ticket_book(movie_1_details,data_1,id_1,time,morning_seats,price)
                if check_1==-2:
                    empty_seats_1=morning_seats
                    s1=s1+empty_seats_1
                    data_1=data_1-1
                data_1=data_1+1
                id_1=id_1+1
                continue
        elif movie==2:
            if s2>0:
                while True:
                    try:
                        evening_seats=int(input("\t\t\t\tEnter the Number of seats. (Press 0 to cancel the Tickets and (-1) to Exit): "))
                        if evening_seats <=15 and evening_seats >=1:
                            s2=s2-evening_seats
                            if s2<0:
                                s2=s2+evening_seats
                                print("\n\t\t\t\t\tThe only remaining Capacity is "+str(s2)+" seats\n")
                                continue
                            break
                        elif evening_seats==0:
                            print('''
                                                Redirecting to Main Menu...
                                                 ''')
                            sleep(.75)
                            break
                        elif evening_seats==-1:
                            end_pgm()
                        else:
                            print("\n\t\t\t\tSorry you can only book 15 seats once\n \t\t\t\tPlease Enter between (1-15)\n")
                        continue
                    except ValueError:
                        print("\n\t\t\t\tSorry You have Entered an Invalid Input\n \t\t\t\tPlease Enter between (1-15)\n")
                        continue
            else:
                print("\n\t\t\t\tSoory to tell you that Seat capacity is full\n\t\t\t\tYou can chose another movie")
                continue
            if evening_seats!=0:
                price=evening_seats*800
                time='05:00 pm'
                check_2=ticket_book(movie_2_details,data_2,id_2,time,evening_seats,price)
                if check_2==-2:
                    empty_seats_2=evening_seats
                    s2=s2+empty_seats_2
                    data_2=data_2-1
                data_2=data_2+1
                id_2=id_2+1
                continue
        elif movie==3:
            if s3>0:
                while True:
                    try:
                        night_seats=int(input("\t\t\t\tEnter the Number of seats (Press 0 to cancel the Tickets and (-1) to Exit): "))
                        if night_seats <=15 and night_seats >=1:
                            s3=s3-night_seats
                            if s3<0:
                                s3=s3+night_seats
                                print("\n\t\t\t\t\tThe only remaining Capacity is "+str(s3)+" seats\n")
                                continue
                            break
                        elif night_seats==0:
                            print('''
                                                Redirecting to Main Menu...
                                                 ''')
                            sleep(.75)
                            break
                        elif night_seats==-1:
                            end_pgm()
                        else:
                            print("\n\t\t\t\tSorry you can only book 15 seats once\n \t\t\t\tPlease Enter between (1-15)\n")
                        continue
                    except ValueError:
                        print("\n\t\t\t\tSorry You have Entered an Invalid Input\n \t\t\t\tPlease Enter between (1-15)\n")
                        continue
            else:
                print("\n\t\t\t\tSoory to tell you that Seat capacity is full\n\t\t\t\tYou can chose another movie")
                continue
            if night_seats!=0:
                price=night_seats*800
                time='09:00 pm'
                check_3=ticket_book(movie_3_details,data_3,id_3,time,night_seats,price)
                if check_3==-2:
                    empty_seats_3=night_seats
                    s3=s3+empty_seats_3
                    data_3=data_3-1
                data_3=data_3+1
                id_3=id_3+1
                continue
        elif movie==0:
            print('''
                                                Redirecting to Main Menu...
            
            ''')
            sleep(0.75)
            continue
        elif movie==-1:
            end_pgm()
    elif direct==3:
        while True:
            try:
                token=int(input("\n\t\t\t\tEnter the ID (Press 0 for Main Menu and (-1) to Exit the Program): "))
                if token <=3150 and token >=1001 or token==-1 or token==0:
                    break
                else:
                    print("\n\t\t\t\tPlease Enter a valid input\n")
                continue
            except ValueError:
                print("\n\t\t\t\tSorry You have Entered an Invalid Input\n \t\t\t\tPlease try Again\n")
            continue
        if token>=1001 and token <=1150:
            search(token,movie_1_details)
        elif token>=2001 and token <2150:
            search(token,movie_2_details)
        elif token>=3001 and token<=3150:
            search(token,movie_3_details)
        elif token==0:
            print('''
                                                Redirecting to Main Menu...
            
            ''')
            sleep(.75)
        elif token==-1:
            end_pgm()
    elif direct==4:
        while True:
            try:
                token=int(input("\n\t\t\t\tEnter the ID (Press 0 for Main Menu and (-1) to Exit the Program):  "))
                if token <=3150 and token >=1001 or token==0 or token==-1:
                    break
                else:
                    print("\n\t\t\t\tPlease Enter a valid input\n")
                continue
            except ValueError:
                print("\n\t\t\t\tSorry You have Entered an Invalid Input\n \t\t\t\tPlease try Again\n")
            continue
        if token>=1001 and token <=1150:
            deleted_seats_1=remover(token,movie_1_details)
            s1=s1+deleted_seats_1
        elif token>=2001 and token <2150:
            deleted_seats_2=remover(token,movie_2_details)
            s2=s2+deleted_seats_2
        elif token>=3001 and token<=3150:
            deleted_seats_3=remover(token,movie_3_details)
            s3=s3+deleted_seats_3
        elif token==0:
            print('''
                                                Redirecting to Main Menu...
            
            ''')
            sleep(.75)
        elif token==-1:
            end_pgm()
    elif direct==5:
        end_pgm()
import sqlite3, datetime, random
import sys
connection=sqlite3.connect("bus.db")
cursor=connection.cursor()

cursor.execute("""select count(name) from sqlite_master where type='table' and name='admin'""")
if cursor.fetchone()[0]!=1:
    cursor.execute("""CREATE TABLE admin( 
    user_name VARCHAR2(30) primary key, 
    password VARCHAR2(20) not null);""")
    cursor.execute("""CREATE TABLE bus_line( 
    bus_id number primary key,
    bus_name VARCHAR2(30) not null);""")
    cursor.execute("""CREATE TABLE ticket_status( 
    tcode number primary key,
    status VARCHAR2(30));""")
    cursor.execute("""CREATE TABLE traveller( 
    traveller_id number,
    tname VARCHAR2(60),
    tage number,
    temail VARCHAR2(30),
    tphone number,
    nopasg number,
    departure VARCHAR2(30),
    arrival VARCHAR2(30),
    seatn number,
    meal VARCHAR(30),
    baggage VARCHAR2(30),
    typej VARCHAR2(50));""")
    cursor.execute("""CREATE TABLE payment( 
    seat_number number,
    meal VARCHAR2(30),
    baggage VARCHAR2(30),
    tcode number,
    traveller_id number);""")
    cursor.execute("""CREATE TABLE ticket(
    ticketcode number primary key,
    net_price number,
    price number);""")
    cursor.execute("""CREATE TABLE one_way_booking( 
    no_of_pas1 number,
    pay_in1 number,
    dep_from1 VARCHAR2(30),
    dep_date1 date,
    destination1 VARCHAR2(30));""")
    cursor.execute("""CREATE TABLE two_way_booking( 
    no_of_pas2 number,
    pay_in2 number,
    dep_from2 VARCHAR2(30),
    dep_date2 date,
    ret_date date,
    destination2 VARCHAR2(30));""")
    cursor.execute("""CREATE TABLE customer(
    username VARCHAR2(30) primary key,
    pass VARCHAR2(30) not null,
    email VARCHAR2(30),
    age number not null,
    first_n VARCHAR2(30),
    second_n VARCHAR2(30),
    phone number);""")
    cursor.execute("""insert into bus_line values(100,'Pratik Travels-1')""")
    cursor.execute("""insert into bus_line values(101,'Pratik Travels-2')""")
    cursor.execute("""insert into bus_line values(102,'Pratik Travels-3')""")
    cursor.execute("""insert into bus_line values(103,'Pratik Travels-4')""")
    cursor.execute("""insert into bus_line values(104,'Rose Travels-1')""")
    cursor.execute("""insert into bus_line values(105,'Rose Travels-2')""")
    cursor.execute("""insert into bus_line values(106,'Rose Travels-3')""")
    cursor.execute("""insert into bus_line values(107,'Rose Travels-4')""")
    cursor.execute("""insert into bus_line values(108,'Rani Travels-1')""")
    cursor.execute("""insert into bus_line values(109,'Rani Travels-2')""")
    cursor.execute("""insert into bus_line values(110,'Rani Travels-3')""")
    cursor.execute("""insert into bus_line values(111,'Rani Travels-4')""")
    cursor.execute("""insert into one_way_booking (no_of_pas1) VALUES (0)""")
    cursor.execute("""insert into two_way_booking (no_of_pas2) VALUES (0)""")
    
    
    print("Database successfully created !")
    
    
else:
    
    
    def mainMenu():
        cursor.execute("""select count(*) from traveller;""")
        x=cursor.fetchall()                                                
        y=(1000+x[0][0])
        trav_id=y
        print(trav_id)
        print("1. Administration\n")
        print("2. Customer\n")
        print("3. Traveller\n")
        print("4. Quit\n")
        
        while True:
            selection=int(input())
            
            if selection==1:
                error2=1
                while error2==1:
                    e=int(input("Press 1 if you are an exiting admin.\nPress 2 if you are a new admin."))
                    if e==2:
                        u_id=input('Enter user name - ')
                        pas=input('Enter password - ')
                        cursor.execute("""insert into admin values(?,?)""",(u_id,pas))
                    elif e==1:
                        i=input("\nEnter your User ID - ")
                        p=input("Enter your Password - ")
                        cursor.execute("""select count(user_name) from admin where user_name=?""",(i,))
                        if cursor.fetchone()[0]==1:
                            cursor.execute("""select count(password) from admin where password=?""",(p,))
                            if cursor.fetchone()[0]==1:
                                print("Sign in successfull!\n")
                                connection.commit()

                                error2=0                              
                                def adminMenu():
                                    print("1. Traveller Details\n")
                                    print("2. Ticket Status\n")
                                    print("3. Bus Details\n")
                                    while True:
                                        access=int(input())
                                        if access==1:
                                            trav=int(input("Enter Traveller ID - "))
                                            print("Traveller Details - ")
                                            cursor.execute("""select * from traveller where traveller_id=(?)""",(trav,))
                                            for row in cursor.fetchall():
                                                print("Traveller ID: ",row[0])
                                                print("Booked by: ",row[1])
                                                print("Age: ",row[2])
                                                print("E-mail: ",row[3])
                                                print("Phone: ",row[4])
                                                print("Passengers :",row[5])
                                                print("From: ",row[6])
                                                print("To: ",row[7])
                                                print("Seat No:",row[8])
                                                print("Meal:",row[9])
                                                print("Baggage:",row[10])
                                                print("Type: ",row[11])
                                                print("\n")
                                            
                                                cont=input("Do you want to continue ? (yes/no)")
                                                if cont=='yes':
                                                    adminMenu()
                                                else:
                                                    print("Thank you for letting us serve you. Have a nice day ahead!\n")
                                                    mainMenu()
                                            
                                        
                                        elif access==2:
                                            tic=input("Enter Ticket Code - ")
                                            print("Ticket Details - ")
                                            cursor.execute("""select * from ticket_status where tcode=(?)""",(tic,))
                                            for row in cursor.fetchall():
                                                print("Ticket Code: ",row[0])
                                                print("Status: ",row[1])
                                                print("\n")
                                            cont=input("Do you want to continue ? (yes/no)")
                                            if cont=='yes':
                                                adminMenu()
                                            else:
                                                print("Thank you for letting us serve you. Have a nice day ahead!")
                                                
                                            break    
                                        elif access==3:
                                            bus=input("Enter Bus ID - ")
                                            print("Bus Details - ")
                                            cursor.execute("""select * from bus_line where bus_id=(?)""",(bus,))
                                            for row in cursor.fetchall():
                                                print("Bus ID: ",row[0])
                                                print("Bus Name: ",row[1])
                                                print("\n")
                                            cont=input("Do you want to continue ? (yes/no)")
                                            if cont=='yes':
                                                adminMenu()
                                            else:
                                                print("Thank you for letting us serve you. Happy a nice day ahead!")
                                                sys.exit(0)
                                        else:
                                            print("Invalid choice. Enter 1-4")
                                            adminMenu()
                                        break
                                adminMenu()
                            else:
                                print("Incorrect passoword. Please retry! ")
                        else:
                            print("Incorrect User ID. Please retry! ")
                
            elif selection==2:
                    error1=1
                    k=1
                    while k!=0 and error1==1:
                        k=int(input("1. Existing Customer.\n2. New Customer.\n3. Quit\n"))
                        if k==2:
                            c_id=input('Enter username - ')
                            c_pas=input('Enter password - ')
                            c_em=input('Enter e-mail id - ')
                            c_age=int(input('Enter age - '))
                            c_fn=input('Enter your first name - ')
                            c_ln=input('Enter your last name - ')
                            c_phn=int(input('Enter your phone number - '))
                            cursor.execute("""insert into customer values(?,?,?,?,?,?,?)""",(c_id,c_pas,c_em,c_age,c_fn,c_ln,c_phn,))
                            connection.commit()
                            
                        elif k==1:
                            c_id=input('Enter username - ')
                            c_pas=input('Enter password - ')
                            cursor.execute("""select count(username) from customer where username=(?)""",(c_id,))
                            if cursor.fetchone()[0]==1:
                                cursor.execute("""select count(pass) from customer where pass=(?)""",(c_pas,))
                                if cursor.fetchone()[0]==1:
                                    print("Sign in successfull!\n")
                                    error1=0
                                    
                                    def custMenu():
                                        print("1. One way trip")
                                        print("2. Round trip")
                                        print("3. Exit\n")

                                        yes=0
                                        while True:
                                            access1=int(input())
                                            if access1==1:
                                                typej='One Way'
                                                cursor.execute("""select count(*) from traveller;""")
                                                x=cursor.fetchall()                                                
                                                y=(1000+x[0][0])
                                                trav_id=y
                                                print(y)
                                                connection.commit()
                                                cursor.execute("""SELECT SUM(no_of_pas1)FROM one_way_booking""")
                                                totalnp=cursor.fetchall()
                                                nop=int(input("Enter total no. of passengers - "))
                                                totalnp=nop+totalnp[0][0]
                                                price=random.choice([500,600,700,800,900,1000])
                                                pay=input("Cash/UPI/pay later - ")          
                                                dep=input("Departure from - ")
                                                date=input('Enter date of departure(yyyy-mm-dd) - ')
                                                dest=input("Enter Destination - ")
                                                meal=input("Enter meal selection(Veg/Non veg/Special) - ")
                                                if meal.lower()=='veg':
                                                    pric=200
                                                elif meal.lower()=='non veg':
                                                    pric=300
                                                elif meal.lower()=='special':
                                                    pric=400
                                                total_price=price+pric
                                                bag=input("Enter baggage capacity(small/medium/large) - ")
                                                cursor.execute("""insert into one_way_booking values(?,?,?,?,?)""",(nop,pay,dep,date,dest))
                                                print("Ticket booking successful!\n")

                                                cursor.execute("""insert into payment(seat_number,meal,baggage,tcode,traveller_id) values(?,?,?,?,?)""",(totalnp,meal,bag,y,trav_id))
                                                cursor.execute("""insert into ticket values(?,?,?)""",(y,total_price,price))
                                                print("Ticket code is : ",y)
                                                print("Traveller id is: ",trav_id)                                                    
                                                
                                                if pay.lower()=='pay later':
                                                    cursor.execute("""insert into ticket_status values(?,?)""",(y,'Not Confirmed'))
                                                elif pay.lower()=='cash' or pay.lower()=='upi':
                                                    cursor.execute("""insert into ticket_status values(?,?)""",(y,'Confirmed'))
                                                    cursor.execute("""select * from customer where username=(?)""",(c_id,))
                                                    for row in cursor.fetchall():                                                        
                                                        ta=row[1]
                                                        te=row[2]
                                                        tfn=row[4]                                                  
                                                        tp=row[6]
                                                        
                                                    i=0+yes

                                                    print(y,tfn,ta,te,tp,dep,dest,totalnp,meal,bag,'One way')
                                                    cursor.execute("""insert into traveller(traveller_id,tname,tage,temail,tphone,nopasg,departure,arrival,seatn,meal,baggage,typej) values (?,?,?,?,?,?,?,?,?,?,?,?)""",(y,tfn,ta,te,tp,nop,dep,dest,totalnp,meal,bag,typej))
                                                    connection.commit()

                                                connection.commit()

                                                cont=input("Do you want to book more tickets ? (yes/no)")
                                                if cont=='yes':
                                                    yes=yes+1
                                                    custMenu()
                                                else:
                                                    print("Thank you for letting us serve you. Happy journey!")
                                                    break
                                                    break
                                                
                                            elif access1==2:
                                                cursor.execute("""select count(*) from traveller;""")
                                                x=cursor.fetchall()                                                
                                                y=(1000+x[0][0])
                                                trav_id=y
                                                print(y)
                                                cursor.execute("""SELECT SUM(no_of_pas2)FROM two_way_booking""")
                                                totalnp=cursor.fetchall()
                                                nop=int(input("Enter total no. of passengers - "))
                                                totalnp=nop+totalnp[0][0]
                                                price=random.choice([900,1200,1500,1800,2000,2500])
                                                pay=input("Cash/UPI/pay later - ")
                                                dep=input("Departure from - ")
                                                date1=input('Enter date of departure(yyyy-mm-dd) - ')
                                                date2=input('Enter date of arrival(yyyy-mm-dd) - ')
                                                dest=input("Enter Destination - ")
                                                meal=input("Enter meal selection(Veg/Non veg/Special) - ")
                                                if meal.lower()=='veg':
                                                    pric=200
                                                elif meal.lower()=='non veg':
                                                    pric=300
                                                elif meal.lower()=='special':
                                                    pric=400
                                                total_price=price+pric
                                                bag=input("Enter baggage capacity(small/medium/large) - ")
                                                cursor.execute("""insert into two_way_booking values(?,?,?,?,?,?)""",(nop,pay,dep,date1,date2,dest))
                                                print("Ticket booking successful!\n")

                                                cursor.execute("""insert into payment(seat_number,meal,baggage,tcode,traveller_id) values(?,?,?,?,?)""",(totalnp,meal,bag,y,trav_id))
                                                cursor.execute("""insert into ticket values(?,?,?)""",(y,total_price,price))
                                                print("Ticket code is : ",y)
                                                print("Traveller id is: ",trav_id)
                                                    
                                                if pay.lower()=='pay later':
                                                    cursor.execute("""insert into ticket_status values(?,?)""",(y,'Not Confirmed'))
                                                elif pay.lower()=='cash' or pay.lower()=='upi':
                                                    cursor.execute("""insert into ticket_status values(?,?)""",(y,'Confirmed'))
                                                    cursor.execute("""select * from customer where username=(?)""",(c_id,))
                                                    for row in cursor.fetchall():                                                        
                                                        ta=row[1]
                                                        te=row[2]
                                                        tfn=row[4]                                                  
                                                        tp=row[6]
                                                        
                                                    i=0+yes

                                                    print(y,tfn,ta,te,tp,dep,dest,totalnp,meal,bag,'One way')
                                                    cursor.execute("""insert into traveller(traveller_id,tname,tage,temail,tphone,nopasg,departure,arrival,seatn,meal,baggage,typej) values (?,?,?,?,?,?,?,?,?,?,?,?)""",(y,tfn,ta,te,tp,nop,dep,dest,totalnp,meal,bag,typej))
                                                    connection.commit()
                                                        
                                                connection.commit()
                                                cont=input("Do you want to book more tickets ? (yes/no)")
                                                if cont=='yes':
                                                    custMenu()
                                                else:
                                                    print("Thank you for letting us serve you. Happy journey!")
                                                    break
                                                    break

                                            elif access1==3:
                                                break
                                                
                                            else:
                                                print("Invalid choice. Enter 1, 2 or 3")
                                                custMenu()         
                                    custMenu()                                        
                                else:
                                    print("Incorrect passoword. Please retry! ")
                            else:
                                print("Incorrect User ID. Please retry! ")
                    break                              
            
            elif selection==3:
                t_id=input('Enter traveller id - ')
                print("Traveller Details: ")
                cursor.execute("""select * from traveller where traveller_id=(?)""",(t_id,))
                for row in cursor.fetchall():
                    print("Traveller ID: ",row[0])
                    print("Booked by: ",row[1])
                    print("Age: ",row[2])
                    print("E-mail: ",row[3])
                    print("Phone: ",row[4])
                    print("From: ",row[5])
                    print("To: ",row[6])
                    print("Seat No:",row[7])
                    print("Meal:",row[8])
                    print("Baggage:",row[9])
                    print("Type: ",row[10])
                    print("\n")                                        
                print("Ticket Details - ")
                cursor.execute("""select * from ticket_status where tcode=(?)""",(t_id,))
                for row in cursor.fetchall():
                    print("Ticket Code: ",row[0])
                    print("Status: ",row[1])
                    print("\n")
                cursor.execute("""select seat_number,meal,baggage from payment where tcode=(?)""",(t_id,))
                for row in cursor.fetchall():
                    print("Seat number: ",row[0])
                    print("Meal: ",row[1])
                    print("Baggage: ",row[2])
                    cursor.execute("""select net_price,price from ticket where ticketcode=(?)""",(t_id,))
                
                cont=input("Do you want to continue ? (yes/no)")
                if cont=='yes':
                    mainMenu()
                else:
                    print("Thank you for letting us serve you. Have a nice day ahead!\n")
                    break

            elif selection==4:
                sys.exit()
                                        
            else:
                print("Invalid choice. Enter 1-4")
                exit
                mainMenu()
                break
    mainMenu()


    connection.commit()

connection.commit()
connection.close()

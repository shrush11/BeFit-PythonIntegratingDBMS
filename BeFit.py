from tkinter import *
from PIL import Image
from tabulate import tabulate
import math
import matplotlib.pyplot as grp
import time
import csv as csv
import webbrowser
global lst2
global d
print("WELCOME TO BeFiT!!")
print("BeFit IS A PROGRAM THAT ENABLES ITS USERS TO KEEP A TRACK ON THEIR HEALTH AND FITNESS")
print("WITH OUR VERY OWN SCHEDULED WORKOUTS WE FOCUS ON IMPROVING HEALTH OF INDIVIDUALS THROUGH THIS CODE")
print("BeFit FILTERS A LOT OF OPTIONS FOR THE USER TO MAKE THE CODE USER-FRIENDLY AND HENCE ACCESS THEIR BEST WORKOUT PLANS")
print("SO WHAT ARE WE WAITING FOR!!")
print("LETS GET STARTED")
print("PLEASE FILL OUT THE FOLLOWING OPTIONS TO CREATE YOUR PROFILE")
gui = Tk(className='Python Examples - Button')
gui.geometry("250x80")
# create button
button = Button(gui, text='START', width=40, height=5, bg="blue", fg="white")
# add button to gui window
button.pack()
gui.mainloop()
img=Image.open("logo.jpg")
img.show()


flst=[]
# Input user information 
name=input("Enter the name :")
name.capitalize()
flst.append(name)
address=input("Enter the address:")
flst.append(address)
phone=int(input("Enter the phoneno:"))
count=0
phoneno=phone
while phone>0:
    count+=1
    phone//=10
if count!=10:
        print("invalid input")
        phoneno=int(input("Enter the phoneno:"))
else:
        pass
flst.append(phoneno)
emailid=input("Enter the Email Id:")
flst.append(emailid)
date=input("Enter the Date Of Birth:")
flst.append(date)
age=int(input("Enter the age between 15-60:"))
if  age<=15 or age>=60:
    print("INVALID AGE ENTER AGAIN")
    age=int(input("Enter the age between 15-60:"))
else:
    pass
flst.append(age)
gender=input("Enter the gender:")
flst.append(gender)
height=float(input("Enter the height(in cm):"))
flst.append(height)
weight=float(input("Enter the weight(in kg):"))
flst.append(weight)

# bmi calculation 
bmi=(weight/(height*height))*10000
flst.append(bmi)
print("The Body Mass Index is:",bmi)

#calorie calculation
bmrm=66.47+(13.75*weight)+(5.003*height)-(6.755*age)
bmrf=65.51+(9.563*weight)+(1.850*height)-(4.676*age)
if gender.lower()=="male":
    calorie=bmrm*1.375
else:
    calorie=bmrf*1.375
flst.append(calorie)
print("The calorie is",calorie)

# Storing the user details in the form of a dictionary
flst1=["Name","Address","Phone no","Email","DIB","Age","Gender","Weight","Height","Bmi","Calorie Count"]
finald={}
c=0
for p in flst:
    Str=flst[c]
    w=flst1[c]
    print(w,Str)
    finald[w]=Str
    c+=1

#Python-mysql interface
import mysql.connector as con 
mycon=con.connect(host="localhost",user="root",password="shrushti",database="UserInfo1")
if mycon.is_connected()==True:
    print("succesfully connected")
    print(mycon)
else:
    print("not connected")
mycursor=mycon.cursor()
mycon.commit()

#Fitness test
print("THIS IS THE STAGE 1")
print("BEFORE GIVING YOU WORKOUTS , WE NEED TO KEEP A BASIC HEALTH CHECK OF YOUR CURRENT FITNESS")
print("TO DO SO , YOU NEED TO GIVE A BASIC FITNESS TEST THAT BeFit WILL BE PROVDING YOU SHORTLY")
lst1=[("1","Shuttle Run(in min)","15"),
        ("2","Lunges","20"),
        ("3","Crunches","20"),
        ("4","Squats","20"),
        ("5","Plank(in secs)","40",)]
header=["SrNo.","Exercises","no of times"]
print(tabulate(lst1,headers=header,tablefmt="grid"))
print("THE ABOVE TABLES SHOWS A LIST OF WORKOUTS THAT NEED TO BE COMPLETED BY THE USER IN A TIME SPAN OF 30-MINUTES TOTAL")
print("IF YOU FAIL TO COMPLETE ALL OF THEM IN THE GIVEN SPAN OF TIME , DONT WORRY , JUST INPUT THE INFORMATION OF HOW MANY EXERCISES YOU HAVE DONE")
print("IT IS COMPULSORY TO ATTEND EACH AND EVERY EXERCISE AS THIS TEST DETERMINES YOUR OVERALL HEALTH AND WILL HELP BeFit TO KNOW YOU BETTER")

#Displaying image of workouts
img1=Image.open("fit test.jpg")
img1.show()
lst3=[]
lst7=[]

#Input details of fitness test
print("Input your records")
lst2=["Shuttle Run","Lunges","Crunches","Squats","Plank"]
d={}
for z in lst2:
    print("Enter no of",z)
    num=str(input(":"))
    num1=int(num)
    lst4=[z,num]
    lst7.append(num1)
    t=tuple(lst4)
    lst3.append(t)
    d[z]=num
header=["SrNo.","Exercises","no of times"]
count1=0
count2=0
d1={"Shuttle Run":12,"Lunges":20,"Crunches":14,"Squats":16,"Plank":35}

#Remarks
def main():
    global d1
    global count1
    global count2
    global rem1
    lst5=list(d1.values())    
    for z in range(len(lst2)):
        if lst5[z]>=lst7[z]:
           count1+=1
        if lst5[z]<lst7[z]:
           count2+=1
    if count1>count2:
        rem1="Well Done !!!"
        print(tabulate(lst3,headers=header,tablefmt="grid"))
        print("very good")
    else:
        rem1="Can do better!!"
        print(tabulate(lst3,headers=header,tablefmt="grid"))
        print("can do better")
        print("We suggest you to fill  out a health report ....")

#Fitness test (age/weight) wise
#Agegrp-1
if age>=15 and age<=30:
    def agegrp1():
       if weight>=40 and weight<=65:
           d1={"Shuttle Run":12,"Lunges":20,"Crunches":14,"Squats":16,"Plank":35}
           main()
       elif weight>65 and weight<100:
           d1["Shuttle Run"]=10
           d1["Lunges"]=15
           d1["Crunches"]=12
           d1["Squats"]=15
           d1["Plank"]=30
           main()
       else:
            pass
       return d1
    agegrp1()
    
# agegrp-2
elif age>30 and age<=45:
    def agegrp2():
        if weight>=40 and weight<=60:
           d1["Shuttle Run"]=10
           d1["Lunges"]=16
           d1["Crunches"]=12
           d1["Squats"]=16
           d1["Plank"]=25
           main()
        if weight>65 and weight<100:
            d1["Shuttle Run"]=9
            d1["Lunges"]=16
            d1["Crunches"]=12
            d1["Squats"]=16
            d1["Plank"]=20
            main()
        return d1
    agegrp2()
    
# agegrp-3
elif age>45 and age<=60:
    def agegrp3():
         if weight>=40 and weight<=60:
           d1["Shuttle Run"]=10
           d1["Lunges"]=16
           d1["Crunches"]=12
           d1["Squats"]=16
           d1["Plank"]=25
           main()
         if weight>65 and weight<100:
            d1["Shuttle Run"]=5
            d1["Lunges"]=12
            d1["Crunches"]=12
            d1["Squats"]=12
            d1["Plank"]=20
            main()
         return d1
    agegrp3()
#Options
print("WELCOME TO STAGE 2")
print("BELOW ARE OPTIONS PROVIDED FOR YO TO CHOOSE BETWEEN FILLING OUT A HEALTH REPORT OR CONTINUING WITH THE AVAILABLE WORKOUTS")
print("MENU--------------------------------OPTIONS")
print("TO CONTINUE BY FILLING OUT A HEALTH REPORT-----------1")
print("TO CONTINUE WITH THE AVAILABLE WORKOUTS(MEDIUM/ADVANCE)----------------2")
gui = Tk(className='Python Examples - Button')
gui.geometry("250x80")
# create button
button = Button(gui, text='PROCEED', width=40, height=5, bg="blue", fg="white")
# add button to gui window
button.pack()
gui.mainloop()
opt=int(input("ENTER YOUR CHOICE:"))
#Yoga exercises
def yoga():
             qr="create table Yoga7(YogaExercise char(50))"
             mycursor.execute(qr)
             print("YOGA IS SCHEDULES FOR NEXT 2 DAYS")
             print("Remember, try to hold each pose for 15 seconds, and breathe for those 15 seconds. It is common when first starting to get lost in your mind due to the discomfort. Allow your breath to bring you back to center.")
             print("Also to allow yourself to rest one minute between sets, and one minute after, preferably in Savasana, known as Corpse Pose. This is the ultimate resting pose, and is actually much harder than it looks when first starting out!")
             mycursor.execute("insert into Yoga7 values('Marjaryasana and Bitilasana(Cat and Cow)')")
             mycursor.execute("insert into Yoga7 values('Adho mukha svanasana(Downward Facing Dog)')")
             mycursor.execute("insert into Yoga7 values('Anuvittasana(Standing Backbend)')")
             mycursor.execute("insert into Yoga7 values('Virabhadrasana II(Warrior II)')")
             mycursor.execute("insert into Yoga7 values('Trikonasana(Triangle)')")
             mycursor.execute("insert into Yoga7 values('Uttanasana(Standing Forward Fold)')")
             mycursor.execute("insert into Yoga7 values('Bhujangasana(Cobra)')")
             mycursor.execute("insert into Yoga7 values('Kapotasana(Pigeon)')")
             mycursor.execute("insert into Yoga7 values('Paschimottanasana(Seated Forward Fold)')")
             mycursor.execute("insert into Yoga7 values('Savasana(Resting Pose)')")
             mycon.commit()
             
#Presumed 24 Hour timer
global x
x=[]
global y
y=[]
global countday
global pgsc
countday=0
pgsc=0
t=3
def countdown(t):
        while t:
                mins,secs=divmod(t,60)
                timer='{:02d}:{:02d}'. format(mins,secs)
                print(timer,end="\r")
                time.sleep(1)
                t-=1
        
def days(countday=0,pgsc=0):
           day=1
           while day<2:
              print("have you done your workout today?------yes or no")
              n=input("enter your answer")
              if n.lower()=="yes":
                  x.append(countday)
                  y.append(pgsc)
                  countday+=1
                  pgsc+=2
              if n.lower()=="no":
                  x.append(countday)
                  y.append(0)
                  countday+=1
                  pgsc-=4
              day+=1
countday=0
pgsc=0
def graph():
             c=0
             global countday
             global pgsc
             countday=0
             pgsc=0
             while c<14:
                    countdown(3)
                    countday+=1
                    pgsc+=2
                    days(countday,pgsc)
                    c+=1

#First option
if opt==1:
     webbrowser. open("https://docs.google.com/forms/d/e/1FAIpQLSdRmiCpc1AYBzwfGv5Uiwm8aDa-t197klvlCdGc1JBkQg4B-Q/viewform?gxids=7628")
     hr1=open("HR Ans.csv",'r')
     hr2=csv.reader(hr1)
     list1=[]
     for s in hr2:
        list1.append(s)
a=list1[1]
print(a)
def opt1():
              qr="create table HeartProblem(Cardio varchar(50),Sets char(30),CoreWorkout char(50),Sets1 char(30))"
              mycursor.execute(qr)
              print("WORKOUT IS SCHEDULED FOR THE NEXT 14 DAYS")
              print("The following workout is divided into alternate sections of 5 days cardio and 2 days yoga for the upcoming 14 days")
              print("Remember to take rest of 120sec between every set")
              mycursor.execute("insert into HeartProblem values('Run 2km','1','crunches','8x2')")
              mycursor.execute("insert into HeartProblem values('Rest','180sec','Rest','20sec')")
              mycursor.execute("insert into  HeartProblem values('Skipping','100x2','Leg Raises','10x2')")
              mycursor.execute("insert into  HeartProblem values('Rest','120sec','Rest','20 sec')")
              mycursor.execute("insert into  HeartProblem values('Lunges','8x2','Leg Scissors','10x2')")
              mycursor.execute("insert into  HeartProblem values('Rest','120sec','Toe Touch','10sec each leg')")
              mycursor.execute("insert into  HeartProblem values('Standing quadriceps stretch','1 each leg x2','Butterfly Stretch','15 sec')")
              mycursor.execute("insert into  HeartProblem values('Plank','30sec','Childs Pose','20sec')")
              mycon.commit()
              img2=Image.open("HP2.jpg")
              img2.show()
              img3=Image.open("HP1.jpg")
              img3.show()
def opt2():
              qr="create table RespProble3(Cardio varchar(50),Sets char(50),CoreWorkout char(50),Sets1 char(50))"
              mycursor.execute(qr)
              print("WORKOUT IS SCHEDULED FOR THE NEXT 14 DAYS")
              print("The following workout is divided into alternate sections of 5 days cardio and 2 days yoga for the upcoming 14 days")
              print("Remember to take rest of 120sec between every set")
              mycursor.execute("insert into RespProble3 values('Run 1km','1x2','crunches','8x2')")
              mycursor.execute("insert into RespProble3 values('Rest','180sec','Side Leg Raises','10x2')")
              mycursor.execute("insert into RespProble3 values('Squat Jumps','10x2','Leg Raises','10x2')")
              mycursor.execute("insert into RespProble3 values('Rest','120sec','Rest','20 sec')")
              mycursor.execute("insert into RespProble3 values('Lunges','8x2','Leg Scissors','10x2')")
              mycursor.execute("insert into RespProble3 values('Standing quadriceps stretch','1 each leg x2','Butterfly Stretch','15 sec')")
              mycursor.execute("insert into RespProble3 values('Plank','30sec','Childs Pose','20sec')")
              mycon.commit()
              img4=Image.open("RP1.jpg")
              img4.show()
              img5=Image.open("RP2.jpg")
              img5.show()
def opt3():
              qr="create table JointProble6(Cardio varchar(50),Sets char(50),CoreWorkout char(50),Sets1 char(50))"
              mycursor.execute(qr)
              print("WORKOUT IS SCHEDULED FOR THE NEXT 14 DAYS")
              print("The following workout is divided into alternate sections of 5 days cardio and 2 days yoga for the upcoming 14 days")
              print("Remember to take rest of 120sec between every set")
              mycursor.execute("insert into JointProble6 values('Run 2km','1','crunches','8x2')")
              mycursor.execute("insert into JointProble6 values('Rest','180sec','Hamstring Stretch','20sec each leg x2')")
              mycursor.execute("insert into JointProble6 values('Skipping','100x2','Leg Raises','10x2')")
              mycursor.execute("insert into JointProble6 values('Rest','120sec','Rest','20 sec')")
              mycursor.execute("insert into JointProble6 values('Leg Extentions','8x2','Leg Scissors','10x2')")
              mycursor.execute("insert into JointProble6 values('Calf Exercises','5x2','Toe Touch','10sec each leg')")
              mycursor.execute("insert into JointProble6 values('Standing quadriceps stretch','1 each leg x2','Butterfly Stretch','15 sec')")
              mycursor.execute("insert into JointProble6 values('Plank','30sec','Childs Pose','20sec')")
              mycon.commit()
              img6=Image.open("JP1.jpg")
              img6.show()
              img7=Image.open("JP2.jpg")
              img7.show()

#Giving exercises on the basis of health problems
if a[4]=='Heart Problem':
             print("Here are the list of exercises we recommend you to do!!!!")
             opt1()
             yoga()
             graph()
if  a[4]=='Respiratory Distress':
             print("Here are the list of exercises we recommend you to do!!!!")
             opt2()
             yoga()
             graph()
if a[4]=="Joint Problem":
             print("Here are the list of exercises we recommend you to do!!!")
             opt3()
             yoga()
             graph()
hr1.close()
countday=0
pgsc=0
def graph1():
              global countday
              global pgsc
              c=0
              while c<5:
                    countdown(3)
                    countday+=1
                    pgsc+=2
                    days(countday,pgsc)
                    c+=1
def graph2():
             global countday
             global pgsc
             c=0
             while c<2:
                    countdown(3)
                    countday+=1
                    pgsc+=2
                    days(countday,pgsc)
                    c+=1


#Second options
print("AS YOU CHOSE TO CONTINUE WITH THE AVAILABLE WORKOUTS")
print("BELOW DISPLAYED ARE THE 2 TYPES OF WORKOUTS THAT WE AT BeFit PROVIDE")
print("MEDIUM LEVEL - WHERE WE GIVE YOU WORKOUTS ACCORDING TO YOUR INFORMTAION UP TILL NOW")
print("ADVANCE LEVEL - WHERE WE GIVE MORE CUSTOMISED WORKOUTS , BUT YOU NEED TO SUBSCRIBE FOR THEM!!")
if opt==2:
     print("MENU---------------->options")
     print("MEDIUM LEVEL----->1")
     print("ADVANCE LEVEL(Subscription Required)----->2")
     opt2=int(input("ENTER YOUR CHOICE:"))
     if opt2==1:
          def opt1():
#Medium level
              if age>=15 and age <=30:
                 if weight>=40 and weight<=65:
                       qr="create table Medium3(Cardio varchar(50),Sets char(10),CoreWorkout char(50),Sets1 char(50))"
                       mycursor.execute(qr)
                       print("Workout is scheduled for next 14 days")
                       mycursor.execute("insert into Medium3 values('Run 2km','1','crunches','10x2')")
                       mycursor.execute("insert into Medium3 values('Jumping Jacks','10x2','Rest','20sec')")
                       mycursor.execute("insert into Medium3 values('Rest','120 sec ','Leg Scissors','10x2')")
                       mycursor.execute("insert into Medium3 values('Squat Jumps','10x2','Rest','20 sec')")
                       mycursor.execute("insert into Medium3 values('Lunges','10x2','Leg Raises','10x2')")
                       mycursor.execute("insert into Medium3 values('Mountain Climbers','20x2','Toe Touch','10sec x2')")
                       mycursor.execute("insert into Medium3 values('Pushups','15x2','Rest','20 sec')")
                       mycon.commit()
                       img8=Image.open("med1.jpg")
                       img8.show()
                       img9=Image.open("med1.1.jpg")  
                       img9.show()
                 elif weight>65 and weight<=100:
                       qr="create table Medium2(Cardio varchar(50),Sets char(10),CoreWorkout char(50),Sets1 char(50))"
                       mycursor.execute(qr)
                       print("Workout is scheduled for next 14 days")
                       mycursor.execute("insert into Medium2 values('Run 2km','1','crunches','7x2')")
                       mycursor.execute("insert into Medium2 values('Jumping Jacks','7x2','Rest','20sec')")
                       mycursor.execute("insert into Medium2 values('Rest','120 sec ','Leg Scissors','10x2')")
                       mycursor.execute("insert into Medium2 values(Skipping','3minsx2','Rest','20 sec')")
                       mycursor.execute("insert into Medium2 values('Lunges','10x2','Leg Raises','8 x2')")
                       mycursor.execute("insert into Medium2 values('Mountain Climbers','10x2','Toe Touch','10secx2')")
                       mycursor.execute("insert into Medium2 values('Plank','30sec x2','Rest','20 sec')")
                       mycon.commit()
                       img10=Image.open("med2.1.jpg")
                       img10.show()
                       img11=Image.open("med2.2.jpg")
                       img11.show()
              elif age>30 and age<=45:
                 if weight>=40 and weight<=65:
                      qr="create table Medium2(Cardio varchar(50),Sets char(10),CoreWorkout char(50),Sets1 char(50))"
                      print("Workout is scheduled for next 14 days")
                      mycursor.execute("insert into Medium2 values('Run 2km','1','crunches','10x2')")
                      mycursor.execute("insert into Medium2 values('Jumping Jacks','10x2','Rest','20sec')")
                      mycursor.execute("insert into Medium2 values('Rest','120 sec ','Leg Scissors','10x2')")
                      mycursor.execute("insert into Medium2 values('Squat Jumps','7x2','Rest','20 sec')")
                      mycursor.execute("insert into Medium2 values('Lunges','10x2','Leg Raises','10x2')")
                      mycursor.execute("insert into Medium2 values('Mountain Climbers','16x2','Toe Touch','10secx2')")
                      mycursor.execute("insert into Medium2 values('Pushups','15x2','Rest','20 sec')")
                      mycon.commit()
                      img12=Image.open("med1.jpg")
                      img12.show()
                      img13=Image.open("med2.2.jpg")
                      img13.show()
                 if weight>65 and weight<=100:
                      qr="create table Medium2(Cardio varchar(50),Sets char(10),CoreWorkout char(50),Sets1 char(50))"
                      mycursor.execute(qr)
                      print("Workout is scheduled for next 14 days")
                      mycursor.execute("insert into Medium2 values('Run 2km','1','crunches','7x2')")
                      mycursor.execute("insert into Medium2 values('Jumping Jacks','7x2','Rest','20sec')")
                      mycursor.execute("insert into Medium2 values('Rest','120 sec ','Leg Scissors','10x2')")
                      mycursor.execute("insert into Medium2 values(Skipping','2minsx2','Rest','20 sec')")
                      mycursor.execute("insert into Medium2 values('Lunges','10x2','Leg Raises','8 x2')")
                      mycursor.execute("insert into Medium2 values('Mountain Climbers','10x2','Toe Touch','10secx2')")
                      mycursor.execute("insert into Medium2 values('Plank','30sec x2','Rest','20 sec')")
                      mycon.commit()
                      img14=Image.open("med2.1.jpg")
                      img14.show()
                      img15=Image.open("med2.2.jpg")
                      img15.show()
              elif age>45 and age<=60:
                 if weight>=40 and weight<=65:
                     qr="create table Medium2(Cardio varchar(50),Sets char(10),CoreWorkout char(50),Sets1 char(50))"
                     print("Workout is scheduled for next 14 days")
                     mycursor.execute("insert into Medium2 values('Run 1.5km','1','crunches','10x2')")
                     mycursor.execute("insert into Medium2 values('Jumping Jacks','7x2','Rest','20sec')")
                     mycursor.execute("insert into Medium2 values('Rest','120 sec ','Leg Scissors','10x2')")
                     mycursor.execute("insert into Medium2 values('Squat Jumps','7x2','Rest','20 sec')")
                     mycursor.execute("insert into Medium2 values('Lunges','10x2','Leg Raises','10x2')")
                     mycursor.execute("insert into Medium2 values('Mountain Climbers','16x2','Toe Touch','10secx2')")
                     mycursor.execute("insert into Medium2 values('Pushups','15x2','Rest','20 sec')")
                     mycon.commit()
                     img16=Image.open("med1.jpg")
                     img16.show()
                     img17=Image.open("med1.1.jpg")
                     img17.show()
                     
              if weight>65 and weight<=100:
                    qr="create table Medium2(Cardio varchar(50),Sets char(10),CoreWorkout char(50),Sets1 char(50))"
                    cursor.execute(qr)
                    print("Workout is scheduled for next 14 days")
                    cursor.execute("insert into Medium2 values('Run 2km','1','crunches','7x2')")
                    cursor.execute("insert into Medium2 values('Jumping Jacks','7x2','Rest','20sec')")
                    cursor.execute("insert into Medium2 values('Rest','120 sec ','Leg Scissors','10x2')")
                    cursor.execute("insert into Medium2 values(Skipping','2minsx2','Rest','20 sec')")
                    cursor.execute("insert into Medium2 values('Lunges','10x2','Leg Raises','8 x2')")
                    cursor.execute("insert into Medium2 values('Mountain Climbers','10x2','Toe Touch','10secx2')")
                    cursor.execute("insert into Medium2 values('Plank','30sec x2','Rest','20 sec')")
                    mycon.commit()
                    img18=Image.open("med2.1.jpg")
                    img18.show()
                    img19=Image.open("med1.1.jpg")
                    img19.show()
              else:
                    pass

     b=1
     while b<=4:
        if b==1:
            opt1()
            graph1()
            b+=1
            print(b)
        elif b==2:
            yoga()
            graph2()
            b+=1
            print(b)
        elif b==3:
            opt1()
            graph1()
            b+=1
            print(b)
        elif b==4:
            opt1()
            graph2()
            b+=1
            print(b)
        else:
          print("hello")
          break

# Advance Level
if opt2==2:

#Description of advance...
    print("Listed below are three packages  with required subscription amount specially customized by our expert team of trainers ....")
    print("Advance Workout Plan-1 focusses more on cardio and jumps improving heart rate and breathing- Rs.2000-------->1")
    print("Advance Workout Plan-2 focusses more on cardio improving endurance  and speed -Rs.2500------------------------->2")
    print("Advance Workout Plan-3 focusses more on limbs exercises and flexibility-Rs.3000--------------------------------------->3")
    choice=int(input("Enter your choice..."))


#Enter your banking details
    print("FOR SUBSCRIPTION")
    print("Enter the mode of payment----->")
    print("Card payment--------->1")
    print("Google Pay------------>2")
    print("Paytm----------------->3")
    ch=int(input("Enter your choice"))
    if ch==1:

#Enter your card details....
       cdno=input("Enter your card no.")
       if len(cdno)!=19:
            print("Invalid input enter again.")
            cdno=input("Enter your card no.")
            doe=input("Enter date of expiry:")
       else:
           pass
       print("Welcome","name","to fitness station")

#Google Pay
    if ch==2:
        print("Scan QR code...")
        img20=Image.open("qrcode.jpg")
        img20.show()
        print("Welcome","name","to fitness station")

#Paytm
    if ch==3:
        print("Payment to business no.....98765XXXXX")
        print("Welcome","name","to fitness station")

#Advance Workouts....(Table)
    def advance():
        if  choice ==1:
            ADV1a=[("RUN(2KM)","1 set","PLANK TO PUSHUP","8x2","AIR SQUATS","10x2","STANDING QUADRICEPS STRETCH","10sec each side"),
            ("JUMPING JACKS","10x2","DIPS","10x2","PENDULUM LUNGES","10x2","SIDE BENCH STRETCTH","30sec each side"),
            ("SKIPPING","300 skips","INCLINE PUSHUPS","10x2","SINGLE-LEG DEADLIFTS","10x2","ARM-CROSS SHOULDER STRETCH","30sec each side"),
            ("HIGH JUMPS","10x2","","","","","OVERHEAD TRICEP STRETCH","30sec each side"),
            ("","","","","","","CHEST-CROSS ARM SWING","30sec"),
            ("CRUNCHES","10x2","","","","","CHILDS POSE","30sec"),
            ("PLANK","45sec","","","","","SITTING FORWARD BEND TOE-TOUCH","30sec"),
            ("","","","","","","BUTTERFLY STRETCH","30sec"),
            ("","","","","","","CORE ABDOMINAL STRETCH","30sec")]
            ADVH1a=["FULL BODY CARDIO","","ARMS","","LEGS","","COOL-DOWN EXERCISES",""]
            print(tabulate(ADV1a, headers=ADVH1a,tablefmt="grid"))
            img21=Image.open("adv1.jpg")
            img21.show()
            img25=Image.open("adv1.3.jpg")
            img16show()
            img26=Image.open("adv1.2.jpg")
            img16show()

        elif choice==2:
             ADV1b=[("RUN(2KM)","1 set","INCHWORMS","5x2","HIGH KNEES","10x2 each leg","STANDING QUADRICEPS STRETCH","10sec each side"),
             ("BURPEES","10x2","DIPS","10x2","LUNGES","10x2","SIDE BENCH STRETCH","30sec each side"),
             ("SKIPPING","300 skips","PUSHUPS","10x2","SITUPS","10x2","ARM-CROSS SHOULDER STRETCH","30sec each side"),
             ("SPOT JUMPS","20x2","ARM CIRCLES","10x2 each hand","","","OVERHEAD TRICEP STRETCH","30sec each side"),
             ("","","","","","","CHEST-CROSS ARM SWING","30sec"),
             ("LEG RAISES","10x2","","","","","CHILDS POSE","30sec"),
             ("PLANK","45sec","","","","","SITTING FORWARD BEND TOE-TOUCH","30sec"),
             ("","","","","","","BUTTERFLY STRETCH","30sec"),
             ("","","","","","","CORE ABDOMINAL STRETCH","30sec")]
             ADVH1b=["FULL BODY CARDIO","","ARMS","","LEGS","","COOL-DOWN EXERCISES",""]
             print(tabulate(ADV1b, headers=ADVH1b,tablefmt="grid"))
             img27=Image.open("adv2.1.jpg")
             img27.show()
             img28=Image.open("adv2.2.jpg")
             img16show()
             img29=Image.open("adv2.3.jpg")
             img29.show()
     
        elif choice==3:
             ADV1c=[("RUN(2KM)","1 set","PLANK TO PUSHUP","8x2","AIR SQUATS","10x2","STANDING QUADRICEPS STRETCH","10sec each side"),
             ("JUMPING JACKS","10x2","DIPS WITH SINGLE LEG EXTENTION","10x2","BACKLIFTS","10x2 each leg","SIDE BENCH STRETCTH","30sec each side"),
             ("SKIPPING","300 skips","INCLINE PUSHUPS","10x2","PENDULUM LUNGES","10x2","ARM-CROSS SHOULDER STRETCH","30sec each side"),
             ("","","ARM CIRCLES","10x2","","","OVERHEAD TRICEP STRETCH","30sec each side"),
             ("","","","","","","CHEST-CROSS ARM SWING","30sec"),
             ("CRUNCHES","10x2","","","","","CHILDS POSE","30sec"),
             ("PLANK","45sec","","","","","SITTING FORWARD BEND TOE-TOUCH","30sec"),
             ("","","","","","","BUTTERFLY STRETCH","30sec"),
             ("","","","","","","CORE ABDOMINAL STRETCH","30sec")]
             ADVH1c=["FULL BODY CARDIO","","ARMS","","LEGS","","COOL-DOWN EXERCISES",""]
             print(tabulate(ADV1c, headers=ADVH1c,tablefmt="grid"))
             img22=Image.open("adv1.jpg")
             img22.show()
             img23=Image.open("adv2.jpg")
             img23.show()
             img24=Image.open("adv3.jpg")
             img24.show()
        else:
             pass

    b=1
    while b<2:
        advance()
        graph()
        b+=1
        

#Output Details
print("************************************")
for k in finald:
    print(k,finald[k])
    print("**********************************|")
    
#Graph
print(x)
print(y)
grp.plot(x,y)
grp.xlabel('no of days')
grp.ylabel('progress scale')
grp.show()

print("HERE WE COME TO THE END OF YOUR 14 DAYS WORKOUT PLAN")
print("HOPE TO SEE YOU FIT AND ENERGETIC!!!")
print("REGARDS BEFIT")


"""
 This is a program for my chatbot ...
 1. THE BOT WILL START WITH A GREETING MESSAGE AND IT INTRODUCES ITSELF AND ASK FOR YOUR NAME.
 
 2. THE BOT WILL GREET AND SENDS THE WELOCOME MESSAGE TO PERSON.

 3. AND THEN BOT WILL ASK WHAT A PERSON WANT TO DO , IT WILL OFFER A CHOICES OF THINGS TO SELECT BASED ON
    WHAT IT IS DESIGNED FOR .

4. IT WILL RESPOND TO THE GIVEN INPUT AND IN CASE OF BAD INPUT IT ASKS FOR CORRECT INPUT FOR WHICH IT IS DESINGED.
"""
import random
import math
import datetime

# According to the time , it greets the users by saying good morning , good afternoon and good evening
def time():
    x=datetime.datetime.now()
    y=int(x.strftime("%H"))
    if(y>=12 and y<17):
        print("Hello GoodAfternoon ",end=",")
    elif(y>=17 and y<24):
         print("Hello GoodEvening ",end=",")
    else:
        print("Hello GoodMorning ",end=",")


# Details of the item where users are searched for
def items_details(type,item):
    fruits = {"mango":"Calories-60 [Total Carbohydrate-15g , Fat-0.4g , Protein-0.8g ]","apple":"Calories-52 [Total Carbohydrate-14g , Fat-0.2g , Protein-0.3g ]","orange":"Calories-97 [Total Carbohydrate-24g , Fat-0.2g , Protein-1.3g ]" }
    biscuits ={"marie gold":"Calories-406 [Total Carbohydrate-71g , Fat-11g , Protein-7.1g ]","oreo":"Calories-165 [Total Carbohydrate-26g , Fat-5.7g , Protein-4g ]","milk bikis":"Calories-428 [Total Carbohydrate-63g , Fat-15g , Protein-8g ]" }
    vegetables = {"tomato":"Calories-16 [Total Carbohydrate-3.2g , Fat-0.2g , Protein-1.2g ]","potato":"Calories-58 [Total Carbohydrate-12g , Fat-0.1g , Protein-2.6g ]","red chilli":"Calories-40 [Total Carbohydrate-8.8g , Fat-0.4g , Protein-1.9g ]" } 
    print("\n Nutrition values of the item : ",end="")
    try:
        if (type=="fruits"):
            print(item + " contains "+ fruits[item])
        elif(type=="biscuits"):
            print(item+ " contains "+biscuits[item])
        elif(type=="vegetables"):
            print(item+ " contains "+vegetables[item])
        else:
            print("Sorry , we doesn't have the deatils of that item")
    except:
        print("Nutrients of",item,"doesn't found")
    print()
 
# Used to greet the user 
def gretting_message():
    responses=["Hi there! I am Nutribot. I can help you by suggesting Nutritional values of item and also help you to find nutrional values of some items",
                "Hey , I am Nutribot. I can help you by suggesting Nutritional Values of item and also help you to find nutrional values of some items"]
    print(random.choice(responses))

def welcome(name):
    print (" Nice to meet you "+ name + " please select an option given below ")

# Describes the BMI of the user and tells which category you are to maintain your body fit
def suggesting_elements(name):
    print("\n"+name+" could you please provide your details so that we can find your Body Mass Index")
    weight=int(input("Your weight(kgs) : "))
    height=int(input("Your height(feet) : "))
    height2=int(input("your height(inches) : "))
    bmi=(float)(weight/pow((0.3048*height+0.0254*height2),2))
    bmi_str=str(bmi)
    if (bmi>=0 and bmi<18.5):
        print("\n your Body mass index is "+bmi_str+" is low it means that you are underweight . I suggest you to eat some high calorie food to gain weight.")
    elif (bmi>=18.5 and bmi<25):
        print("\n"+ name+" your Body mass index is "+bmi_str+" is average i.e means you are Normal . you are perfectly healthy.")
    elif (bmi>=25 and bmi<30):
        print ("\n"+name+" your Body mass index is "+bmi_str+" is high i.e means you are OverWeight. I suggest you to eat low calorie and low fat food and also suggest you to do some exercise.")
    else:
        print ("\n"+name+" Your Body mass index is "+bmi_str+" is very high i.e means you are Obese. I suggest you to consult a doctor.")
    print()

# Search for items or elements
def search_for_element():
    item_type=input("Enter the type of item you want to search for like fruits,vegetables,biscuits, etc....  : ")
    item_name=input("Enter the name of item you want to search for : ")
    items_details(item_type,item_name)

# Serach for options
def options_menu():
    print("1. Search the information for the item you want.")
    print("2. Want any suggestion to keep your body healty and fit. ")
    print("3. Exit")
    try:
        return int(input("Enter the option you want : "))
    except:
        print("Enter number only from the above options")

# Main function of bot which takes inputs and gives information
def bot():
    gretting_message()
    name=input("Your name : ")
    time()
    welcome(name)
    option = options_menu()
    while(option!=3):
        if (option == 1):
            search_for_element()
        elif (option == 2):
            suggesting_elements(name)
        else:
            print("\n Please select a number from the above options only")
            print()
        option = options_menu()
    print("Thank You for using this Chatbot")

bot()
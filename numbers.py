numbers = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
Nums2=numbers[::]
print(numbers[0::2])
print (80 // 5)
print(80 % 3)
nums = numbers.split()
Nums= nums.reverse
print(Nums)
name ="arshan atahskar"
namesplit = name.split()
print(nums)
print(namesplit[::1])
names = namesplit * 3
print(names)
piazza_price=300
pizza_people=5
print(pizza_people * piazza_price)
pizza_share=pizza_people * piazza_price
print(pizza_share ** 2 )
piazza_price=400
print(piazza_price)
format = f"pizza price was a little high and was {piazza_price} and we were {pizza_people} and each of our share was {pizza_share}"
print(format)
Format= f"my name is {name} and i love {80//3} and i love {Nums2}"
print(Format)
shopping_list = ['chair','labtop','bottle',piazza_price,'game','ps4','ps5','pen','headphone', 342,3.16,3,8]
print(shopping_list)
Name=name.upper()
#lower or upper or anthing that need '.lower or something else' is for strings not list.
Names=name.capitalize()
print(Name,Names)
print(shopping_list[0:10:])
#next day i have to practice .append() and .pop
NUmbers= shopping_list.pop()
NumberS = shopping_list.append(21)
print(NUmbers,NumberS)
print(shopping_list)
#append gonne plus one word that i want in end of the list and .pop is going to remove last word of the list.this thing only work on list not string.
text="hello" + "!" + "?"
Text= text + "!"
print(Text)
#django
_set=set([1,2,3,4,5,5,"arshia"])
print(_set)
_set.add(67)
print(_set) 
setA={1,2,3,4}
setB={3,4,5,6,}
U_set= setA.union(setB) #اجتماع
print(U_set)
U_Set=setA.intersection(setB) #اشتراک
print(U_Set)
print(2>1)
print(1>2)
a=False
print(type(a))
age=45
height=180
if age>45  or  height<=180:
    print("true")
else:
    print("false")

age=18
score=17
if age >=18 and score>=16 :
    print("Accepted")
else:
    print("Rejected")

age=16
height=180
if age>16 and height>185:
    print("can join")
else:
    print("cannot join")

score=11

if score >=18:
    print("very good ")
elif score in (15,16,17):
        print("good")
elif score in (11,12,13,14):
     print("more try")
else:
    if score <=10:
         print("bad")

username = "arshan"
password = "1234"

input_username = "arshan"
input_password = "1234"

if input_username==username and input_password==password :
     print("login successful")
elif input_username!=username :
     print("Username Incorrect")
else:
     if  input_username==username and input_password!=password:
          print("Password Incorrect")
          
age=17
vip=False
banned=True

if banned==True:
     print("Access Denied")
elif age>=18 or vip==True:
     print("Access Granted")
else:
     if age>=18 or vip==False:
          print(" Not Old Enough")


name="arshan"
if name== "":
     print ("Please enter your name")
else:
     if name==name:
          print("Welcome",name)


students = {
    "arshan": {"age": 17, "score": 19},
    "sara": {"age": 18, "score": 15},
    "ali": {"age": 20, "score": 8},
    "mobina": {"age": 16, "score": 20}
}
if students["arshan"]["score"]>=18:
     print("Excellent")

for name in students:
   if students[name]["score"]>= 18:
        print(name,'Excellent')
   elif score >= 15:
     print(name, "Good") 
   else: print(name, "Try Harder")

user=[]
username="Arshan"
password="123456"

input_username="Arshan "
input_password="123456"

if len(input_username)>=4:
   print("Registration Successful")
elif  " " in input_username:
     print("Username cannot contain spaces")
import os 
print("FILE IS HERE:", os.path.abspath("name.txt"))

name=input("what is your name:? ")
print("Hello",name)
print("i love you",name)

file =open("name.txt","a")
file.write(name +"\n") 
file.close()

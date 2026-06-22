class_name="D"
number_student = 4
student= f"""class_{class_name} have {number_student} student 
names:[ali , sara , mobina , arad]"""
#print(student)

grade_12 = {"class_1":{
    "yuji":{
        "age":18 ,
          "score":[14,15,10]
    },
    "megumi":{
        "age":18 , 
        "score":[19,19,20]
    },
    "nobara":{
        "age":18,
        "score":[17,18,17]
    },
},
             "class_2":{
    "todo":{
        "age":19,
           "score":[20,20,20]
             
    
    }, 
    "choso":{
        "age":150,
            "score":[0,0,0]
    },
    "maki":{
        "age":19,
           "score":[14,18,18]
    }
             }}
#print(grade_12.keys())
#print(grade_12.values())
for class_name in grade_12:
    for name in grade_12[class_name]:
        for  personal_info,value in grade_12[class_name][name].items():
            print(personal_info,value)
#with .item() i can get more than one thin in dict.for example ,
#we can consider functon.one in and one out.give me BOTH key and value together”
for Class_name, Student in grade_12.items():
    for name , info in Student.items():
        print(name,info["age"], info["score"])
top_score=0
top_student=""
#for class_anme , for_student in grade_12.items():
import math
coordinates=(3,4)
x1 , y1=coordinates
x2 ,y2 =(0,0)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #تاپل
print(distance)
#sqrt mean جذر 
animals=("bird","angry bird","tiger","eagle")  
for animal in animals:
    print(len(animal))
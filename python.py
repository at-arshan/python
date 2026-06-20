name = "arshan"
lastname = "atashkar"
age = "19"
summery = """my name is arshanatashkarand.
im very happy to work in python"""
print(summery[0:  :1])
number ="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
print(number)
print(number[0: 30 :3])
nums = number.split()
print(nums[::3])
personal_info = summery.split()
print(personal_info[::1])
ages = age * 4
print(ages)
print(type(ages))
person={"ali":100 
        ,
          "sara":200
            , 
            "mmd":300 }
print(person["ali"])

class_student={
    1:{ 
        "mmd":20,
        "sara":18,
        "artin":17
        } , 
        "two":
        {"john":20
         ,"dexter":20
         ,"walter white":22
         }
}
print(class_student[1])
class_A= {
    1:
    ["ali"
     ,"sara"
     ,"artin"
     ,"rozbeh"
     ,"namazian"
     ],
       2:
       ["asghar"
        ,"arman"
        ,"marvel"
        ,"arshia"
        ,"arshan"
        ,"shideh"
        ]
        }
print(class_A[1])
print(class_A[2])
print(class_A.keys())
print(class_A.values())
print(class_A.items())
print(class_A.get(2))
print(class_A[1][0].upper())
print(class_A[1][1].upper())
print(class_A[1][2].upper())
pen_cost={
    1:
    {"blue":10 
      , "red":10 
      , "black":15
      },
        2:
        {"grenn":25
          , "yellow":30
            , "green":25 
                , "pink":23}}
print(pen_cost)
students = {"class_B":
{"mmd":
 {"age":18
  ,"height":178
  ,"avg":17
  ,"subjects": ["Math", "Physics", "Chemistry"]
 },
   "sara":
  {"age":18
  ,"height":156
  , "avg":19
  , "subjects": ["Math", "Physics", "Chemistry"]
     } ,
   "ali":
    {"age":18
  ,"height":184
  , "avg":15
  , "subjects": ["Math", "Physics", "Chemistry"]
  }
          } ,
           "class_C":{
  "arshan":
    {"age":19
  , "height":184
  , "avg":17
  ,  "subjects": ["Math", "Physics", "Chemistry"]
  }
  , "matin":{
    "age":18
  , "height":172
  , "avg":15
  ,  "subjects": ["Math", "Physics", "Chemistry"]
  }
            }} 
print(students["class_B"]["mmd"]["age"])
print(students["class_C"]["arshan"]["avg"])
print(students["class_B"].values())
print(students.keys())
#f"i have students name {students['class_B'].keys}
for i in students:
    print(i)
    print(students[i].keys())

for w in class_student:
    print(w)
    print(class_student[w].keys())

for s in class_student:
    print(class_student[w].values())
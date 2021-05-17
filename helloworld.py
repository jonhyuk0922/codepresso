"""def getAge():
    age = input("take a age")
    if(age.isdigit()):
        return int(age)
    else:
        return 0

age = getAge()
print(age)


def greet_user(username):
    print("hello,"+ username.title()+"!")

greet_user('Jesse')

def avg(math=0,eng=0,kor=0):
    avg = (math*1.1) + (eng*1.2) + (kor*1.4) /3
    return ave


print(avg(84,70))     
print(avg(90,60))

def menu(morning, afternoon, dinner):
    print(f'morning is {morning}\n,lunch is {afternoon}\n, dinner is {dinner}\n')

menu(morning='a',afternoon='b',dinner='c')
menu(morning = "chicken" , afternoon = "noodle" , dinner = "rice") 

def myFunc(menu, result = "1234"):
     print(menu)
     print(id(result))
     print(result)

myFunc("testmenu1")
myFunc("testmenu2") 


def testFunc(pos1,pos2,pos3, *args):
    print(pos1,pos2,pos3,args);

testFunc("1","2","3","args1","args2") 


def avg(*args):
    score_avg = sum(args)/len(args)
    return score_avg

print(avg(84,69,75))
print(avg(87,90,89,95)) 

def grade(**scores):
    print(f"subject{scores.keys()}")
    print(f"score{scores.values()}")
    score_avg = sum(scores.values())/len(scores.values())
    if score_avg >= 90:
        grade = "A"
    elif score_avg >= 80:
        grade = "B"
    elif score_avg >= 70:
        grade = "C"
    else:
        grade = "F"
    return grade
print(grade(korean=100, english=60))
print(grade(math=80, korean=50, english=60)) """


class Student:
    def __init__(self,name,korean,english,math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

        print(self.name, "생성")
        
    def do_midterm_exam(self):
        print("do_midterm_exam")

    def get_sum(self):
        return self.korean + self.english + self.math
        

jessy = Student('jessy',
              korean=90,
              english=30,
              math=40)

print(id(jessy))
jay= Student('jay',
             korean=20,
             english=30,
             math=40)
print(id(jay))

jessy = Student('jessy',90,60,90)
beth = Student('beth',90,90,90)
jay = Student('jay',90,60,60)

students =(jessy, beth, jay)
scores = [student.get_sum() for student in students]
print('total',sum(scores))
print('average',sum(scores)/len(scores))

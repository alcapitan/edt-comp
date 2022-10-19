from datetime import datetime

class Person():
    def __init__(self):
        self.timetable = {}
        self.name = None
        for i in range(7):
            self.timetable[i] = [None for j in range(7)]
    
    def generate(self,timetable):
        # self.changeName(timetable.name) à changer !!!!!!
        for i in range(len(timetable)):
            print(timetable.keys())
            if i in timetable.keys():
                self.generateDay(i,timetable[i])
            else:
                self.generateDay(i,[Null for j in range(4)])
    
    def generateDay(self,day,hours):
        for i in range(7):
            self.generateHour(day,i,hours[i])
    
    def generateHour(self,day,moment,hour):
        self.timetable[day][moment] = hour
    
    def changeName(self,newName):
        self.name = newName


def display(person):
    dayName = {0:'lundi',1:'mardi',2:'mecredi',3:'jeudi',4:'vendredi',5:'samedi',6:'dimanche'}
    print(person.name.upper())
    for day in person.timetable:
        print(f"{dayName[day].capitalize()} : ")
    return

"""currentTime = datetime.now().strftime("%H:%M")
print(currentTime)"""


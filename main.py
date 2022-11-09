from datetime import datetime

class Person():
    def __init__(self):
        self.timetable = {}
        self.name = None
        for i in range(7):
            self.timetable[i] = [None for j in range(4)]
    
    def changeName(self,newName):
        self.name = newName
    
    def generate(self,timetable):
        for day in self.timetable.keys():
            if day in timetable.keys():
                self.generateDay(day,timetable[day])
            else:
                self.generateDay(day,[None for i in range(4)])
    
    def generateDay(self,day,hours):
        for i in range(4):
            self.generateHour(day,i,hours[i])
    
    def generateHour(self,day,moment,hour):
        self.timetable[day][moment] = hour


def display(person):
    dayName = {0:'lundi',1:'mardi',2:'mercredi',3:'jeudi',4:'vendredi',5:'samedi',6:'dimanche'}
    print(person.name.upper())
    for day in person.timetable:
        courseMorning = not((person.timetable[0] == None) and (person.timetable[1] == None))
        courseAfternoon = not((person.timetable[2] == None) and (person.timetable[3] == None))
        if courseMorning and courseAfternoon:
            print("Pas cours ce jour.")
        else:
            print(f"{dayName[day].capitalize()} : {person.timetable[day]}")
    return

"""currentTime = datetime.now().strftime("%H:%M")
print(currentTime)"""


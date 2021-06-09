# think of a class as a template for new objects

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

#p = Point(2,8)
#print(f"p(x,y) = ({p.x},{p.y})")

class Flight():
    def  __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats(): # it's equivalent to say "if self.open_seats == 0"
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Hermione", "Ron", "Ginny", "Draco"]

for person in people:
    if flight.add_passenger(person):
        print(f"Passenger '{person}' added successfully")
    else:
        print(f"Sorry, passenger {person} is overbooked")

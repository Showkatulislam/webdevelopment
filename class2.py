class Flight():
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.passengers=[]

    def add_passengers(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passengers)


fl=Flight(3)

people=["jayed","mukter","shaik","tamim"]


for p in people:
    success=fl.add_passengers(p)
    if success:
        print(f"added {p} to flight successfully")
    else:
        print(f"added {p} to flight not  successfully")




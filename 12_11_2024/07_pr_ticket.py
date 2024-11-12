class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f"the name of the train is {self.name}")
        print(f"the ticket available in  the train are {self.seats}")
    def fareInfo(self):
        print("the price of a ticket is Rs {self.fare}")
    def bookTicket(self):
        if( self.seats>0):
            print("your ticket is booked! your ticket no is {self.seats}")
            self.seats = self.seats-1
        else:
            print("the train is full! kindly try again")    
intercity = Train("intercity express:  10221", 90  ,1 )
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()

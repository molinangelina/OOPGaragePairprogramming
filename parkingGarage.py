class ParkingGarage():
    def __init__ (self, tickets = list(range(1, 21)), currentTicket = dict(), parkingSpaces = list(range(1, 21))):
        self.tickets = tickets
        self.currentTicket = currentTicket
        self.parkingSpaces = parkingSpaces  

    def payForParking(self):
        while True:
            
            payment= input("Please pay $5 before taking your ticket. (enter total payment: 5) ")
            if payment == "5":
                self.currentTicket["paid"] = "True"
                print("Thank you for paying. You have 15 minutes to leave")
                break
            else:
                print("Invalid response. Please enter 5")
                
    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()
        
    def leaveGarage(self):
        value = "True"
        if value in self.currentTicket.values():
            print("Thank you, have a nice day!")
                
        else:
            print("Please pay for ticket")
            self.payForParking()
            
        self.tickets.append(20)
        self.parkingSpaces.append(20)
            


        
        
pg1 = ParkingGarage()
pg1.takeTicket()
pg1.payForParking()
pg1.leaveGarage()





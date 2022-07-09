class ParkingGarage():
    def __init__ (self, tickets = [], currentTicket = {}, parkingSpaces = []):
        self.tickets = tickets
        self.currentTicket = currentTicket
        self.parkingSpaces = parkingSpaces  

    def takeTicket(self):
        self.tickets -= 1
        self.parkingSpaces -= 1

    def payForParking(self):
        payment= input("Please pay $5 before taking your ticket")
        

    def leaveGarage(self):